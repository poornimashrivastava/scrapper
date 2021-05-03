# web scrapping : finding snippets about items on google search
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def googleQuery(query) :
    query = query.replace(' ', '+')

    try :
        # url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'

        url = f"https://google.com/search?q={query}"

        getURL = requests.get(url, headers=headers)
        if getURL.status_code == 200 :
            # print(getURL.status_code)
            soup = BeautifulSoup(getURL.text, "html.parser")

    except :
        print("Couldn't establish connection!")

    try :
        try :
            result = soup.select('.RqBzHd')[0].getText().strip()

        except :
            try :
                head = soup.select('.AZCkJd')[0].getText().strip()

                try :
                    result = soup.select('.e24Kjd')[0].getText().strip()
                
                except :
                    result = ""
                result = f'{head}\n{result}'
            
            except :
                try :
                    result = soup.select('.hgKElc')[0].getText().strip()
                except :
                    result = soup.select('.kno-rdesc span')[0].getText().strip()
    except :
        result = "Not found!"
    return result

res = googleQuery(str(input("Enter a query: ")))
print(res)


