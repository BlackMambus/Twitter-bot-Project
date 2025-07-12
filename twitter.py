import tweepy

# Replace with your credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_SECRET = 'your_access_secret'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Post a tweet
def tweet(message):
    try:
        api.update_status(message)
        print("✅ Tweeted successfully!")
    except Exception as e:
        print("❌ Error tweeting:", e)

# Example usage
if __name__ == "__main__":
    tweet("Hello, world! This is my first bot tweet. 🤖 #Python #TwitterBot")

