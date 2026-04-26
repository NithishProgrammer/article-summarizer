from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

app = FastAPI()

@app.post('/summarise')
def summarize_aticle(url : str):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text , 'html.parser')
    text = " ".join([p.text for p in soup.find_all('p')])

    parser = PlaintextParser.from_string(text , Tokenizer('english'))
    summarizer = LuhnSummarizer()

    summary = summarizer(parser.document , 10)

    return {'Url' : url  ,  'summary' : [str(sentence) for sentence in summary]}

