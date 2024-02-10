#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """superclass"""
    def __init__(self, *args, **kwargs):
        """construct/

        Args:
            args: arguments
            kwargs: key and value of attrs
        Attributes:
            id: class id
            created_at: datetime created at
            updated_at: datetime updated at
        """

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, t_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """update attr update_at with the current time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dict containing all k/v of dict of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """print format"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
