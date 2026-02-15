# Authentication

## Overview
The AT100DaysChallenge project uses API key authentication to securely communicate with external AI and vector database services.

Authentication is currently implemented at the service-to-service level.

## External Service Authentication
The application authenticates with:

- Cohere — for generating text embeddings

- Pinecone — for storing and querying vector embeddings

Authentication is performed using API keys stored in Django settings.

## Configuration
API keys must be defined as environment variables:
<pre>
COHERE_API_KEY=your_cohere_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_region
</pre>


## How Authentication Works in Code
1. Cohere Client Initialization

<pre>
def get_cohere_client():
    return cohere.Client(settings.COHERE_API_KEY)
</pre>

The API key is passed directly to the Cohere client during initialization.

2. Pinecone Client Initialization
<pre>
def get_pinecone_client():
    return Pinecone(api_key=settings.PINECONE_API_KEY)
</pre>

The Pinecone API key is used to authenticate requests to the vector database.