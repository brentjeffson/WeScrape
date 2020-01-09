from os import path


class Sources:
    MANGAKAKALOT = 'https://mangakakalot.com'
    LEVIATANSCANS = 'https://leviatanscans.com'


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


PATTERN = 0
SELECTOR = 1

SELECTORS = {
    Sources.MANGAKAKALOT: [
        "link[rel=\"alternate\"]",
        "li.manga-info-text > li > h1",
        "div#noidungm",
        "div.chapter-list > div.row > span > a",
        "div.vung-doc img",
        "h3.story_name > a"
    ],
    Sources.LEVIATANSCANS: [
        "a.media-content",
        "div.d-flex > div.heading > h5",
        "div.row > div:nth-child(2)",
        "div.list div.flex > a:first-child",
        "div.vung-doc img",
        "div.media.media-comic-card + div.list-content a.list-title"
    ]
}

REQUIRED_PARAMETERS = {
    Sources.LEVIATANSCANS: ['query']
}

APIS = {
    Sources.MANGAKAKALOT: '/search',
    Sources.LEVIATANSCANS: '/comics'
}

if __name__ == '__main__':
    print(Sources.LEVIATANSCANS in REQUIRED_PARAMETERS)