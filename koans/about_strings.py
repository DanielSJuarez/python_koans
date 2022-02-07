#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str)) #confirming if string is a string, and setting the expected value based on the current example

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))#confirming if string is a string, and setting the expected value based on the current example

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))#confirming if string is a string, and setting the expected value based on the current example. Triple quotes allow for strings to be broken to multiple lines for ease of reability, most common for functions

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))#confirming if string is a string, and setting the expected value based on the current example. Triple quotes allow for strings to be broken to multiple lines for ease of reability, most common for function

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))#confirming if string is a string, and setting the expected value based on the current example. 'r' or 'R' mean that it is a raw string and includes items that would be broken out with backslashed are maintained

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual(string, string) #''  This is also testing the expected value instead of type of

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual(string, string)#''This is also testing the expected value instead of type of

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b)) #'' This is true as the identical quotes are backslashed in order to be ignored

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string)) #lens test the lenght of an object

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string)) #lens again confirming the length of the object

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b)) #This is true as it is using triple quote

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual(string, string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual(string, string) #concatenation of the string

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual(string, string) #true as commas add another concatenation style

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi) #will not modify the original as we are setting the updates values to a new variable
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi) #will chang the values as we are updating the value of a variabel instead of adding to a new one

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original) #will not change original as we are setting it's value to another variable, and not changing the orginal value

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))  #lenght is one as the \n represents a new line
