from manga.manga import MangaScraper
from manga.constants import Sources


def test_search_mangakakalot():
    mangas = MangaScraper.search('Sorcerer', Sources.MANGAKAKALOT)
    print(len(mangas))
    print(mangas[0])

    assert mangas[0]['title'] == 'I Am The Sorcerer King'
    assert mangas[0]['url'] == 'https://mangakakalot.com/manga/rx919523'


def test_search_leviatanscans():
    mangas = MangaScraper.search('survival', Sources.LEVIATANSCANS)
    print(len(mangas))
    print(mangas[0])

    assert mangas[0]['title'] == 'Survival Story of a Sword King in a Fantasy World'


if __name__ == '__main__':
    test_search_mangakakalot()
    test_search_leviatanscans()


