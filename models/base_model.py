#!/usr/bin/python3
"""
Defines base model class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel that defines all common attributes/methods for other classe"""

    def __init__(self, *args, **kwargs):
        """A new BaseModel
        Args: any
        Kwargs: key/value"""

        self.id = str(uuid4())  # creates a unique id and converted to string.
        self.created_at = datetime.now()  # time it was created.
        self.updated_at = datetime.now()  # time it was updated.

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs != 0:
            # if kwargs not empty
            for key, value in kwargs.items():
                # ilterates over the pairs
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    # treats values as datetime striing
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                    # and coverts it to date time obj
                else:
                    # assigns the value to the corresponding
                    # attributes
                    self.__dict__[key] = value
        else:
            # it creates a new instance with a new id
            # and the current datetime as created_at and updated_at.
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute with nowtime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        # creates a copy of the instance
        dict_copy = self.__dict__.copy()
        # added a key to this dict with th name
        dict_copy["__class__"] = self.__class__.__name__
        # converts my attributes to string object
        # in isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """return a string that includes the class name, id,
        and dictionary representation of the instance."""
        classna = self.__class__.__name__
        return "[{}] ({}) {}".format(classna, self.id, self.to_dict())
