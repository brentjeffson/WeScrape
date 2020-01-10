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
    MANGA_IMAGE_URL = -1
    MANGA_TITLE = 1
    MANGA_DESCRIPTION = 2

    CHAPTER_URL = 3
    CHAPTER_TITLE = -1
    CHAPTER_IMAGES = 4

    SEARCHED_URL = 5
    SEARCHED_IMAGE_URL = 6
    SEARCHED_TITLE = 7


SELECTORS = {
    Sources.MANGAKAKALOT: {
        Selector.MANGA_URL: "link[rel=\"alternate\"]",
        Selector.MANGA_IMAGE_URL: '',
        Selector.MANGA_TITLE: "li.manga-info-text > li > h1",
        Selector.MANGA_DESCRIPTION: "div#noidungm",
        Selector.CHAPTER_URL: "div.chapter-list > div.row > span > a",
        Selector.CHAPTER_IMAGES: "div.vung-doc img",
        Selector.SEARCHED_URL: "h3.story_name > a",
    },
    Sources.LEVIATANSCANS: {
        Selector.MANGA_URL: "a.media-content",
        Selector.MANGA_IMAGE_URL: '',
        Selector.MANGA_TITLE: "div.d-flex > div.heading > h5",
        Selector.MANGA_DESCRIPTION: "div.row > div:nth-child(2)",
        Selector.CHAPTER_URL: "div.list div.flex > a:first-child",
        Selector.CHAPTER_IMAGES: "div.vung-doc img",
        Selector.SEARCHED_URL: "div.media.media-comic-card + div.list-content a.list-title",
    },
}

REQUIRED_PARAMETERS = {
    Sources.LEVIATANSCANS: ['query']
}

APIS = {
    Sources.MANGAKAKALOT: '/search',
    Sources.LEVIATANSCANS: '/comics'
}