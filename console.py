#!/usr/bin/python3

class HBNBCommand (cmd.Cmd):
 """Simple command interpreter for HBNB project."""
 prompt = "(hbnb) "


def do_quit(self, arg):
    """Exit the program"""
    return True

def do_EOF(self, arg):
    """Exit the program on EOF (ctrl+D)"""
    print("\nGoodbye!")
    return True

def emptyline(self)