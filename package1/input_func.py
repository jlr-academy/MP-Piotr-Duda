def input_person_name():
    while True:
        name = (input("Enter name: "))
        if str(name):
            return name
        elif name == "":
            print("Input required.")

def input_number():
    while True: 
        number = input("Enter phone number:")
        if int(number):
            return number
        else:
            print("Incorrent input: number is required.")

def input_person_address():
    while True:
        name = (input("Enter address: "))
        if str(name):
            return name
        elif name == "":
            print("Input required.")
        
