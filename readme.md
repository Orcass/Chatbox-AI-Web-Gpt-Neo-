fitur website ini di rancang dengan memggunakan model gtp neo dari transformer yang tersedia darui huging face transformers.
project ini nantinya akan saya kembangkan lebih dalam lagi karena saya ingin membuat project untuk protofolio saya.

Inslasi: 1%

resoursce:
 - https://huggingface.co/EleutherAI/gpt-j-6b
 - libary/doc: https://huggingface.co/docs/transformers/model_doc/gpt_neo

 progress: 
 - build code to api
 - mennggunakan rendering web sebagai text respnse dari bot terserbut.
 - masih menggunakan lokal yang bekerja pada gpu dan hosting lainya.

 kekurangan:
  - masih menggunakan lokal komputer/server
  - belum menggunakan model dari ip
  - website kurang menarik dan responsif.

yang harus saya kerjakan:
- pernqambahan protofolio
- penambahan button.
- rubah warna website menjadi elegant.

kode cadangan untuk menggunakan api dari mode gpt neo:
code:
import requests
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
headers = {"Authorization": "Bearer YOUR_HUGGING_FACE_API_KEY"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "inputs": "Hello, how are you?",
    "parameters": {"max_new_tokens": 150}
})
print(response)