from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

items = [
     "hotcake-2pcs",
     "hotcakes-3pcs",
     "deluxe-breakfast",
     "hotcakes-with-sausage-hash-browns",
     "jumbo-breakfast",
     "grilled-chicken-twisty-pasta-original",
     "ham-n-egg-twisty-pasta-original",
     "sausage-n-egg-twisty-pasta-original",
     "grilled-chicken-twisty-pasta-tonkotsu",
     "ham-n-egg-twisty-pasta-tonkotsu",
     "sausage-n-egg-twisty-pasta-tonkotsu"
]

nutritional_values = []

for item in items:
    url = f"https://mcdonalds.com.hk/en/nutrition/{item}/"
    r = session.get(url)
    r.html.render(wait=4, sleep=4, keep_page=True, scrolldown=1)
    data_list = []
    for i in r.html.find('.flex_item_3'):
        data_list.append(i.text)
    nutritional_values.append(data_list)

print(nutritional_values)