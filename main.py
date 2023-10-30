def main():
    prompt = "Enter your action: add, show, edit, complete or exit: "

    while True:
        action = input(prompt).strip().lower()

        if action.startswith('add'):
            todo = action.replace('add', '').strip()

            todos = read_todos()
            todos.append(todo.capitalize() + '\n')

            write_todos(todos)

        elif action.startswith(('show', 'display')):
            todos = read_todos()

            for index, item in enumerate(todos):
                print(f'{index + 1}. {item.strip()}')

        elif action.startswith('exit'):
            break

        elif action.startswith('edit'):
            todos = read_todos()

            number = int(input('Enter number of the todo to edit: ')) - 1
            todos[number] = input('Enter new todo: ') + '\n'

            write_todos(todos)

        elif action.startswith('complete'):
            number = int(action.replace('complete', '').strip())

            todos = read_todos()
            index = number - 1
            completed_todo = todos.pop(index).strip()
            message = f'The todo: "{completed_todo}" was completed.'
            print(message)

            write_todos(todos)

        else:
            print("Hey, you entered an unknown command.")


def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


def read_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


if __name__ == '__main__':
    main()
