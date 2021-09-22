import json
import logging
from restweetution.collectors import Streamer

if __name__ == "__main__":
    logging.basicConfig()
    logging.root.setLevel(logging.INFO)
    with open(r"C:\Users\Orion\Documents\Projets\CERES\credentials_pro.json", "r") as f:
        token = json.load(f).get('token')
    config = {
        'token': token,
        'tweet_storage': {
            "root_directory": r"C:\Users\Orion\Documents\OutputTweets",
            "host": "localhost",
            "user": "test",
            "password": "lol",
            "max_size": 1000
        },
        'media_storage': {
            "root_directory": r"C:\Users\Orion\Documents\OutputTweets\media",
            "max_size": 1000
        },
        'verbose': True
    }
    s = Streamer(config)
    s.collect()