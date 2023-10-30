def main():
    user_prompt = 'Enter your action: add, show, edit, complete or exit: '
    actions = {
        'add': add_todo,
        'show': show_todos,
        'display': show_todos,
        'exit': exit,
        'edit': edit_todo,
        'complete': complete_todo
    }

    while True:
        user_action = input(user_prompt).strip().lower()
        prompt = user_action.split()[0]
        action = actions.get(prompt)
        if prompt in ('show', 'display', 'edit', 'exit'):
            action()
        else:
            action(user_action)


def complete_todo(user_action):
    number = int(user_action
                 .replace('complete', '')
                 .strip())
    todos = read_todos()
    index = number - 1
    completed_todo = todos.pop(index).strip()
    message = f'The todo: "{completed_todo}" was completed.'
    print(message)
    write_todos(todos)


def edit_todo():
    todos = read_todos()
    number = int(input('Enter number of the todo to edit: ')) - 1
    todos[number] = input('Enter new todo: ') + '\n'
    write_todos(todos)


def show_todos():
    todos = read_todos()
    for index, item in enumerate(todos):
        print(f'{index + 1}. {item.strip()}')


def add_todo(user_action):
    todo = user_action.replace('add', '').strip()
    todos = read_todos()
    todos.append(todo.capitalize() + '\n')
    write_todos(todos)


def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


def read_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


if __name__ == '__main__':
    main()
