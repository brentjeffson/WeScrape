from os import path

LOCATOR_PATH = path.join(path.dirname(__file__), 'locators.json')

class Sources:
    MANGAKAKALOT = 'https://mangakakalot.com'
    LEVIATANSCANS = 'https://leviatanscans.com'


PATTERN = 0
SELECTOR = 1


class Pattern:
    CHAPTER_UID = 0
    CHAPTER_URL = 1
    CHAPTER_TITLE = 2


class Selector:
    MANGA_URL = 0
    MANGA_TITLE = 1
    MANGA_DESCRIPTION = 2
    CHAPTER_ITEM = 3
    CHAPTER_IMAGE = 4
    SEARCHED_MANGA = 5


APIS = {
    Sources.MANGAKAKALOT: '/search',
    Sources.LEVIATANSCANS: ''
}