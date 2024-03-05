#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


obj1 = BaseModel()
obj2 = User()
obj3 = State()
obj4 = City()
obj5 = Review()
obj6 = Amenity()
obj7 = Place()

'''my_user.save()'''


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
