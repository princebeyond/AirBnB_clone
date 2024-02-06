                                   BEGINNING OF AIRBNB
first file -> base_model super class BaseModel:
def __init__(self, *args, **kwargs)
	creates a unique id and converted to string.
	time it was created.
	time it was updated.
	if kwargs not empty
	ilterates over the pairs
	treats values as datetime string
	coverts it to date time obj
	assigns the value to the corresponding attributes
	it creates a new instance with a new id
	and the current datetime as created_at and updated_at.

def save(self)
	updates the public instance attribute with nowtime

def to_dict(self):
	creates a copy of the instance
	added a key to this dict with th name
	converts my attributes to string object in isoformat()

def __str__(self)
	return a string that includes the class name, id, and dictionary representation of the instance.
all for base_model
