import ollama

prompt = "What is the Lebanese national history?"
response = ollama.embeddings(
    model = 'all-minilm',
    prompt = prompt
)

import weaviate

client = weaviate.connect_to_local()
collection = client.collections.get(name='docs')

results = collection.query.near_vector(
    near_vector = response['embedding'],
    limit = 1
)

data = results.objects[0].properties['text']

prompt_template = f'Using this data: {data}. Repond to this prompt: {prompt}.'

output = ollama.generate(
    model = 'mistral',
    prompt = prompt_template
)

print(output['response'])