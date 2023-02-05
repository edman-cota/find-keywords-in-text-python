from requests_html import HTMLSession
from rake_nltk import Rake

local_text = 'Buenos dias, me estoy cominicando con ustedes el día de hoy respecto a los malos servicios que he tenido las últimas ocaciones que he ido a la tienda. Ustedes son una mierda de empresa.'

def extract_text_from_web():
    s = HTMLSession()
    url = 'https://www.musicradar.com/reviews/tech/akg-c214-172209'
    response = s.get(url)
    return response.html.find('div#article-body', first=True).text

r = Rake()
r.extract_keywords_from_text(extract_text_from_web())
# r.extract_keywords_from_text(local_text)
print(r.get_ranked_phrases_with_scores())