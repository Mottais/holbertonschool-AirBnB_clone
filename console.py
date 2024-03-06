#!/usr/bin/python3
""" Console """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        return True

    def emptyline(self):
        """
        Handles empty line
        """
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_id = args[1]
            obj = storage.all().get(f"{args[0]}.{obj_id}")
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_id = args[1]
            obj = storage.all().get(f"{args[0]}.{obj_id}")
            if obj:
                del storage.all()[f"{args[0]}.{obj_id}"]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        objs = storage.all()
        args = arg.split()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif args[0] in ("BaseModel", "User", "State", "Review ",
                         "Place", "City", "Amenity"):
            print([str(obj) for obj in objs.values()
                   if obj.__class__.__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance's attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_id = args[1]
            obj = storage.all().get(f"{args[0]}.{obj_id}")
            if obj:
                if len(args) < 4:
                    print("** attribute name missing **")
                    return
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except AttributeError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
