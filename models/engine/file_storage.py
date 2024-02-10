#!/usr/bin/python3
"""storage module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """storage class

    Attributes:
        __file_path: name of file to save obj to
        __objects: objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        seralized_obj = {}
        for k, obj in FileStorage.__objects.items():
            seralized_obj[k] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                object_dict = json.load(f)
                for k in object_dict.values():
                    cls_name = k["__class__"]
                    del k["__class__"]
                    self.new(eval(cls_name)(**k))
        except FileNotFoundError:
            return
