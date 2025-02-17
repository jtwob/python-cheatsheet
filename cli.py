import cmd

class MyCLI(cmd.Cmd):
    prompt = '(mycli) '
    intro = "Simple CLI example"

    def do_greet(self, name):
        """Greets the person"""
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

    def do_exit(self, inp):
        """Exit the application"""
        print("Bye")
        return True
    
    def default(self, inp):
        print("Invalid command")

    def emptyline(self):
        pass

if __name__ == '__main__':
    MyCLI().cmdloop()