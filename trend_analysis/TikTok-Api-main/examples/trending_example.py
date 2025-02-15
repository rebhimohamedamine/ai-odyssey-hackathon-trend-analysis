from TikTokApi import TikTokApi
import asyncio
import os
import schedule
import time
from pymongo import MongoClient

# Get ms_token
ms_token = os.environ.get("ms_token")  # Replace with actual ms_token if needed

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["tiktok_data"]
collection = db["trending_videos"]

async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=5, browser="webkit")

        trending_data = []

        async for video in api.trending.videos(count=30):
            video_dict = video.as_dict  # ✅ FIX: Remove ()
            trending_data.append(video_dict)

        if trending_data:
            collection.insert_many(trending_data)
            print(f"✅ {len(trending_data)} trending videos saved to MongoDB")
        else:
            print("⚠️ No data collected")

def run_scraper():
    asyncio.run(trending_videos())

# Schedule the scraper to run every 5 minutes
schedule.every(10).minutes.do(run_scraper)

print("🚀 TikTok Scraper is running every 10 minutes...")

while True:
    schedule.run_pending()
    time.sleep(1)  # Prevent CPU overuse

