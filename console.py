#!/usr/bin/python3
"""define class"""

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    """custom prompty (hbnb)"""

    def do_quit(self, ln):
        """quit program"""
        return (True)

    def do_EOF(self, ln):
        """exit program"""
        print()
        return True

    def emptyline(self):
        """shouldnt execute anything"""
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
