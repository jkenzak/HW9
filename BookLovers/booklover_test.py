import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        book = BookLover('Jack', 'jak5je@virginia.edu', 'fantasy')
        book.add_book('Game of Thrones', 5)
        actual = 'Game of Thrones' in book.book_list['book_name'].values
        expected = True
        self.assertEqual(actual, expected)

    def test_2_add_book(self):
        book = BookLover('Jack', 'jak5je@virginia.edu', 'fantasy')
        book.add_book('Game of Thrones', 5)
        book.add_book('Game of Thrones', 4)
        actual = len(book.book_list) == 1
        expected = True
        self.assertEqual(actual, expected)

    def test_3_has_read(self):
        book = BookLover('Jack', 'jak5je@virginia.edu', 'fantasy')
        book.add_book('Game of Thrones', 5)
        actual = book.has_read('Game of Thrones')
        expected = True
        self.assertEqual(actual, expected)

    def test_4_has_read(self):
        book = BookLover('Jack', 'jak5je@virginia.edu', 'fantasy')
        book.add_book('Game of Thrones', 5)
        actual = book.has_read('Clash of Kings')
        self.assertFalse(actual)

    def test_5_num_books_read(self):
        book = BookLover('Jack', 'jak5je@virginia.edu', 'fantasy')
        book.add_book('Game of Thrones', 4)
        book.add_book('Clash of Kings', 5)
        book.add_book('Storm of Swords', 5)
        expected = 3
        self.assertEqual(book.num_books_read(), expected)

    def test_6_fav_books(self):
        book = BookLover('Jack', 'jak5je@virginia.edu', 'fantasy')
        book.add_book('Game of Thrones', 4)
        book.add_book('Clash of Kings', 5)
        book.add_book('Storm of Swords', 2)
        book.add_book('Feast for Crows', 3)
        favs = book.fav_books()
        self.assertTrue(min(favs['book_rating'].values) > 3)
        

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)

    