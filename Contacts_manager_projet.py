import pickle
import re


def save():
    family_file = open("family.pickle", "wb")
    pickle.dump(family, family_file)
    family_file.close()


def check():
    global family
    try:
        family_file = open("family.pickle", "rb")
        family = pickle.load(family_file)
    except IOError or EOFError:
        family = {}


def main_menu():
    check()
    print("----------------------------------------------------------------------")
    print(f"Hello, You are in the Main menu of the program.")
    print("Please, select one of the following options:")
    print("")
    print("[1] - Search contact by Name.")
    print("[2] - Search contact by City.")
    print("[3] - Search contact by Phone number.")
    print("[4] - Show all contacts.")
    print("[5] - Add new contact.")
    print("[6] - Delete contact.")
    print("[7] - Update contact.")
    print("[8] - Quit the program.")
    print("")
    print("Just type down one of the options in the console and press Enter:")
    choice = input()
    choice_menu(choice)


def choice_menu(choice):
    if choice == "1":
        search_by_name()
    elif choice == "2":
        search_by_city()
    elif choice == "3":
        search_by_number()
    elif choice == "4":
        show_contacts()
    elif choice == "5":
        add_contact()
    elif choice == "6":
        delete_contact()
    elif choice == "7":
        pass
    #    update_contact()
    elif choice == "8":
        quit()
    else:
        print("----------------------------------------------------------------------")
        print("-----------------------Invalid Choice---------------------------------")
        print("---------------------Back to Main Menu--------------------------------")
        main_menu()


def search_by_name():  # Choice - 1
    print("------------------------------------------------")
    print("Please Enter the Searched Name and press enter:")

    name = input()
    while not validate_name(name):
        validate_name_while_text()
        name = input()

        if name == "y":
            main_menu()

    not_found = True
    for key, value in family.items():
        if value[0] == name:
            not_found = False
            iterate_values(key, value)
            # print(f"There is a match:")
            # print(f"Name: {value[0]}")
            # print(f"City: {value[1]}")
            # print(f"Telephone Number: {key}")
            # print("---------------------------------------")
    if not_found:
        print("-----------------------------------------------------------------------------------------")
        print(f"Unfortunately, we did not find a contact with this Name: {name} in the contact list!")
        print("But bare in mind, that you can aways add New Contact with that Name from the Main Menu!")
        print("-----------------------------------------------------------------------------------------")

    print("If you want to try the search again, just press [a] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")
    choice = input()
    if choice == "y":
        main_menu()
    elif choice == "a":
        search_by_name()
    else:
        print("Since you didn't say neither [y], nor [a] I will quit the program for you")
        quit()


def search_by_city():  # Choice - 2
    print("Please Enter the Searched City and press enter:")

    city = input()
    while not validate_city(city):
        validate_city_while_text()
        city = input()

        if city == "y":
            main_menu()

    not_found = True
    print("---------------------------------------")
    for key, value in family.items():
        if value[1] == city:
            not_found = False
            iterate_values(key, value)
            # print(f"There is a match:")
            # print(f"Name: {value[0]}")
            # print(f"City: {value[1]}")
            # print(f"Telephone Number: {key}")
            # print("---------------------------------------")
    if not_found:
        print("-----------------------------------------------------------------------------------------")
        print(f"Unfortunately, we did not find a contact with such City: {city} in the contact list!")
        print("But bare in mind, that you can aways add New Contact with that City from the Main Menu!")
        print("-----------------------------------------------------------------------------------------")

    print("If you want to try the search again, just press [a] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")
    choice = input()
    if choice == "y":
        main_menu()
    elif choice == "a":
        search_by_city()
    else:
        print("Since you didn't say neither [y], nor [a] I will quit the program for you")
        quit()


