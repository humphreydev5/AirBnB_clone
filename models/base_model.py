#!/usr/bin/python3
''' BaseModel that defines all common attributes/methods
for other classes'''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defining a class base model"""
    def __init__(self, *arg, **kwargs):
        """Initialization of base class instance
        Args:
            *args: arguments
            **kwargs: key-value arguments
        """
        from . import storage  # Import with the methond
        if kwargs:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Defining save method"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Defining to_dict method"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        for k in dct:
            if type(dct[k]) is datetime:
                dct[k] = dct[k].isoformat()
        return dct

    def __str__(self):
        ''' returns a string representation of the model '''
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)
