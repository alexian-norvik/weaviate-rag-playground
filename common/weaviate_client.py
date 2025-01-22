import weaviate
from weaviate.classes.init import Auth

import config

# Connect to the cluster
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=config.WCD_URL,
    auth_credentials=Auth.api_key(config.WCD_API_KEY),
    headers={"X-OpenAI-Api-Key": config.OPENAI_API_KEY},
)

# Create collection
# questions = client.collections.create(
#     name="Question",
#     vectorizer_config=Configure.Vectorizer.text2vec_openai(),
#     generative_config=Configure.Generative.openai(),
# )
