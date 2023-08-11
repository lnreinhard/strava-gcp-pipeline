# IMPORT MODULES
import os
from tqdm import tqdm
import json
import pandas as pd
import requests
import urllib3
from google.cloud import storage

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def hello_pubsub(event, context):

    #SET ENVIRONMENT VARIABLES
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    refresh_token = os.environ.get("REFRESH_TOKEN")

    # DEFINE FUNCTION TO GET NEW ACCESS TOKEN
    def get_access_token(client_id, client_secret, refresh_token):
    
        oauth_url = 'https://www.strava.com/oauth/token'
    
        payload = {
            'client_id': client_id, 
            'client_secret': client_secret, 
            'refresh_token': refresh_token, 
            'grant_type': 'refresh_token', 
            'f': 'json', 
        }
    
        r = requests.post(oauth_url, data=payload, verify=False, timeout=30)
        
        access_token = r.json()['access_token']
        return access_token
    

    # GET NEW ACCESS TOKEN
    print("Getting new access token...")
    access_token = get_access_token(client_id, client_secret, refresh_token)
    print("Access token obtained:", access_token)


    # DEFINE FUNCTION TO GET STRAVA DATA
    def get_data(access_token, per_page=200, page=1):
    
        activities_url = 'https://www.strava.com/api/v3/athlete/activities'
        headers = {'Authorization': 'Bearer ' + access_token}
        params = {'per_page': per_page, 'page': page}
        
        data = requests.get(
            activities_url, 
            headers=headers, 
            params=params
        ).json()
        
        return data

    # GET STRAVA DATA
    max_number_of_pages = 10
    data = list()
    print("Fetching Strava data...")
    for page_number in tqdm(range(1, max_number_of_pages + 1)):
        page_data = get_data(access_token, page=page_number)
        if page_data == []:
            break
        data.append(page_data)
    print("Strava data fetched.")
    

    # DATA DICTIONARIES
    data_dictionaries = []
    for page in data:
        data_dictionaries.extend(page)


    # PRINT NUMBER OF ACTIVITIES
    print('Number of activities downloaded: {}'.format(len(data_dictionaries)))

    data_json = json.dumps(data_dictionaries)

    storage_client = storage.Client()
    bucket_name = os.environ.get("BUCKET_NAME")

    print("Uploading data to Google Cloud Storage...")

    def upload_to_bucket(blob_name, file, bucket_name, content_type):
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_string(file, content_type)
            return True
        except Exception as e:
            print(e)
            return False

    upload_to_bucket("strava_raw", data_json, bucket_name, "application/json")
    print("Data upload completed.")