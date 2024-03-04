#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects."""

    prompt = "(HBNB) "

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
