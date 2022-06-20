import asyncio
import logging

import restweetution.config as config
from restweetution.collectors.async_client import AsyncClient
from restweetution.collectors.async_streamer import AsyncStreamer
from restweetution.models.examples_config import ALL_CONFIG
from restweetution.storage.async_storage_manager import AsyncStorageManager
from restweetution.storage.elastic_storage.elastic_storage import ElasticTweetStorage

logging.basicConfig()
logging.root.setLevel(logging.INFO)

config = config.get_config()

esc = config['elastic_config']
es_storage = ElasticTweetStorage(name=esc['name'],
                                 es_url=esc['url'],
                                 es_user=esc['user'],
                                 es_pwd=esc['pwd'])
# es_storage = ElasticTweetStorage(name='Localhost_Elastic',
#                                  es_config={
#                                      "url": "http://localhost:9200",
#                                      "user": "",
#                                      "pwd": ""}
#                                  )
config1 = {
    'token': config['token'],
    'verbose': False,
    'tweet_config': ALL_CONFIG,
    'average_hash': True
}


async def launch():
    client = AsyncClient(config1['token'])
    storage_manager = AsyncStorageManager()
    storage_manager.add_storage(es_storage, ['Rule'])
    streamer = AsyncStreamer(client, storage_manager)
    streamer.set_query_params(config1['tweet_config'])
    await streamer.add_stream_rules({'Rule': '(johnny) OR (depp)'})

    asyncio.create_task(streamer.collect())

loop = asyncio.get_event_loop()
loop.create_task(launch())
loop.run_forever()
