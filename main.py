from os import path
import csv


def show_all():
    pass

def search():
    pass

def add_new_contact():
    pass

def edit():
    pass

def delete():
    pass

def imp():
    pass

def read_records():
    pass

def main_menu():
    play = True

    while play:
        read_records()
        answer = input("\nPhone book. Select operation:\n\n"
                       "1. Show all\n"
                       "2. Search\n"
                       "3. Add a record\n"
                       "4. Edit\n"
                       "5. Delete\n"
                       "6. Export\n"
                       "7. Import\n"
                       "8. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                search()
            case "3":
                add_new_contact()
            case "4":
                edit()
            case "5":
                delete()
            case "6":
                export()
            case "7":
                imp()
            case "8":
                play = False
            case _:
                print("Try again!\n")


main_menu()