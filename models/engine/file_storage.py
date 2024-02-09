#!/usr/bin/python3
"""storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        seralized_obj = {}
        for k, obj in self.__objects.items():
            seralized_obj[k] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, serialized_obj in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**serialized_obj)
        except FileNotFoundError:
            return
