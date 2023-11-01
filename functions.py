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


def write_todos(todos: list[str], file_path: str = "todos.txt") -> None:
    """
    Write todos to a file.

    Args:
        todos (List[str]): The list of todos.
        file_path (str, optional): The file path to write todos to.
        Defaults to "todos.txt".
    """
    with open(file_path, "w") as file:
        file.writelines(todos)


def read_todos(file_path: str = "todos.txt") -> list[str]:
    """
    Read todos from a file.

    Args:
        file_path (str, optional): The file path to read todos from.
        Defaults to "todos.txt".

    Returns:
        List[str]: The list of todos.
    """
    with open(file_path, "r") as file:
        todos = file.readlines()
    return todos
