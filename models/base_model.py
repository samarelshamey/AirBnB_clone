#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models

storage = FileStorage()


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
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for k, v in kwargs.items():
                if k == "_class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_format))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """update attr update_at with the current time"""

        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dict containing all k/v of dict of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """print format"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
