#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(0, len(empty_dict)) #dictionary is the equiv to a object, this is set to a lenght of 0 as it has not contents

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(2, len(babel_fish)) #lenght of 2 as it has 2 value pairs

    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual('uno', babel_fish['one'])
        self.assertEqual('dos', babel_fish['two']) #uses bracket notation to access data

    def test_changing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        expected = {'one': 'eins', 'two': 'dos'}
        self.assertDictEqual(expected, babel_fish) #using bracket notation and setting the value with equals

    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(True, dict1 == dict2) #order does not matter as long as the key value pairs are the same


    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys())) #dictionary has {key: value} this is checking to validate if the value matches
        self.assertEqual(2, len(babel_fish.values()))
        self.assertEqual(True, 'one' in babel_fish.keys())
        self.assertEqual(False, 'two' in babel_fish.values())
        self.assertEqual(False, 'uno' in babel_fish.keys())
        self.assertEqual(True, 'dos' in babel_fish.values())

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards)) #is taking setting keys from all the initial values pushed in, and spreading the value passed at the end to all keys
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])

