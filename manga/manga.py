import re

import requests
from bs4 import BeautifulSoup
from manga.constants import Selector, APIS, SELECTORS, REQUIRED_PARAMETERS, PATTERNS, Pattern


class Chapter:

    def __init__(self, uid, url, title, images=None):
        self._uid = uid
        self._url = url
        self._title = title
        self._images = images

    def __str__(self):
        return '({0}): {1} - {2}'.format(self.uid, self.title, self.url)

    @property
    def uid(self):
        return self._uid

    @property
    def url(self):
        return self._url

    @property
    def title(self):
        return self._title

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, images):
        self._images = images

    @property
    def size(self):
        return len(self.images)


class Manga:

    def __init__(self, url, image_url, title, chapters=None):
        self._url = url
        self._image_url = image_url
        self._title = title
        self._chapters = [] if chapters is None else chapters

    def __str__(self):
        return f"{self.title}({self.size})"

    @property
    def url(self):
        return self._url

    @property
    def image_url(self):
        return self._image_url

    @property
    def title(self):
        return self._title

    @property
    def chapters(self):
        return self._chapters

    @chapters.setter
    def chapters(self, chapters):
        self._chapters = chapters

    @property
    def size(self):
        return len(self.chapters)


class MangaScraper:

    def __init__(self, markup, source):
        self._manga = None
        self._source = source
        selectors = SELECTORS[source] if source in SELECTORS else {}
        patterns = PATTERNS[source] if source in PATTERNS else {}

        self._manga = self.find_details(markup, source, SELECTORS, PATTERNS)
        self.find_chapters(markup, selectors)

    def find_details(self, markup, source, selectors, patterns):
        selectors = selectors[source] if source in SELECTORS else {}
        patterns = patterns[source] if source in PATTERNS else {}
        soup = BeautifulSoup(markup, "html.parser")

        url = soup.select(selectors[Selector.MANGA_URL])[0]["href"]
        title = soup.select(selectors[Selector.MANGA_TITLE])[0].text.replace("\n", "")
        image_url_tag = soup.select(selectors[Selector.MANGA_IMAGE_URL])[0]
        image_url = ""
        if image_url_tag.name == 'a':
            r = re.search(patterns[Pattern.MANGA_IMAGE_URL], str(image_url_tag))
            image_url = r.groups()[0]
            if source not in image_url:
                if not image_url[0] == '/':
                    image_url = '/' + image_url
                image_url = source + image_url

        elif image_url_tag == 'img':
            image_url = image_url_tag['src']

        return Manga(url, image_url, title)

    def find_chapters(self, markup, selectors):
        soup = BeautifulSoup(markup, 'html.parser')

        chapter_tags = soup.select(selectors[Selector.CHAPTER_URL])
        temp_chapters = []
        for chapter_tag in chapter_tags:
            url = chapter_tag['href']
            title = chapter_tag.text.replace('\n', '')
            uid = re.split(r'[\s-]', title)[1]

            temp_chapters.append(Chapter(uid, url, title))

        self._manga.chapters = temp_chapters
        return temp_chapters

    def find_images(self, markup, chapter):
        soup = BeautifulSoup(markup, 'html.parser')
        selectors = SELECTORS[self.source]

        image_tags = soup.select(selectors[Selector.CHAPTER_IMAGES])
        temp_images = []
        for image_tag in image_tags:
            href = image_tag['src']
            temp_images.append(href)

        chapter.images = temp_images
        self.update(chapter, chapter)
        return chapter

    def update(self, old_chapter, new_chapter):
        index_to_replace = self._manga.chapters.index(old_chapter)
        self._manga.chapters[index_to_replace] = new_chapter

    @staticmethod
    def search(keyword, source, as_payload=False, headers=None):
        api = source + APIS[source]

        resp = None
        if source in REQUIRED_PARAMETERS:
            params = {REQUIRED_PARAMETERS[source][0]: keyword}
            resp = requests.get(api, params=params, headers=headers)
        else:
            api += '/' + keyword
            resp = requests.get(api, headers=headers)

        if not resp.ok:
            return None
        markup = resp.text

        content_type = resp.headers['content-type']

        selectors = SELECTORS[source]

        tmp_mangas = []
        if 'text/html' in content_type:
            soup = BeautifulSoup(markup, 'html.parser')
            searched_tags = soup.select(selectors[Selector.SEARCHED_URL])

            for searched_tag in searched_tags:
                url = searched_tag['href'].strip()
                title = searched_tag.text.replace('\n', '').strip()
                tmp_mangas.append({'url': url, 'title': title})
        elif 'application/json' in content_type:
            pass

        return tmp_mangas

    @staticmethod
    def supported():
        for value in SELECTORS:
            print(value)

    @property
    def locator(self):
        return self._locator

    @property
    def source(self):
        return self._source

    @property
    def size(self):
        return len(self.manga.size)

    @property
    def manga(self):
        return self._manga

# class Manga:
#     _chapters = []
#
#     def __init__(self, docstring, source):
#         locator = {}
#         with open(LOCATOR_PATH, encoding='utf-8') as f:
#             locator = json.loads(f.read())
#
#         if len(locator) > 0:
#             pattern = locator[source]['patterns']
#             self.find_chapters(docstring, pattern)
#
#     def find_chapters(self, str, patterns):
#         """find all available chapters in the given str, if no chapters are available returns None"""
#         # isolate the chapters
#         print('Isolating Chapters using -> {0}'.format(patterns[Pattern.CHAPTER_CONTAINER]))
#         pattern = re.compile(patterns[Pattern.CHAPTER_CONTAINER], re.DOTALL)
#         searched = re.search(pattern, str)
#
#         if searched is None:
#             return None
#         pos = searched.span()
#         isolated_str = str[pos[0]:pos[1]]
#
#         # find all instances of chapters
#         pattern = re.compile(patterns[Pattern.CHAPTER_ITEM])
#         chapter_items = re.findall(pattern, isolated_str)
#         if not len(chapter_items) > 0:
#             return None
#
#         temp_chapters = []
#         for chapter_item in chapter_items:
#             searched_uid = re.search(patterns[Pattern.CHAPTER_UID], chapter_item)
#             searched_url = re.search(patterns[Pattern.CHAPTER_URL], chapter_item)
#             searched_title = re.search(patterns[Pattern.CHAPTER_TITLE], chapter_item)
#
#             uid = searched_uid.groups()[0] if len(searched_uid.groups()) > 0 else ''
#             url = searched_url.groups()[0] if len(searched_url.groups()) > 0 else ''
#             title = searched_title.groups()[0] if len(searched_title.groups()) > 0 else ''
#
#             temp_chapters.append(Chapter(uid, url, title))
#         self.chapters = temp_chapters
#         return temp_chapters
#
#     @property
#     def size(self):
#         """returns the number of chapters available in the manga"""
#         return len(self.chapters)
#
#     @property
#     def chapters(self):
#         """returns all available chapters in the manga"""
#         return self._chapters
#
#     @chapters.setter
#     def chapters(self, chapters):
#         self._chapters = chapters
#
#     def replace(self, old_chapter, new_chapter):
#         """replaces current chapter with the new one"""
#         index_to_replace = self._chapters.index(old_chapter)
#         self._chapters[index_to_replace] = new_chapter








