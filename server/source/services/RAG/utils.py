# import pymongo

# def get_mongo_client(mongo_uri):
#   """Establish connection to the MongoDB."""

#   try:
#     client = pymongo.MongoClient(mongo_uri, appname="devrel.content.python")
#     print("Connection to MongoDB successful")
#     return client
#   except pymongo.errors.ConnectionFailure as e:
#     print(f"Connection failed: {e}")
#     return None

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("thenlper/gte-large")

def get_embedding(text: str) -> list[float]:
  if not text.strip():
    print('Attempted to get embedding for empty text.')

  embeddings = model.encode(text)
  return embeddings.tolist()


def message_prompt(query, source_information):
  combined_information = f"Query: {query}\nContinue to answer the query by using the Search Result: {source_information}."

  messages = [
    {
        'role': 'system',
        'content': 'You are an expert recruitment assistant that provides insights and recommendations based on the combined information from the user\'s CV, job description, and additional data retrieved from a vast collection of job information. Your responses should be concise, relevant, and directly address the user\'s query.'
    },
    {
        'role': 'user',
        'content': f'{combined_information}'
    }
  ]

  return messages
