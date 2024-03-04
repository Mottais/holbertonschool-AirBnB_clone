#!/usr/bin/python3
"""definition of class used to store objects"""
import json
import importlib


class FileStorage:
    """
    This class represents a file storage system
    for objects in the application.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary '__objects' containing all objects."""
        return self.__objects

    def new(self, obj):
        """Adds the object saved to '__objects' dictionary."""
        index = obj.__class__.__name__ + "." + obj.id
        self.__objects[index] = obj

    def save(self):
        """Serializes '__objects' dictionary to a JSON file."""
        dict_to_save = {}
        for key, obj in self.__objects.items():
            dict_to_save[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """Deserializes the JSON file and loads objects into '__objects'."""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as file:
                Dico_objets = json.load(file)
                for key, value in Dico_objets.items():
                    self.__objects[key] = BaseModel(**value)
        except Exception:
            pass
