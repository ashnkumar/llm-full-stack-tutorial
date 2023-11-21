import requests
import json
import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
openai_client = OpenAI(api_key=OPENAI_API_KEY)

OPENAI_EMBEDDING_MODEL = 'text-embedding-ada-002'
PROMPT_LIMIT = 3750
CHATGPT_MODEL = 'gpt-4-1106-preview'

def get_embedding(chunk):
  url = 'https://api.openai.com/v1/embeddings'
  headers = {
      'content-type': 'application/json; charset=utf-8',
      'Authorization': f"Bearer {OPENAI_API_KEY}"            
  }
  data = {
      'model': OPENAI_EMBEDDING_MODEL,
      'input': chunk
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))  
  response_json = response.json()
  embedding = response_json["data"][0]["embedding"]
  # response = openai_client.embeddings.create(
  #     input=chunk, model=OPENAI_EMBEDDING_MODEL)
  # embedding = response.data[0].embedding
  return embedding

def get_llm_answer(prompt):
  messages = [{"role": "system", "content": "You are a helpful assistant."}]
  messages.append({"role": "user", "content": prompt})

  url = 'https://api.openai.com/v1/chat/completions'
  headers = {
      'content-type': 'application/json; charset=utf-8',
      'Authorization': f"Bearer {OPENAI_API_KEY}"            
  }
  data = {
      'model': CHATGPT_MODEL,
      'messages': messages,
      'temperature': 1, 
      'max_tokens': 1000
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))
  response_json = response.json()
  completion = response_json["choices"][0]["message"]["content"]
  return completion