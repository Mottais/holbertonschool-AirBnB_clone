#!/usr/bin/python3
"""definition of class used to store objects"""
import json
import importlib


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionaty '__objects'"""
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the object with the key """
        index = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[index] = obj

    def save(self):
        """Serializes '__objects' dictionary to a JSON file"""
        dict_to_save = {}
        for key, obj in self.__objects.items():
            dict_to_save[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """Deserializes the JSON file to __objects' dictionary'"""
        try:
            with open(self.__file_path, "r") as file:
                for key, value in json.load(file).items():
                    module = importlib.import_module('models.base_model')
                    fonction = getattr(module, value["__class__"], None)
                    self.__objects[key] = fonction(**value)
        except Exception:
            pass
