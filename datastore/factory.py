from datastore.datastore import DataStore
import os


async def get_datastore() -> DataStore:
    datastore = os.environ.get("DATASTORE")
    assert datastore is not None

    match datastore:
        case "redis":
            from datastore.providers.redis_datastore import RedisDataStore

            return await RedisDataStore.init()
        case _:
            raise ValueError(f"Unsupported vector database: {datastore}")
