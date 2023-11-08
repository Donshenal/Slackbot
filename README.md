# Slackbot for posting data from PostgreSQL

This Python project is designed to periodically fetch data from a PostgreSQL database and post it on a Slack channel using Slack's webhook integration.

## Overview

The `Slackbot.py` script fetches data from a PostgreSQL database table `post_sentiment` and posts information on a Slack channel. It involves the following steps:

1. **Wait Duration:** The script waits for 20 seconds to give Slackbot time to post messages.
2. **Database Connection:** Establishes a connection to a PostgreSQL database using SQLAlchemy.
3. **Querying Data:** Runs a SQL query to retrieve the top 5 rows from the `post_sentiment` table.
4. **Posting to Slack:** For each row of the fetched data, the script constructs a Slack message consisting of post text and sentiment score, formatting it using Slack's Block Kit. This data is then posted on a specified Slack channel using a webhook.
5. **Time Interval:** It pauses for 60 seconds before posting each subsequent message.

## Usage

The script `Slackbot.py` and the `Dockerfile` can be used to deploy the Slackbot. To run the Slackbot, ensure you have the necessary dependencies and then execute the following:

1. Build the Docker container:

docker build -t slackbot .

2. Run the Docker container:

docker run slackbot

## Project Structure

- `Slackbot.py`: Python script for fetching data from PostgreSQL and posting it on Slack.
- `Dockerfile`: Dockerfile specifying the environment and setup for the Slackbot.

## Note

- Update the `WEBHOOK_URL` in the `Slackbot.py` script with your Slack webhook URL.
- Ensure your PostgreSQL connection details are correctly set in the Python script.
- Adjust the time intervals and data fetching logic as required for your use case.

Feel free to modify and adapt the code to suit your specific requirements.
