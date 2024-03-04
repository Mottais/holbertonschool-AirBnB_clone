#!/usr/bin/python3
"""
Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        print("Goodbye!")
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        print("\nGoodbye!")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
