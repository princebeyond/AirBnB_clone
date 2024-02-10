                                   BEGINNING OF AIRBNB
FIRST FILE -> base_model super class BaseModel:
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

SECOND FILE -> __init__.py magic method for models
	Setting up File Storage:
	The line from models.engine.file_storage import FileStorage 
	imports the FileStorage class from a file called file_storage.py located in the models
	/engine directory. This class likely provides functionality to store and retrieve data in JSON format.

	Creating a FileStorage Instance:
	The line storage = FileStorage() creates an instance of the FileStorage class 
	and assigns it to the variable storage. This instance represents a storage system that can store and retrieve data

	Reloading Data: 
	The line storage.reload() invokes the reload() method of the FileStorage instance. 
	This method is responsible for loading data from a JSON file into memory. 
	If there's previously stored data in the JSON file, this method loads it into the __objects attribute of the FileStorage instance.

THIRD FILE -> filestorage (haven't gone really deep into the tasks but this and base_model is tricky for me atleast) super class FileStorage
def __init__(self)
	atrributes paths and object

def all(self)
	returns the dictionary __objects
	while the all() method may not be strictly necessary for the basic functionality 
	of the FileStorage class, it provides valuable functionality for debugging, data retrieval, and integration purposes, making it a useful addition to the class.

def new(self, obj)
	sets in __objects the obj with key <obj class name>.id
	created a unique key by combining the class
	name and the id of the object

def save(self)
	serializes __objects to the JSON file (path: __file_path)

def reload(self)
	deserializes the JSON file to __objects
        (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
