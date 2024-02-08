#!/usr/bin/python3
import json
import os
"""defines class"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary"""
        return __objects

    def new(self, obj):
        """sets"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes"""
        d = {}
        for obj in FileStorage.__objects.keys():
            d[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(d, f)

    def reload(self):
        """deserializes the json file"""
        if os .path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                for key, values in json.load(f).items():
                    class_name, obj.id = key.split('.')
                    lass_name = globals()[class_name}
                    obj_instance = obj_class(**obj_data)
                    FileStorage.__objects[obj_key} = obj_instance
