import base64
from pyserini.search import SimpleSearcher
import json
import ollama


def search_document_query(query):
  searcher = SimpleSearcher.from_prebuilt_index('msmarco-passage')
  hits = searcher.search(query, 10)
  return [hit.lucene_document.get('raw') for hit in hits]

# return 10 documents from the query
def searching(query):
  print("queryyyyyyyy", query)
  passages = search_document_query(query)
  document = []
  for passage_str in passages:
      passage_dict = json.loads(passage_str)
      content = passage_dict['contents']
      document.append(content)
  return document


def create_prompt(queryText, passages):
  print("creating prompt....")
  if queryText == "":
      return ""
  prompt = f"""
  Given the query below and 10 irrrelevant passages retrieved by a search engine,
  Please expand the query to retrieve more relevant documents.
  Don't explain. Only mention the expanded query directly, without anything preceding and following it.

  Query: {queryText}
  Passage1: {passages[0]}
  Passage2: {passages[1]}
  Passage3: {passages[2]}
  Passage4: {passages[3]}
  Passage5: {passages[4]}
  Passage6: {passages[5]}
  Passage7: {passages[6]}
  Passage8: {passages[7]}
  Passage9: {passages[8]}
  Passage10: {passages[9]}

  """
  print("prompt:", prompt)
  return prompt

# return expanded query
def get_expanded_query(prompt):
  if prompt == "":
      return ""
  try:
      ollama.pull('llama3')
      response = ollama.chat(
          model='llama3',
          messages = [{
              'role': 'user',
              'content': prompt,
          }]
      )
      return response['message']['content']
  except Exception as e:
      print(f"Failed to get expanded query for prompt: {prompt}. Error: {e}")
      return ''




