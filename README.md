# Introduction
This project provides the source code for a Google Cloud Function that interacts with the Strava API, retrieves activity data, and stores it in a Google Cloud Storage bucket. The function is designed to be executed by a scheduler every 30 minutes, ensuring that the latest activity data is regularly fetched and stored.

# Code Explanation

The primary functionalities of the code include:

1. Fetching data from the Strava API: The code integrates with the Strava API to retrieve activity data. This includes information such as distance, duration, elevation, and more for each activity.

2. Converting activities to JSON: The fetched activity data is then transformed into JSON format, making it easy to work with and analyze.

3. Writing to Google Cloud Storage: The resulting JSON file is written to a designated Google Cloud Storage bucket. This allows for efficient storage and enables further processing or analysis of the activity data.

The Google Cloud Function, powered by this code, serves as an automated solution for keeping the activity data up-to-date in a centralized storage location. By executing the function on a scheduled basis, it ensures that the most recent activities are consistently captured and made available for downstream processes or analysis.

# Usage

To utilize this Google Cloud Function and automate the retrieval and storage of Strava activity data, follow these steps:

**1. Prerequisites:** Before getting started, ensure you have the following prerequisites in place:

* A Google Cloud Platform (GCP) project with billing enabled.
* The Google Cloud SDK (gcloud) installed and authenticated with your GCP project.
* A Strava developer account with an active application and the necessary API credentials.

**2. Setup:**

* Clone or download the source code from this repository.
* Configure your Google Cloud project and set up a Google Cloud Storage bucket to store the activity data.

**3. Configuration:**
* Update the necessary environment variables or configuration values in the code:
  * Provide your Strava API credentials (client ID, client secret, etc.) to authorize access to the Strava API.
  * Specify the details of your Google Cloud Storage bucket (bucket name, authentication credentials, etc.).

**4. Deployment:**
* Deploy the Google Cloud Function using the provided deployment command or script.
* Configure the scheduler to trigger the function execution every 30 minutes. You can utilize GCP's Cloud Scheduler service for this purpose.

**5. Testing and Monitoring:**

* Test the function by triggering it manually or waiting for the scheduler to execute it.
* Monitor the function's logs and Cloud Storage bucket to ensure the data is being fetched and stored correctly.

I want to push this change