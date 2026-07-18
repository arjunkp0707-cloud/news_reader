import requests 
query =input("what type of news are you interested today?")
api = "980f7c4380514adaba5d54da8361a597"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-07-15&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)
data = r.json()
articles = data["articles"]
for index ,article in enumerate  (articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")


   