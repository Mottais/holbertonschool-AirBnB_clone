#!/usr/bin/python3
"""Definition of class basemodel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Definition of class basemodel"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """return string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns list of attributes including class name"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
