from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='dummy_data.csv')

docs=loader.load()

print(docs[2].page_content)