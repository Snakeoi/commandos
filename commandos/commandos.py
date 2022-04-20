from sys import argv

class Commandos(object):

    def __init__(self):
        self.known_command = False
        self.v = []

    def set_v(self):
        v = argv
        v.pop(1)
        v.pop(0)
        self.v = v

    def show_help(self, func, command):
        print('----------------------------------\nCommand:', command)
        help(func)

    def command(self, *args):
        def inner(func):
            try:
                if argv[1] == args[0]:
                    self.set_v()
                    func()
                    self.known_command = True
                elif argv[1] == 'help':
                    self.show_help(func, args[0])
                    self.known_command = True
            except IndexError:
                pass
        
        return inner

    def run(self):
        self.command()
        if self.known_command == False:
            print('Command unknown. Use the command "help" to get information about the available commands.')