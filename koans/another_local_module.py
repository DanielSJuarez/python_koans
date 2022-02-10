#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Goose:
    @property
    def name(self):
        return "Mr Stabby"

class Hamster:
    @property
    def name(self):
        return "Phil"

class _SecretSquirrel: #will return undefined as hidden by  _
    @property
    def name(self):
        return "Mr Anonymous"