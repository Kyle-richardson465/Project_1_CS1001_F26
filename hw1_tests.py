"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count(text = "Kyle RIchardson"), 4) 

    def test_vowel_count_No_vowel(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count(text = "Nymph"),0)
    def test_vowel_count_empty_list(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count([]),[])

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([[1], [2, 3], [], [4, 5, 6], [7, 8]]),[[2, 3], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([[0,0,0],["",""],[100]]), [["",""]])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs(([[9, 2], [3, 1, 2], [5, 5]])),([[2, 9], [3, 1, 2], [5, 5]]))

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs(([[2,10],[10,10,10],[0,100]])),([[2,10],[10,10,10],[0,100]]))

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3, 25), data.Price(2, 50)), 5.75)

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3, 75), data.Price(2, 50)), 6.25)

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
       # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
       self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(0,0),data.Point(1,1))),1)
    def test_rectangle_area_negative_coordinates(self):
       # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
       self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-1,-1),data.Point(5,5))),36)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author(("J.K Rowling"),[data.Book(["J.K Rowling"], "Harry Potter"),data.Book(["Rick Riordian"],"Percy Jackson"),data.Book(["J.K Rowling"],"Harry Potter and the half blood prince")]),(["Harry Potter","Harry Potter and the half blood prince"]))

    def test_books_by_author_no_matches(self):
       # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author(("James Patterson"),[data.Book(["J.K Rowling"], "Harry Potter"),data.Book(["Rick Riordian"],"Percy Jackson"),data.Book(["J.K Rowling"],"Harry Potter and the half blood prince")]),([]))


    


    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0,0),data.Point(3,4))),(2.5,(1.5,2.0)))

    def test_circle_bound_different_circle(self):
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0,0),data.Point(6,4))),(13**0.5,(3.0,2.0)))


    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([data.Employee("sam",16.50),data.Employee("bob",18),data.Employee("kenny",1.50),data.Employee("steven",16.50)]),(["kenny"]))

   
    def test_below_pay_average_empty_list(self):
       # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
       self.assertEqual(hw1.below_pay_average([]),([]))



if __name__ == '__main__':
    unittest.main()
