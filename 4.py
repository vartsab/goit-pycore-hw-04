def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return f"The name {name} is already exists on your contacts list."
        else:
            contacts[name] = phone
            return "Contact added."
    except ValueError:
        return "Wrong input! Please use the following format:" \
                "add <Name> <Phone number>"

def change_contact(args, contacts):
    # checking if the prompt was entered correctly
    try:
        name, phone = args
        # checking if the name exists
        if name in contacts:
            # updating the phone number
            contacts[name] = phone
            return "Contact updated."
        else:
            # returning an error message if the name is not in the dictionary
            return f"The name {name} is not on your contacts list yet."
    except ValueError:
        return "Wrong input! Please use the following format:" \
                "change <Name> <Phone number>"

def show_phone(args, contacts):
    # checking if the prompt was entered correctly
    try:
        name = args[0]
        # checking if the name exists
        if name in contacts:
            # returning the name if the name is in the dictionary
            return contacts[name]
        else:
            # returning the error message if the name is not in the dictionary
            return f"The name {name} is not on your contacts list yet."
    except ValueError:
        return "Wrong input! Please use the following format:" \
                "phone <Name>"

def show_all(contacts):
    # declare a string to store the results
    res = ""
    # checking if the list is empty
    if not len(contacts) == 0:
        # returning an error message if it's empty
        return "Your contact list is empty."
    else:
        # loop through the dictionary appending names and phone numbers
        # to the resulting string
        for name, phone in contacts.items():
            res += f"{name}: {phone} \n"
        # removing extra line at the end of the resulting string
        return res.rstrip("\n")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()