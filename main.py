def main():
    prompt = "Enter your action: add, show, edit, complete or exit: "

    while True:
        action = input(prompt).strip().lower()

        if action.startswith("add"):
            todo = action.replace("add", "").strip()

            todos = read_todos()
            todos.append(todo.capitalize() + "\n")

            write_todos(todos)

        elif action.startswith(("show", "display")):
            todos = read_todos()

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")

        elif action.startswith("exit"):
            break

        elif action.startswith("edit"):
            number = get_position(
                action, "Please, enter a position to edit (must be a number): "
            )
            try:
                todos = read_todos()
                todo = todos[number].strip()
                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo.capitalize() + "\n"
                write_todos(todos)
            except ValueError:
                print("Please, enter a valid number.")
                continue

        elif action.startswith("complete"):
            number = get_position(
                action, "Please, enter a position to complete (must be a number): "
            )
            try:
                todos = read_todos()
                todo_to_complete = todos.pop(number).strip()
                message = f"You have completed {todo_to_complete}"
                print(message)
                write_todos(todos)
            except IndexError:
                print("Please, enter a valid position.")
                continue

        else:
            print("Hey, you entered an unknown command.")


def get_position(action, prompt):
    if action == "edit" or action == "complete":
        number = int(input(prompt)) - 1
    else:
        number = int(action.replace("edit", "").replace("complete", "").strip()) - 1
    return number


def write_todos(todos):
    with open("todos.txt", "w") as file:
        file.writelines(todos)


def read_todos():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos


if __name__ == "__main__":
    main()
