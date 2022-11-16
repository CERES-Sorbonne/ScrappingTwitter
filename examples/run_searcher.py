import asyncio
import logging
import os
from datetime import datetime

import restweetution.config_loader as config
from restweetution.data_view.elastic_dashboard import ElasticDashboard

logging.basicConfig()
logging.root.setLevel(logging.INFO)

async def launch():
    main_conf = config.get_config_from_file(os.getenv('CONFIG'))
    searcher = main_conf.searcher
    view = ElasticDashboard(main_conf.storage_manager.main_storage, main_conf.storages['ceres_elastic'], 'renaud')
    await searcher.collect(rule=main_conf.searcher_rule, count_tweets=False, fields=main_conf.query_fields, recent=False, start_time=datetime(2017, 11, 10, 16, 44, 20, 323095), end_time=datetime(2022, 4, 1), max_results=100)

try:
    asyncio.run(launch())
except KeyboardInterrupt as e:
    pass
