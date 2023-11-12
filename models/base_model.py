#!/usr/bin/python3
''' module for BaseModel class '''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    ''' class of the base model of higher-level data models '''
    def __init__(self, *arg, **kwargs):
        ''' BaseModel constructor '''
        from . import storage
        if kwargs:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        '''saves the changes made to this model's instance'''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' returns a dictionary representation of the model '''
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
