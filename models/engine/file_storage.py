#!/usr/bin/python3
"""Mod file_storage.py - class FileStorage - func all, new, save, reload"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """Class FileStorage - serializes instances to a JSON file and deserializes
     JSON file to instances - Private class attributes __file_path:
    string - path to the JSON file, __objects: dictionary - empty but will
    store all objects by <class name>.id"""
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def all(self):
        """func all - no args - returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """func new - obj - sets in __objects the obj with key
        <obj class name>.id"""
        if obj:
            self.__objects[obj.__class__.__name__ + "." + str(
                obj.id)] = obj

    def save(self):
        """func save - no args - serializes __objects to the JSON file
        (path: __file_path)"""
        try:
            d = {}
            for k, v in self.__objects.items():
                d[k] = v.to_dict()
            with open(self.__file_path, mode='w', encoding='utf-8') as a_file:
                a_file.write(json.dumps(d))
        except FileNotFoundError:
            pass

    def reload(self):
        """func reload - no args - deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding='utf-8') as a_file:
                d = json.loads(a_file.read())
            for k, v in d.items():
                self.__objects[k] = self.classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass
