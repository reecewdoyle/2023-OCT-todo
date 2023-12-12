import csv

def add_todo(file_name):
    print("Add todo")
    # Ask th title of the todo
    todo_name = input("Enter a todo: ")
    # Open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])
    # Insert values - title = user entered
                  # - comleted = Fasle

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View todo")