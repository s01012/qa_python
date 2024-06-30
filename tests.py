import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.fixture(autouse='True')
    def books_collector_init(self):
        self.collector = BooksCollector()
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        return self.collector
    def test_add_new_book_add_one_books(self):
        self.collector.add_new_book('Му-му')
        assert len(self.collector.get_books_genre()) == 3

    def test_set_book_genre_set_new_genre(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Мультфильмы')
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Мультфильмы'

    def test_get_book_genre_call_get_book_genre(self):
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        specific_genre = self.collector.get_books_with_specific_genre('Ужасы')
        assert specific_genre[0] == 'Гордость и предубеждение и зомби'