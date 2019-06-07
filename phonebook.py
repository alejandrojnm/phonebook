import fnmatch
from utils import validate, sort_data, print_contact


class NotAPhoneNumberException(ValueError):
    """
    To handle a invalid phone number
    """
    pass


class PhoneBook:
    """
    Main class for Phonebook
    """
    def __init__(self, filename):
        self.filename = filename
        self.all_data = []

    def create_contact(self):
        """
        Function to create a contact
        :return: none
        """
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        if not validate(str(phone)):
            raise NotAPhoneNumberException

        self.all_data.append([name, validate(phone), 0])
        self.all_data = sort_data(self.all_data)

    def list_all_contact(self):
        """
        Function list all contact
        :return: list of all contacts
        """
        print('-------------------------------------------------------------')
        print_contact({'name': 'NAME', 'phone': 'PHONE'})
        print('-------------------------------------------------------------')
        for item in self.all_data:
            print_contact({'name': item[0], 'phone': item[1]})
        print('-------------------------------------------------------------')

    def search_contact(self):
        """
        Function to search contact based on the input
        :return: list of contacts found
        """
        search = input("Please enter name or phone: ")
        print('-------------------------------------------------------------')
        print_contact({'name': 'NAME', 'phone': 'PHONE'})
        print('-------------------------------------------------------------')
        for item in self.all_data:
            if fnmatch.fnmatch(str.lower(item[0]), '*{}*'.format(str.lower(search))) or fnmatch.fnmatch(
                    item[1], '*{}*'.format(search)):
                print_contact({'name': item[0], 'phone': item[1]})
        print('-------------------------------------------------------------')

    def delete_contact(self):
        """
        Function to delete contact
        :return: none
        """
        search = input("Please enter name or number: ")
        new_data = []
        for item in self.all_data:
            if not fnmatch.fnmatch(str.lower(item[0]), '*{}*'.format(str.lower(search))) or fnmatch.fnmatch(
                    item[1], '*{}*'.format(search)):
                new_data.append([item[0], item[1], item[2]])

        self.all_data = sort_data(new_data)

        return print("The contact was successfully deleted\n")

    def make_call(self):
        """
        Funtion to make call and increment counter
        :return: msg
        """
        number = input("Please enter phone number: ")
        if validate(number):
            try:
                self.all_data[[i for i, x in enumerate(self.all_data) if x[1] == validate(number)][0]][2] += 1
                print('Successful call')
            except IndexError:
                print('The number you are trying to call does not exist in the Phonebook')
        else:
            print('The number is not valid')

    def list_top_contact(self):
        """
        Function list top 5 contact
        :return: list of top 5 contacts
        """
        print('-------------------------------------------------------------------------')
        print_contact({'name': 'NAME', 'phone': 'PHONE', 'outgoing': 'OUTGOING CALL'}, top=True)
        print('-------------------------------------------------------------------------')
        for item in sort_data(self.all_data, 2)[:5]:
            print_contact({'name': item[0], 'phone': item[1], 'outgoing': item[2]}, top=True)
        print('-------------------------------------------------------------------------')

    def run(self):
        """
        Main function to run program
        :return:
        """
        while True:
            # load data to memory
            if not self.all_data:
                tmp_data = []
                with open(self.filename, 'r') as f:
                    for line in f:
                        data = line.strip().split(',')
                        if validate(data[1]):
                            tmp_data.append([data[0], validate(data[1]), 0])

                self.all_data = sort_data(tmp_data)

            print('''Greetings user! Let's make an addressbook!
            
Would you like to:
1.) Add a New Contact
2.) List All Contacts
3.) Search Contacts
4.) Delete A Contact
5.) Make Call
6.) List top 5 Call
7.) Quit Program\n''')

            choice = input("Select an option: ")

            if choice == "1":
                try:
                    self.create_contact()
                except NotAPhoneNumberException:
                    print("The phone number entered is invalid, creation aborted!")

            elif choice == "2":
                self.list_all_contact()

            elif choice == "3":
                self.search_contact()

            elif choice == "4":
                self.delete_contact()

            elif choice == "5":
                self.make_call()

            elif choice == "6":
                self.list_top_contact()

            elif choice == "7":
                print("Ending Contact Book.\nHave a nice day!")
                break

            else:
                print("Invalid Input! Try again.")


if __name__ == "__main__":
    PhoneBook('contact.txt').run()
