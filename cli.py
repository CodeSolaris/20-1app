from time import strftime

from functions import add_todo, complete_todo, display_todo_list, edit_todo

now = strftime("%B %Y %H:%M:%S")
print("It's", now)


def main():
    prompt = "Enter your action: add, show, edit, complete or exit: "

    while True:
        action = input(prompt).strip().lower()

        if action.startswith("add"):
            todo = action.replace("add", "").strip()
            add_todo(todo)

        elif action.startswith(("show", "display")):
            display_todo_list()

        elif action.startswith("exit"):
            break

        elif action.startswith("edit"):
            edit_todo(action)

        elif action.startswith("complete"):
            complete_todo(action)

        else:
            print("Hey, you entered an unknown command.")


if __name__ == "__main__":
    main()
