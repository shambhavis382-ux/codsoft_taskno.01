todo_list = []

print("TO-DO LIST")
print("1. View Tasks")
print("2. Add Task")
print("3. Update Task")
print("4. Delete Task")
print("5. Exit")
choice = input("Select an option: ")
if choice == '1':
    print("Your Tasks:")
    for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
elif choice == '2':
    newtask = input("Enter the task: ")
    todo_list.append(newtask)
    print("Task added.")

elif choice == '3':
    index = int(input("Enter task number to be updated: ")) - 1
    if 0 <= index < len(todo_list):
        todo_list[index] = input("Enter the new task: ")
        print("Task updated.")
    else:
        print("Invalid choice.")
elif choice=='4':
    index = int(input("Enter task number to be deleted: ")) - 1
    if 0 <= index < len(todo_list):
         todo_list.pop(index)
elif choice == '5':
    print("Thank you!")
else:
     print("Invalid Choice.")