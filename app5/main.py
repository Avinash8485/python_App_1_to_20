import requests
from email import send_email

api_key ='0d4bf89d51af4bbaacf4cefeba2d5e4f'
url ="https://newsapi.org/v2/everything?q=tesla&from=2025-02-08&sortBy=publishedAt&apiKey=0d4bf89d51af4bbaacf4cefeba2d5e4f&language=en"

req = requests.get(url)
context = req.json()

body =""

for article in context['articles'][:20]:
      body = "Subject : Today's News "+'\n'+body + article['title'] +'\n' + article['description'] \
            +'\n'+ article['url']+2*'\n'



body = body.encode("utf-8")
send_email(body)

