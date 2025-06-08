import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/dp/6581339083/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
myRequest = requests.get(url, headers=headers)
print(myRequest)

if myRequest.status_code == 200:
    soup = BeautifulSoup(myRequest.content, 'lxml')
    #text = soup.get_text()

    print(soup.prettify())

    #print(text)

    title = soup.find("span", 'productTitle')
    #titleForm = title.string.strip()

    print(title)

    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    if title is not None:
        print('Título do produto:', title.string)
    else:
        print('Amazon é chata pra crl')

# else:
#     print(f"Erro ao acessar a página: {myRequest.status_code}")





