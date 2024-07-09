# OllamaPDFInsight

OllamaPDFInsight is a small RAG (Retrieval-Augmented Generation) system that leverages Ollama to create embeddings from a PDF file, stores these embeddings in a Weaviate vector store, and uses Ollama to answer questions regarding the PDF content.

## Steps

- Use LangChain document loader to turn the PDF into a set of documents.
- Create a collection from these documents in the Weaviate vector store.
- Use Ollama to generate embeddings from the documents, and store the embeddings in the collection.
- Query and retrieve information from the PDF using Ollama.


## Run & Modify
1. Create a virtual environment:
```sh
pyenv install 3.8.10
pyenv virtualenv 3.8.10 ollama-pdf-insight-env
pyenv activate ollama-pdf-insight-env
```
2. Once the virtual environment is activated, install the requirements from the `requirements.txt` file.
```sh
pip install -r requirements.txt
```
3. Clone the repository:

```sh
git clone https://github.com/yourusername/OllamaPDFInsight.git
cd OllamaPDFInsight
```
4. Prepare the data and the weaviate vector store.
```sh
python load_data.py
```
5. Prepare the template, llm, and run the prompt.
```sh
python retrieve_context.py
```


## References
I essentially followed the steps in [this article](https://weaviate.io/blog/local-rag-with-ollama-and-weaviate) and added my own touch to it.