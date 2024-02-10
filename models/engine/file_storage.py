#!/usr/bin/python3
"""
Defines FileStorage
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances"""

    def __init__(self):
        """attributes"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        newkey = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[newkey] = obj
        # created a unique key by combining the class
        # name and the id of the object

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
    
            serialized_objects[key] = obj.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(serialized_objects, f)
        # se_ob = self.__objects
        # obj_dict = {ob_k: se_ob[ob_k].to_dict() for ob_k in se_ob.keys()}
        # with open(self.__file_path, "w") as f:
        # json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for i in data.values():
                    classna = i["__class__"]
                    del i["__class__"]
                    self.new(eval(classna)(**i))
