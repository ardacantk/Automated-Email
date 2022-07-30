# Gmail: pythonmail05@gmail.com//password: gazi4863 & efqdvhiwylxrcvnq.
import yagmail
import pandas as pd
from News import NewFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    news_feed = NewFeed(interest=row["interest"],
                        from_date=yesterday,
                        to_date=today,
                        language="en")
    email = yagmail.SMTP(user="pythonmail05@gmail.com", password="efqdvhiwylxrcvnq")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']} \n See what's on about {row['interest']} today.\n {news_feed.get()}\nACTK")


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 42:
        df = pd.read_excel("people.xlsx")

        for index, row in df.iterrows():
            send_email()
            time.sleep(60)

print(df)