def search_by_number():  # Choice 3 - Search by Number
    print("Please Enter the Searched Telephone Number and press enter:")

    number = input()
    while not validate_phone_number(number):
        validate_phone_while_text()
        number = input()

        if number == "y":
            main_menu()

    if number in family:
        print("----------------------------------------")
        print("We have a Match:")
        print(f"Name: {family[number][0]}")
        print(f"City: {family[number][1]}")
        print(f"Telephone number: {number}")
        print("----------------------------------------")
    else:
        print("-----------------------------------------------------------------------------------------")
        print(f"Unfortunately, we did not find a contact with such Telephone number: {number} in the contact list!")
        print("But bare in mind, that you can aways add New Contact with that number, from the Main Menu!")
        print("-----------------------------------------------------------------------------------------")

    print("If you want to try the search again, just press [a] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")
    choice = input()
    if choice == "y":
        main_menu()
    elif choice == "a":
        search_by_number()
    else:
        print("Since you didn't say neither [y], nor [a] I will quit the program for you")
        quit()


def show_contacts():  # Choice - 4
    if len(family.items()) == 0:
        print("Unfortunately, there are no contacts to show yet.")
        print("If you want to create a new contact. Press [c] and hit Enter:")
        print("If you want to go back to Main Menu press [y] and hit Enter:")
        choice = input()
        if choice == "c":
            add_contact()
        elif choice == "y":
            main_menu()
        else:
            print("Since you didn't press [c] or [y]. I will quit the program for you!")
            quit()
    print("The contacts in the list are:")
    print("---------------------------------------")
    for number, value in family.items():
        print_contact(number, value)

    print("If you want to see the contacts again, just press [a] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")
    choice = input()
    if choice == "y":
        main_menu()
    elif choice == "a":
        show_contacts()
    else:
        print("Since you didn't say neither [y], nor [a] I will quit the program for you")
        quit()


def add_contact():  # Choice - 5
    name = input("Please enter a name: ")

    while not validate_name(name):
        validate_name_while_text()
        name = input()

    #NOPE
    # while name in family:
    #     print("***WARNING***")
    #     print("The name you are trying to add already exist in the Contacts!")
    #     name = input("Please provide a different name and press Enter:")

    city = input("Please enter a city: ")
    while not validate_city(city):
        validate_city_while_text()
        city = input()

    number = input("Please enter a phone number: ")
    while not validate_phone_number(number):
        validate_phone_while_text()
        number = input()

    while number in family.keys():
        print("***WARNING***")
        # we have to think about this message
        print("The number you are trying to add already exist in the Contacts under different name!")
        number = input("Please provide a different number and press Enter:")
        while not validate_phone_number(number):
            validate_phone_while_text()
            number = input()

    family[number] = [name, city]
    save()

    print(f"-------------------------------------------------")
    print("Information is successfully added.")
    print(f"If you want to go back to the main menu, press [y]:")
    print(f"If you want to add another contact, press [a]:")

    print(f"-------------------------------------------------")
    choice = input()
    if choice == "y":
        main_menu()
    elif choice == "a":
        add_contact()
    else:
        print("Since you didn't press [s] or [y] I will quit the program for you")
        quit()


