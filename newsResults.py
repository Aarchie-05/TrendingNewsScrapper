from GoogleNews import GoogleNews
news = GoogleNews(period='1d')
news.search("India")
result = news.result()
import pandas as pd
data = pd.DataFrame(result)
print(data.columns)
for i in result:
    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read Full News : ", i["link"])