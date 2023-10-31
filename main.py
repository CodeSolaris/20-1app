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
            try: 
                if action == 'edit':
                    number = int(
                        input('Please, enter a position to edit (must be a number): ')
                        ) - 1
                else:   
                    number = int(action.replace('edit', '').strip()) - 1
                todos = read_todos()

                new_todo = input('Enter new todo: ') + '\n'
                todos[number] = new_todo

                write_todos(todos)
            except ValueError:
                print('Please, enter a valid number.')
                continue

        elif action.startswith('complete'):
            try:
                if action == 'complete':
                    number = int(
                        input('Please, enter a position to complete (must be a number): ')
                        ) - 1
                else:   
                    number = int(action.replace('complete', '').strip()) - 1
                todos = read_todos()

                completed_todo = todos.pop(number).strip()
                message = f'The todo: "{completed_todo}" was completed.'
                print(message)

                write_todos(todos)
                
            except IndexError:
                print('there is no todo at this position.')
                continue

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
