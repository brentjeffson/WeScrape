from os import path


class Sources:
    MANGAKAKALOT = 'https://mangakakalot.com'
    LEVIATANSCANS = 'https://leviatanscans.com'


class Pattern:
    MANGA_IMAGE_URL = 1

    CHAPTER_UID = 0
    CHAPTER_URL = 1
    CHAPTER_TITLE = 2


class Selector:
    MANGA_URL = 0
    MANGA_IMAGE_URL = 1
    MANGA_TITLE = 2
    MANGA_DESCRIPTION = 3

    CHAPTER_URL = 4
    CHAPTER_TITLE = 5
    CHAPTER_IMAGES = 6

    SEARCHED_URL = 7
    SEARCHED_IMAGE_URL = 8
    SEARCHED_TITLE = 9


PATTERNS = {
    Sources.LEVIATANSCANS: {
        Pattern.MANGA_IMAGE_URL: r"\((.+)\)",
    },
}

SELECTORS = {
    Sources.MANGAKAKALOT: {
        Selector.MANGA_URL: "link[rel=\"alternate\"]",
        Selector.MANGA_IMAGE_URL: "div.manga-info-pic > img",
        Selector.MANGA_TITLE: ".manga-info-text > li > h1",
        Selector.MANGA_DESCRIPTION: "div#noidungm",
        Selector.CHAPTER_URL: "div.chapter-list > div.row > span > a",
        Selector.CHAPTER_IMAGES: "div.vung-doc img",
        Selector.SEARCHED_URL: "h3.story_name > a",
    },
    Sources.LEVIATANSCANS: {
        Selector.MANGA_URL: "a.media-content",
        Selector.MANGA_IMAGE_URL: "a.media-content",
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