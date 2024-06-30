import pytest


from main import BooksCollector

class TestBooksCollector:

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

    def test_get_book_genre_shows_success_genre(self):
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_shows_success_genre_list(self):
        specific_genre = self.collector.get_books_with_specific_genre('Ужасы')

        assert specific_genre[0] == 'Гордость и предубеждение и зомби'

    def test_get_books_genre_shows_success_books_dict(self):
        dict_books = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Фантастика'
        }

        assert self.collector.get_books_genre() == dict_books

    def test_get_books_for_children_shows_success_bools_list(self):
        children_books = self.collector.get_books_for_children()

        assert len(children_books) == 1 and children_books[0] == 'Что делать, если ваш кот хочет вас убить'

    def test_add_book_in_favorites_add_one_favorites_book(self):
        self.collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert self.collector.get_list_of_favorites_books()[0] == 'Гордость и предубеждение и зомби'

    def test_delete_book_from_favorites_deleted_one_favorites_book(self):
        self.collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in self.collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_shows_success_favorites_books(self):
        self.collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert self.collector.get_list_of_favorites_books()[0] == 'Что делать, если ваш кот хочет вас убить'
