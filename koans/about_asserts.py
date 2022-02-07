#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        # self.assertTrue(False) # This should be True 
        self.assertTrue(True) #This needs to be true as the item exsists and will not pass to the next statement as assert is a conditional statement returning true of false

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        # self.assertTrue(False, "This should be True -- Please fix this")
        self.assertTrue(True, "This should be True -- Please fix this") #as stated above will not pass to the next statement 

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(2, 1 + 1) #this is a test assement of 1 + 1, and the value that equals true needs to be inputed, thus 2.

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = 2 #set the expected value to make the self-assert true. This method uses a comparitor
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = 2 #set the expected value, but using better syntax
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        # assert False
        assert True #set assert to true to pass the argument

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:
        # self.assertEqual(__, "navel".__class__) # It's str, not <type 'str'>
        self.assertEqual(str, "navel".__class__) # It's asking for the type of this class, which is string. So the input requested is the type of

        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

