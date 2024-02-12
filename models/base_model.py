#!/usr/bin/python3
"""define class"""
from datetime import datetime
from uuid import uuid4
<<<<<<< HEAD
from models import storage
=======
import models
>>>>>>> master


class BaseModel:
    """defines class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
<<<<<<< HEAD
            storage.new(self)
=======
            models.storage.new(self)
>>>>>>> master

    def __str__(self):
        """return string"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
<<<<<<< HEAD
        storage.save()
=======
        models.storage.save()
>>>>>>> master

    def to_dict(self):
        """returns a dictionary containing all keys/values """
        d = {}
        d["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                d[key] = value.isoformat()
            else:
                d[key] = value
        return d
