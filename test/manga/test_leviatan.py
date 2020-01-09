import re

from bs4 import BeautifulSoup
from pathlib import Path

if __name__ == '__main__':
    markup = Path("../resources/leviatan_item.html").read_text(encoding='utf-8')
    soup = BeautifulSoup(markup, 'html.parser')

    # print(soup.html.prettify())
    chapter_tags = soup.select('div.list div.flex > a:first-child')
    for chapter_tag in chapter_tags:
        title = chapter_tag.text.replace('\n', '')
        uid = re.split(r'[\s-]', title)[1]
        url = chapter_tag['href']
        print('({}): {} - {}'.format(uid, title, url))








