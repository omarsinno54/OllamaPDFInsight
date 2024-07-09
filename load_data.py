
import sys
import os

root_dir = os.path.dirname(__file__)
data_dir = os.path.join(root_dir, 'beirut_data')

file_path = os.path.join(data_dir, os.listdir(data_dir)[0])

# Load documents
from langchain_community.document_loaders import PyMuPDFLoader
loader = PyMuPDFLoader(file_path)
documents = loader.load()

# Load documents into vector store
import weaviate
client = weaviate.connect_to_local()

import weaviate.classes as wvc
from weaviate.classes.config import Property, DataType

# If the collection exists, get it and don't create it
try:
    collection = client.collections.create(
        name = 'docs',
        properties = [
            Property(name='text', data_type = DataType.TEXT)
        ]
    )
except weaviate.exceptions.WeaviateQueryError:
    collection = client.collections.get(name='docs')
except weaviate.exceptions.UnexpectedStatusCodeError:
    collection = client.collections.get(name='docs')

import ollama

with collection.batch.dynamic() as batch:
    for i, d in enumerate(documents):
        response = ollama.embeddings(
            model = 'all-minilm',
            prompt = str(d)
        )

        batch.add_object(
            properties = {'text': str(d)},
            vector = response['embedding']
        )
