import os

def simple_shell():
    while True:
        cwd = os.getcwd()
        command = input(f"{cwd}$ ").strip()
        if command.lower() == "exit":
            print("Exiting the shell...")
            break
        # split the command into parts
        parts = command.split()
        if not parts:
            continue
        
        cmd = parts[0]
        args = parts[1:]

        # Add ls command
        if cmd == "ls":
            try:
                for item in os.listdir(cwd):
                    print(item)
            except Exception as e:
                print(f"An error occurred: {e}")

        # Add cd command
        elif cmd == "cd":
            if len(args) == 0:
                print("Error: cd command requires a directory argument")
            else:
                try:
                    os.chdir(args[0])
                except Exception as e:
                    print(f"An error occurred: {e}")
        # add mkdir command
        elif cmd == "mkdir":
            if len(args) == 0:
                print("Error: mkdir command requires a directory argument")
            else:
                try:
                    os.mkdir(args[0])
                except Exception as e:
                    print(f"An error occurred: {e}")
        # handle invalid commands
        else:
            print(f"Invalid command: {cmd}")

simple_shell()