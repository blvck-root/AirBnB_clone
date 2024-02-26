#!/usr/bin/python3

"""FileStorage module"""
import json
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

MODELS = [Amenity, BaseModel, City, Place, Review, State, User]

class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}  # store all objects by <class name>.id
    classes = {cls.__name__: cls for cls in MODELS}

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

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(my_dict, file)

    def reload(self):
        """Deserialize JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                for k, v in data.items():
                    cls = self.classes[v["__class__"]]  # retrieve class
                    self.new(cls(**v))
        except FileNotFoundError:
            pass
