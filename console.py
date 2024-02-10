#!/usr/bin/python3

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
