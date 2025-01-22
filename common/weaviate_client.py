import weaviate
from weaviate.classes.init import Auth

import config

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=config.WCD_URL, auth_credentials=Auth.api_key(config.WCD_API_KEY)
)

client.close()
