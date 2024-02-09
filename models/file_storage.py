#!/usr/bin/python3
"""defines class"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary"""
        return __objects

    def new(self, obj):
        """sets"""
