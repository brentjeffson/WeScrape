from src.main.manga.Manga import Manga
from src.main.manga.consts import Sources


def test_search():
    mangas = Manga.search('Sorcerer', Sources.MANGAKAKALOT)
    print(len(mangas))
    print(mangas[0])
    assert len(mangas) == 14
    assert mangas[0]['title'] == 'I Am The Sorcerer King'
    assert mangas[0]['url'] == 'https://mangakakalot.com/manga/rx919523'


if __name__ == '__main__':
    test_search()


