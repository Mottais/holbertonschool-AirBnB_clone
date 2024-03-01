#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()

my_model.name = "My First Model"
my_model.my_number = 89
my_model.toto = [1, 2, 'x']
my_model.toto = [1, 2, 'y']
my_model.tutu = None
my_model.titi = 1.234
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)

print("\nJSON of my_model:\n")
print("\t: {:<15} : {:<20} : {:<40}:".format('CLE', 'TYPE', 'VALEUR'))
print("\t: {:<15} : {:<20} : {:<40}:".format('-' * 15, '-' * 20, '-' * 40))
for key in my_model_json.keys():
    print("\t: {:<15} : {:<20} : {:<40}:".format(
        key[:15],
        (str(type(my_model_json[key])))[:20],
        str(my_model_json[key])[:40]
        ))
print()
