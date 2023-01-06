from restweetution.data_view.row_view import RowView
from restweetution.data_view.view_exporter import ViewExporter
from restweetution.media_downloader import MediaDownloader
from restweetution.models.config.system_config import SystemConfig
from restweetution.storages.elastic_storage.elastic_storage import ElasticStorage
from restweetution.storages.postgres_jsonb_storage.postgres_jsonb_storage import PostgresJSONBStorage


class StorageInstance:
    def __init__(self, config: SystemConfig):
        self.storage = PostgresJSONBStorage(config.postgres_url)
        if config.media_dir_path:
            self.media_downloader = MediaDownloader(root=config.media_dir_path, storage=self.storage)
        if config.elastic:
            self.elastic = ElasticStorage('elastic', **config.elastic.dict())
            self.elastic_dashboard = ViewExporter(view=RowView(), exporter=self.elastic)
