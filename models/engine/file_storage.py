#!/usr/bin/python3

"""FileStorage module"""
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}  # store all objects by <class name>.id

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds obj to __objects"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
	my_dict = {k: v.to_dict() for k, v in self.__objects.items()}

        with open(self.__filepath, "w") as file:
            json.dump(my_dict, file)

    def reload(self):
        """Deserialize JSON file to __objects"""
	new = {}
        try:
	    with open(self.__filepath, "r") as file:
                new = json.load(file)

                for k, v in new.items():
                    self.__objects[k] = self.classes[v["__class__"]](**v)
        except:
            pass
