#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """superclass"""
    def __init__(self, *args, **kwargs):
        """construct/

        Args:
            args: arguments
            kwargs: key and value of attrs
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)


    def __str__(self):
        """print format"""
        retutn "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update attr update_at with the current time"""

        self.update_at = datetime.now()

    def to_dict(self):
        """return a dict containing all k/v of dict of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
