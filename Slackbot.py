import requests
import sqlalchemy
import pandas as pd
import time

# wait for 20 second for slackbot post
time.sleep(20)

WEBHOOK_URL="https://hooks.slack.com/services/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"

# 1) connecting to postgres
pg = sqlalchemy.create_engine(
    'postgresql://postgres:1234@postgresdb:5432/posts',
    echo=True
    )
connection = pg.connect()

# 2) querying data from postgres
query = '''
    SELECT * FROM post_sentiment
    LIMIT 5
'''
df_posts = pd.read_sql(query,connection)

# 3) posting the data on slack

for i in range(5):
    row = df_posts.iloc[i]
    text = str(row['post_text'])
    sentiment = str(row['sentiment_score'])
    data={
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": text
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": sentiment
                }
            }
        ]
    }
    requests.post(url=WEBHOOK_URL, json=data)
    time.sleep(60)
