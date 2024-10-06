import requests
from bs4 import BeautifulSoup

def get_article_info(url: str) -> dict:
  response = requests.get(url)
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')

      title = soup.find('h1').text.strip()

      date = soup.find('div', class_='update-publish-time')
      loc_info = date.span.text.strip()
      article_date = loc_info.split('-')[1].strip()
      article_location = loc_info.split('-')[-1].strip()

      article_body = soup.find('div', class_='articlebodycontent')
      paragraphs = article_body.find_all('p')
      article_text = ''.join([para.text.strip() for para in paragraphs if para.get('class') is None])

      category = soup.find('li', class_='breadcrumb-item active')

      top_pic = soup.find('div', class_='article-picture top-pic')
      image = None
      if top_pic:
        picture_tag = top_pic.find('picture')
        image = picture_tag.find('source').get('srcset')

      res = {
          "url": url,
          "image": image,
          "category": category.text.strip(),
          "date": article_date,
          "headline": title,
          "location": article_location,
          "content": article_text
      }
      return res
  else:
      print(f"Failed to retrieve the webpage. Status code: {response.status_code}")