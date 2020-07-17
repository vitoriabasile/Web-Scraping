import requests 
import json
from bs4 import BeautifulSoup

res = requests.get("https://digitalinnovation.one/faq")
res.encouding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

# links = soup.find(class_="pagination").find_all('a')
# all_pages = []
# for link in links:
#  page = resquests.get(link.get('href'))
#  all_pages.append(BeautifulSoup(page.text, 'html.parser'))

posts = soup.find_all(class_="card")

all_posts = []
# for posts in all_pages:
for post in posts:
    title = post.find('a').text
    content = post.find(class_="card-body").text
    all_posts.append({
        'title':title, 
        'content':content
    })

    print(all_posts)
    with open('posts.json', 'w') as json_file:
        json.dump(all_posts, json_file, indent=3, ensure_ascii=False)

