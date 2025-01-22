import json

import requests

from common.weaviate_client import client

data_response = requests.get(
    "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
)

data = json.loads(data_response.text)
questions = client.collections.get("Question")

# Insert objects in the collection
# with questions.batch.dynamic() as batch:
#     for d in data:
#         batch.add_object({"answer": d["Answer"], "question": d["Question"], "category": d["Category"]})

# Semantic search which is called `nearText` in Weaviate
response = questions.query.near_text(query="biology", limit=2)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()
