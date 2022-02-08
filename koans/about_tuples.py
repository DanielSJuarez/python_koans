#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTuples(Koan):
    def test_creating_a_tuple(self):
        count_of_three = (1, 2, 5)
        # tuples are ways to old multiple value in a single variable. This is ordered and unchangable
        self.assertEqual(5, count_of_three[2])

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):

        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        self.assertRegex(msg, "'tuple' object does not support item assignment")

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three = (1, 2, 5)
        with self.assertRaises(Exception): #add expection to complete error type
            count_of_three.append("boom")

        # Tuples are less flexible than lists, but faster.

    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three) #this is total replacement, so creating a list. Appending to that, then setting a total new value to the previous tuple with the list
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual((1, 2, 5, "boom"), count_of_three)

    def test_tuples_of_one_look_peculiar(self):
        self.assertEqual(int, (1).__class__)
        self.assertEqual(tuple, (1,).__class__) #since tuple's have to have mulitple values this and the following are tuples as they have empty slot for the next item
        self.assertEqual(tuple, ("I'm a tuple",).__class__)
        self.assertEqual(str, ("Not a tuple").__class__)

    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(('S','u','r','p','r','i','s','e','!'), tuple("Surprise!")) #you can use a tuple to seperate all values inside of a string.

    def test_creating_empty_tuples(self):
        self.assertEqual((), ()) #empty so equals empty
        self.assertEqual((), tuple())  # Sometimes less confusing #empty tuple is empty

    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(('Area 51', (37, 14, 6, 'N'), (115, 48, 40, 'W')), place) #just a spread of the tuple inside of a new one. They will maintain their structure

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append(("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')))

        self.assertEqual('Cthulu', locations[2][0]) #since the tuple is unchangable it cannot be changed, but we are just accessing the values of the list view index
        self.assertEqual(15.56, locations[0][1][2])
