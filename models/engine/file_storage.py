#!/usr/bin/python
# file: modle/engine
# Auth: kelechi nnadi <@alx swe>

""" storing file in the engine """
import json
from models import BaseModel

class FileStorage:
    """ defining the storage class to store data
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ defintion of all attr"""

        return FileStorage.__objects

    def new(self, obj):
        """define the new method"""

        key == "{}.{}".format(obj._class_._name_, obj.id)
        FileStorage.__object[key] = obj
