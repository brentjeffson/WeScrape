import json
import re
from pathlib import Path
from os import path

from bs4 import BeautifulSoup

from src.main.manga.consts import Pattern, LOCATOR_PATH, Selector, SELECTOR


class Chapter:
    _uid = ''
    _url = ''
    _title = ''
    _images = ''

    def __init__(self, uid, url, title, images=None):
        self.uid = uid
        self.url = url
        self.title = title
        self.images = images

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, images):
        self._images = images

    def __str__(self):
        return '({0}): {1} - {2}'.format(self.uid, self.title, self.url)


class Manga:
    _chapters = []
    _source = ''
    _locator = {}

    def __init__(self, markup, source):
        self.source = source
        locators = Path(path.join(path.dirname(__file__), LOCATOR_PATH))

        if locators.exists() and len(locators.read_text()) > 0:
            self.locator = json.loads(locators.read_text(encoding='utf-8'))[self.source]
            selectors = self.locator[SELECTOR]
            self.find_chapters(markup, selectors)

    def find_chapters(self, markup, selectors):
        soup = BeautifulSoup(markup, 'html.parser')

        chapter_tags = soup.select(selectors[Selector.CHAPTER_ITEM])
        temp_chapter = []
        for chapter_tag in chapter_tags:
            url = chapter_tag['href']
            title = chapter_tag.text.replace('\n', '')
            uid = re.split(r'[\s-]', title)[1]

            print(Chapter(uid, url, title))
            temp_chapter.append(Chapter(uid, url, title))

        self.chapters = temp_chapter
        return self._chapters

    def find_images(self, markup, chapter):
        soup = BeautifulSoup(markup, 'html.parser')
        selectors = self.locator[SELECTOR]

        image_tags = soup.select(selectors[4])
        temp_images = []
        for image_tag in image_tags:
            href = image_tag['src']
            temp_images.append(href)

        chapter.images = temp_images
        self.update(chapter, chapter)
        return chapter

    def update(self, old_chapter, new_chapter):
        index_to_replace = self.chapters.index(old_chapter)
        self.chapters[index_to_replace] = new_chapter

    @staticmethod
    def supported():
        locators = Path(path.join(path.dirname(__file__), LOCATOR_PATH))
        locators = json.loads(locators.read_text(encoding='utf-8'))
        for value in locators:
            print(value)

    @property
    def locator(self):
        return self._locator

    @locator.setter
    def locator(self, locator):
        self._locator = locator

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source

    @property
    def size(self):
        return len(self.chapters)

    @property
    def chapters(self):
        return self._chapters

    @chapters.setter
    def chapters(self, chapters):
        self._chapters = chapters
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








