#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        # creates a new string with the values implemented
        self.assertEqual('The values are one and 2', string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        # enters the value in the order displayed then based on index values
        self.assertEqual('The values are DOH, doh, doh and DOH!', string)

    def test_any_python_expression_may_be_interpolated(self):
        import math  # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
                                                            decimal_places)
        # takes the {0} whole number and add the decimal point values set to the variabel
        self.assertEqual('The square root of 5 is 2.2361', string)

    def test_you_can_get_a_substring_from_a_string(self):
        # grabs the initial stargin index from the first number and the ending position and return a new string
        string = "Bacon, lettuce and tomato"
        self.assertEqual('let', string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('a', string[1])  # ''

    def test_single_characters_can_be_represented_by_integers(self):
        # order get the unicode of a character a=97, 1=98
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        # split() takes eaach word and returns a list with each word individually
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re  # import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        # '' and will allow for splitting if the special characters are complied out
        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'
   
    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        # this is simpley just a raw string and takes all characters
        self.assertEqual(string, string)
        # since this is raw it does not account for the new line break but the character lenghts
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        # .joins takes a list and returns the value of the list values added together
        self.assertEqual("Now is the time", ' '.join(words))

    def test_strings_can_change_case(self):
        # update the first letter in the word
        self.assertEqual('Guido', 'guido'.capitalize())
        # sets all letters to uppercase
        self.assertEqual('GUIDO', 'guido'.upper())
        # set all letters to lowercase
        self.assertEqual('timbot', 'TimBot'.lower())
        # capitalizes the first letter in each word
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        # swap current letters with their opposite capitalization
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
