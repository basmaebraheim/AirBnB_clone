#!/usr/bin/python3
"""This module defines a class FileStorage that serializes instances 
to a JSON file and deserializes JSON file to instances"""
import json


class FileStorage:
    """class serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        from models.base_model import BaseModel
        # from models.user import User
        # from models.place import Place
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.review import Review

        classes = {
                    'BaseModel': BaseModel,
                    # 'User': User,
                    # 'Place': Place,
                    # 'State': State,
                    # 'City': City,
                    # 'Amenity': Amenity,
                    # 'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
