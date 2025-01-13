from .utils import get_embedding

def vector_search(user_query, collection):
    """
    Perform a vector search in the MongoDB collection based on the user query.

    Args:
        user_query (str): The user's query string.
        collection (MongoCollection): The MongoDB collection to search.

    Returns:
        list: A list of matching documents.
    """

    # Generate embedding for the user query
    query_embedding = get_embedding(user_query)

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    # Define the vector search pipeline
    vector_search_stage = {
        "$vectorSearch": {
            "index": "vector_index",
            "queryVector": query_embedding,
            "path": "Description_embedding",
            "numCandidates": 150,  # Number of candidate matches to consider
            "limit": 4  # Return top 4 matches
        }
    }

    # Unset stage
    unset_stage = {
        "$unset": "Description_embedding"  # Exclude the 'Description_embedding' field from the results
    }

    # Project stage
    project_stage = {
        "$project": {
            "_id": 0,  # Exclude the '_id' field
            "score": {  # Include the search score
                "$meta": "vectorSearchScore"
            },
            "title": 1,
            "Description": 1,
            "URL": 1

        }
    }

    # Construct the pipeline
    pipeline = [vector_search_stage, unset_stage, project_stage]

    # Execute the search
    results = collection.aggregate(pipeline)
    output = []
    for document in results:
        output.append(document)
    return output
    #return list(results)