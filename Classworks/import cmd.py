import cmd

# phone number: [name, city],
DATABASE = {}

def create_contact(phone, name=None, city=None):
    DATABASE[phone] = [name, city]
    return DATABASE[phone]

def list_contacts():
    return DATABASE

class PhoneBooksShell(cmd.Cmd):
    intro = 'Welcome to the phone book shell. Type help or ? to list commands.\n'
    prompt = '(phonebook) '
    database_file = None

    def do_create_contact(self, arg):
        """Create contact in format: name, phone, city"""
        print(repr(arg))
        name, phone, city = arg.split(' ')
        create_contact(name=name, phone=phone, city=city)

    def do_list_contacts(self, arg):
        """List all contacts in database"""
        contacts = list_contacts()
        for contact in contacts:
            print(contact, contacts[contact])


if __name__ == '__main__':
    shell = PhoneBooksShell()
    shell.cmdloop()