from manga.Manga import Manga, Chapter
from manga.consts import Sources
from pathlib import Path


class TestManga:
    def test_find_chapters_leviathanscans(self):
        markup = Path('src/test/resources/leviatan_item.html').read_text()

        manga = Manga(markup, Sources.LEVIATANSCANS)
        chapters = manga.chapters
        chapter = chapters[0]

        assert len(chapters) == 5
        assert chapter.uid == '4'
        assert chapter.url == 'https://leviatanscans.com/comics/11268-survival-story-of-a-sword-king-in-a-fantasy-world/1/4'
        assert chapter.title == 'Chapter 4'

    def test_find_chapters_mangakakalot(self):
        markup = Path('src/test/resources/manga_item.html').read_text(encoding='utf-8')

        manga = Manga(markup, Sources.MANGAKAKALOT)
        chapters = manga.chapters
        chapter = chapters[0]

        assert len(chapters) == 71
        assert chapter.uid == '71'
        assert chapter.url == 'https://mangakakalot.com/chapter/rx919523/chapter_71'
        assert chapter.title == 'Chapter 71'

    def test_replace_chapter(self):
        markup = Path('src/test/resources/manga_item.html').read_text(encoding='utf-8')

        manga = Manga(markup, Sources.MANGAKAKALOT)
        manga.update(manga.chapters[0], Chapter('New', 'New', 'New'))
        chapter = manga.chapters[0]

        assert chapter.uid == 'New'
        assert chapter.url == 'New'
        assert chapter.title == 'New'

    def test_find_chapter_images(self):
        item_markup = Path('src/test/resources/manga_item.html').read_text(encoding='utf-8')
        item_content_markup = Path('src/test/resources/manga_item_content.html').read_text(encoding='utf-8')

        manga = Manga(item_markup, Sources.MANGAKAKALOT)
        updated_chapter = manga.find_images(item_content_markup, manga.chapters[0])

        assert len(updated_chapter.images) == 8
        assert updated_chapter.images[0] == 'https://s8.mkklcdnv8.com/mangakakalot/r2/rx919523/chapter_71/1.jpg'