def delete_contact():  # Choice - 6
    print("Please select one of the following options:")
    #tova trqbva da go mahnem
    #print("To Delete Contact by NAME, type down [name] and hit Enter.")
    print("To Delete Contact by NUMBER, type down [number] and hit Enter.")
    print("To Escape this menu and go back to Main menu press [y] and hit Enter.")
    #toq lower e izlishen
    choice = input()  # .lower()
    # if choice == "name":
    #     name = input("Please, enter the Name you with to Delete: ")
    #     while name not in family:
    #         print("The name you are trying to Delete, Does not exist")
    #         print("Please, try again with a Name that is in the Contact List.")
    #         print("If you are not sure, about the name you can check all the contacts from the Main Menu.")
    #         name = input("Enter a valid name or press [y] and hit Enter to go back in my menu: ")
    #         if name == "y":
    #             main_menu()
    #     print("***WARNING****")
    #     print(f"Are you sure the you want to Delete {name} form the Contact List")
    #     print(f"Please type down [y] to confirm or [n] to leave it. And go back to Main Menu: ")
    #     y_or_n = input()
    #     if y_or_n == "y":
    #         del family[name]
    #         save()
    #         print(f"--------------------------------------------------------------")
    #         print("The Contact was successfully Deleted")
    #         print(f"If you want to go back to the main menu, press [y]:")
    #         print(f"If you want to review all the remaining contacts, press [s]:")
    #         print(f"--------------------------------------------------------------")
    #         choice = input()
    #         if choice == "y":
    #             main_menu()
    #         elif choice == "s":
    #             show_contacts()
    #         else:
    #             print("Since you didn't press [s] or [y] I will quit the program for you")
    #             quit()
    #     elif y_or_n == "n":
    #         main_menu()
    #     else:
    #         main_menu()
    if choice == "number":
        number = input("Please, enter the Number of the Contact you wish to Delete: ")

        while number not in family:
            # da opravim teksta
            print("The contact you are trying to Delete, Does not exist")
            print("Please, try again with a contact that is in the Contact List.")
            print("If you are not sure, about the contact you can check all the contacts from the Main Menu.")
            number = input("Enter an existing phone number or press [y] and hit Enter to go back in Main Menu: ")

            if number == "y":
                main_menu()

        print("***WARNING****")
        print(f"Are you sure the you want to Delete this contact from the Contact List")
        print("---------------------------------------")
        print_contact(number, family[number])
        print(f"Please type down [y] to confirm or [n] to leave it. And go back to Main Menu: ")

        y_or_n = input()
        if y_or_n == "y":
            del family[number]
            save()

            print(f"--------------------------------------------------------------")
            print("The Contact was successfully Deleted")
            print(f"If you want to go back to the main menu, press [y]:")
            print(f"If you want to review all the remaining contacts, press [s]:")
            print(f"--------------------------------------------------------------")

            choice_2 = input()
            if choice_2 == "y":
                main_menu()
            elif choice_2 == "s":
                show_contacts()
            else:
                print("Since you didn't press [s] or [y] I will quit the program for you")
                quit()
        else:
            main_menu()

    elif choice == "y":
        main_menu()
    else:
        print("Since you didn't press [name], [number] or [y] I will quit the program for you")
        quit()


def validate_name(name):
    if re.compile("^[A-Z][a-z]{2,}$|^[A-Z][a-z]{2,}[-][A-Z][a-z]{2,}$").match(name):
        return True


def validate_city(city):
    if re.compile("^[A-Z][a-z]{3,}$|^[A-Z][a-z]{3,}[ ]([A-Z]|[a-z])[a-z]{3,}$").match(city):
        return True


def validate_phone_number(number):
    if re.compile("^[\\d]{5,15}$").match(number):
        return True


def validate_name_while_text():
    print("***WARNING***")
    print("Invalid name format! The name must be one word starting with a Capital Letter "
          "or two words starting with capital letters and a dash between them.")
    print("Please enter a valid name, like - [Ivan] or [Anna-Maria]: ")


def validate_phone_while_text():
    print("***WARNING***")
    print("Invalid phone number! The telephone number must be between 5 and 15 numbers.")
    print("Please enter a valid phone number: ")


def validate_city_while_text():
    print("***WARNING***")
    print("Invalid city format! Please enter a valid city, like - [Sofia] or [Veliko Tarnovo]: ")
    print("Please, enter Valid City or press [y] for Main Menu:")


def iterate_values(key, value):
    print(f"There is a match:")
    print(f"Name: {value[0]}")
    print(f"City: {value[1]}")
    print(f"Telephone Number: {key}")
    print("---------------------------------------")


def print_contact(key, value):
    print(f"Name: {value[0]}")
    print(f"City: {value[1]}")
    print(f"Telephone Number: {key}")
    print("---------------------------------------")


if __name__ == "__main__":
    main_menu()
