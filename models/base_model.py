#!/usr/bin/python3
"""Class BaseModel - defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Class BaseModel -
    """
    def __init__(self, *args, **kwargs):
        """func __init__ - args, kwargs - id t(str) assigns with an uuid
        when instance is created - created_at/updated_at t(datetime.datime)
        current time of instance creation - models.storage.new() FileStorage
        instance new method accessed - kwargs 'k' are attribute names
        'v' are attribute values - if created_at or updated_at convert
        t(datetime.datetime) to t(str) """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "created_at":
                    v = datetime.now()
                if k == "updated_at":
                    v = datetime.now()
                if k != "__class__":
                    self.__setattr__(k, v)

    def __str__(self):
        """func __str__ - no args - print(instace) returns class name,
        instance id, attribute dict"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """func save - no args - updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """func to_dict - no args - returns a dictionary containing all
        keys/values of __dict__ of the instance, using self.__dict__
        key __class__ is added with the class name of the object
        created_at and updated_at must be converted to t(str) object
        in ISO format - first piece of the serialization/deserialization
        process: create a t(dict) representation of BaseModel"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
