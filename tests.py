import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_new_books_have_not_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гермиона Грейнджер и я же говорила')
        assert collector.get_book_genre('Гермиона Грейнджер и я же говорила') == ''

    @pytest.mark.parametrize('name, genre', [['Рубеус Хагрид и зря я это сказал', 'Комедии']])
    def test_set_book_genre_set_genre_to_new_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_show_books_with_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Рубеус Хагрид и зря я это сказал')
        collector.add_new_book('Рон Уизли и пауки заставляют танцевать')
        collector.set_book_genre('Рубеус Хагрид и зря я это сказал', 'Комедии')
        collector.set_book_genre('Рон Уизли и пауки заставляют танцевать', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Рон Уизли и пауки заставляют танцевать']

    def test_get_books_genre_show_actual_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Рубеус Хагрид и зря я это сказал')
        collector.add_new_book('Рон Уизли и пауки заставляют танцевать')
        collector.add_new_book('Гермиона Грейнджер и я же говорила')
        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_not_show_horror_books(self):
        collector = BooksCollector()
        collector.add_new_book('Рубеус Хагрид и зря я это сказал')
        collector.add_new_book('Рон Уизли и пауки заставляют танцевать')
        collector.set_book_genre('Рубеус Хагрид и зря я это сказал', 'Комедии')
        collector.set_book_genre('Рон Уизли и пауки заставляют танцевать', 'Ужасы')
        assert collector.get_books_for_children() != ['Рон Уизли и пауки заставляют танцевать']

    def test_add_book_in_favorites_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гермиона Грейнджер и я же говорила')
        collector.add_book_in_favorites('Гермиона Грейнджер и я же говорила')
        assert collector.get_list_of_favorites_books() == ['Гермиона Грейнджер и я же говорила']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гермиона Грейнджер и я же говорила')
        collector.add_book_in_favorites('Гермиона Грейнджер и я же говорила')
        collector.delete_book_from_favorites('Гермиона Грейнджер и я же говорила')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_show_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
