#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    """custom prompty (hbnb"""

    def do_quit(self, line):
        """quit program"""
        return (True)

    def do_EOF(self, line):
        """exit program"""
        return True

    def do_emptyline(self):
        """shouldnt execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
