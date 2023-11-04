FILEPATH = "todos.txt"


def get_position(action: str, prompt: str) -> int:
    """
    Get the position of an action based on user input.

    Args:
        action (str): The action to perform.
        prompt (str): The prompt message to display.

    Returns:
        int: The position of the action.
    """
    if action == "edit" or action == "complete":
        number = int(input(prompt)) - 1
    else:
        number = int(action.replace("edit", "").replace("complete", "").strip()) - 1
    return number


def write_todos(todos: list[str], file_path: str = FILEPATH) -> None:
    """
    Write todos to a file.

    Args:
        todos (List[str]): The list of todos.
        file_path (str, optional): The file path to write todos to.
        Defaults to FILEPATH.
    """
    with open(file_path, "w") as file:
        file.writelines(todos)


def read_todos(file_path: str = FILEPATH) -> list[str]:
    """
    Read todos from a file.

    Args:
        file_path (str, optional): The file path to read todos from.
        Defaults to FILEPATH.

    Returns:
        List[str]: The list of todos.
    """
    with open(file_path, "r") as file:
        todos = file.readlines()
    return todos


def add_todo(todo):
    """
    Add a todo to the list.

    Args:
        todo (str): The todo to add.
    """
    todos = read_todos()
    todos.append(todo.capitalize() + "\n")
    write_todos(todos)


def display_todos():
    """
    Display the list of todos.
    """
    todos = read_todos()
    for index, item in enumerate(todos):
        print(f"{index + 1}. {item.strip()}")


def edit_todo(action):
    """
    Edit a todo in the list.

    Args:
        action (str): The action to perform.
    """
    number = get_position(
        action, "Please, enter a position to edit (must be a number): "
    )
    try:
        todos = read_todos()
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo.capitalize() + "\n"
        write_todos(todos)
    except ValueError:
        print("Please, enter a valid number.")


def complete_todo(action):
    """
    Complete a todo in the list.

    Args:
        action (str): The action to perform.
    """
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
