#!/usr/bin/python3
from models.base_model import BaseModel


def print_dict(my_model_json):

    print("\t: {:<15} : {:<20} : {:<40}:".format('CLE', 'TYPE', 'VALEUR'))
    print("\t: {:<15} : {:<20} : {:<40}:".format('-' * 15, '-' * 20, '-' * 40))
    for key in my_model_json.keys():
        print("\t: {:<15} : {:<20} : {:<40}:".format(
            key[:15],
            (str(type(my_model_json[key])))[:20],
            str(my_model_json[key])[:40]
            ))


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

print("Attributs de my_model:")
print_dict(my_model.__dict__)

my_model_json = my_model.to_dict()
print("JSON of my_model:")
print_dict(my_model_json)

my_model_json['created_at'] = "2222 06-14_12:34:56.123456"
my_model_json['updated_at'] = "3333 06-14_12:34:56.123456"
del my_model_json['created_at']
my_model_json['__class__'] = "toto"
print("JSON of my_model:")
print_dict(my_model_json)

my_new_model = BaseModel(**my_model_json)
print("Attributs de my_new_model:")
print_dict(my_new_model.__dict__)


my_new_model_json = my_new_model.to_dict()
print("JSON of my_new_model:")
print_dict(my_new_model_json)
