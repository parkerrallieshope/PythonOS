import os
import colorama
import pyautogui
import keyboard
import shutil
import time
import platform
from colorama import Fore, Style

colorama.init(autoreset=True)  # Autoreset will automatically reset colors after each print statement

def ensure_user_directory():
    user_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'user')
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    return user_dir

def run_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            exec(code, globals())  # Execute the code in the global namespace
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{file_path}' not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def create_item(item_type, name, user_directory):
    if item_type == 'file':
        if not name.endswith('.py'):
            name += '.py'
        file_path = os.path.join(user_directory, name)
        try:
            with open(file_path, 'w') as file:
                file.write("# New Python file\n")
            print(f"{Fore.GREEN}File '{name}' created successfully in Users directory.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    elif item_type == 'dir':
        dir_path = os.path.join(user_directory, name)
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"{Fore.GREEN}Directory '{name}' created successfully in Users directory.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Error: Invalid type '{item_type}' specified.{Style.RESET_ALL}")

def edit_file(file_name, user_directory):
    if not file_name.endswith('.py'):
        file_name += '.py'
    file_path = os.path.join(user_directory, file_name)
    try:
        os.system('cls')
        print(f"{Fore.GREEN}Editing file '{file_name}'. Press enter for new lines. Press enter on an empty line to save and exit.{Style.RESET_ALL}")
        print("Enter your content below...")

        content = []

        while True:
            line = input()
            if line == '':
                break
            content.append(line.replace('\\n', '\n'))

        with open(file_path, 'w') as file:
            file.write("\n".join(content))
        print(f"{Fore.GREEN}File '{file_name}' saved successfully.{Style.RESET_ALL}")
        time.sleep(3)
        os.system('cls')
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def delete_file(file_name, user_directory):
    file_path = os.path.join(user_directory, file_name)
    if os.path.isfile(file_path) and file_path.startswith(user_directory):
        try:
            os.remove(file_path)
            print(f"{Fore.GREEN}File '{file_name}' deleted successfully.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Error: File '{file_name}' not found or deletion not allowed.{Style.RESET_ALL}")

def print_help():
    print("Available commands:")
    print("  cd <directory> - Change directory")
    print("  run <filename> - Execute a Python file")
    print("  dir OR programs - List all files/programs in the current directory")
    print("  dirs - List all directories in the current directory")
    print("  previous - Go back to the previous directory")
    print("  clear - Clear the terminal screen")
    print("  help - Display this help message")
    print("  about - Display information about this operating system")
    print("  create <file/dir> <name> - Create a new Python file or directory")
    print("  edit <filename> - Edit a Python file")
    print("  delete <filename> - Delete a file in the user directory")
    print("  rename <file/dir> <old_name> <new_name> - Rename a file or directory")
    print("  license - Show MIT License.")
    print("  space - Show space taken up in PythonOS directory and space left on drive")
    print("  shutdown - Shutdown PythonOS")
    print("  reboot - Reboot PythonOS")

def print_about():
    print(f"{Fore.GREEN}PythonOS 1.0{Style.RESET_ALL}")
    print("A command-line operating system written in Python")
    print(f"Written by parkerrallieshope{Style.RESET_ALL}")

def fullscreen_shell():
    pyautogui.press('f11')
    
def rename_item(item_type, old_name, new_name, user_directory):
    if item_type == 'file':
        if not old_name.endswith('.py'):
            old_name += '.py'
        old_path = os.path.join(user_directory, old_name)
        new_path = os.path.join(user_directory, new_name + '.py')
    elif item_type == 'dir':
        old_path = os.path.join(user_directory, old_name)
        new_path = os.path.join(user_directory, new_name)
    else:
        print(f"{Fore.RED}Error: Invalid type '{item_type}' specified.{Style.RESET_ALL}")
        return

    try:
        os.rename(old_path, new_path)
        print(f"{Fore.GREEN}{item_type.capitalize()} '{old_name}' renamed to '{new_name}' successfully.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: {item_type.capitalize()} '{old_name}' not found.{Style.RESET_ALL}")
    except FileExistsError:
        print(f"{Fore.RED}Error: {item_type.capitalize()} '{new_name}' already exists.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        
def run_usage():
    print("Usage: run <filename> - Run a Python File in the current directory. Example: run time")
    print("Type 'programs' to see all .py files that are operable.")
    
def license():
    print('''MIT License

Copyright (c) 2024 parkerrallieshope

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

''')

    print('''The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''')
    
    print("DO NOT UNDER ANY CIRCUMSTANCES CHANGE OR REMOVE THIS 'LICENSE' FUNCTION FROM THE 'SOFTWARE' CODE. LEGAL ACTION WILL BE PURSUED IF YOU DO NOT COMPLY TO KEEP THIS LICENSE WITHIN THE CODE.")
    
def welcome():
    print(f"{Fore.GREEN}PythonOS 1.0{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Type 'help' for a list of commands.{Style.RESET_ALL}")
    print("")
    
def calculate_disk_space():
    # Get the directory of the running script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Calculate the total size of all files in the script directory
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(script_directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    
    # Convert total size to GB or MB as appropriate
    if total_size > 1e9:  # Check if total size is larger than 1 GB
        total_gb = total_size / (1024 * 1024 * 1024)
        total_str = f"{total_gb:.2f} GB"
    else:
        total_mb = total_size / (1024 * 1024)
        total_str = f"{total_mb:.2f} MB"
    
    # Get the total size and the amount of free space on the drive
    total, used, free = shutil.disk_usage("/")
    
    # Convert free space to GB or MB as appropriate
    if free > 1e9:  # Check if free space is larger than 1 GB
        free_gb = free / (1024 * 1024 * 1024)
        free_str = f"{free_gb:.2f} GB"
    else:
        free_mb = free / (1024 * 1024)
        free_str = f"{free_mb:.2f} MB"
    
    # Return the space used in the script directory and space left on the drive
    return total_str, free_str

def main():
    base_directory = os.path.dirname(os.path.abspath(__file__))
    current_directory = base_directory
    previous_directory = current_directory

    while True:
        user_input = input(f"{Fore.GREEN}PythonOS {Fore.RED}~ {Style.RESET_ALL}{current_directory}> ")

        if user_input.lower() == 'shutdown':
            print(f"{Fore.YELLOW}Shutting down...{Style.RESET_ALL}")
            time.sleep(2)
            break
            
        if user_input.lower() == 'reboot':
            print("Rebooting...")
            time.sleep(2)
            if platform.system() == "Windows":
                os.system('cls')
                welcome()
            else:
                os.system('clear')
                welcome()

        elif user_input.startswith('cd '):
            new_directory = user_input[3:].strip()
            new_path = os.path.abspath(os.path.join(current_directory, new_directory))
            if os.path.isdir(new_path) and new_path.startswith(base_directory):
                previous_directory = current_directory
                current_directory = new_path
                if not os.listdir(current_directory):
                    print(f"{Fore.YELLOW}Notice: Directory '{new_directory}' is empty.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Error: Cannot navigate to '{new_directory}'. Directory not found or outside base directory.{Style.RESET_ALL}")

        elif user_input.startswith('run '):
            file_name = user_input[4:].strip()
            if file_name.lower() == 'kernel.py' or file_name.lower() == 'kernel':
                print(f"{Fore.RED}Error: Execution of kernel not allowed, kernel is already running.{Style.RESET_ALL}")
            else:
                file_path = os.path.join(current_directory, file_name)
                if not file_name.endswith('.py'):
                    file_path += '.py'
                run_python_file(file_path)

        elif user_input.lower() == 'dir' or user_input.lower() == 'programs':
            files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
            if files:
                print("Files in the current directory:")
                for file in files:
                    print(file)
            else:
                print(f"{Fore.RED}Error: No files found in the current directory.{Style.RESET_ALL}")

        elif user_input.lower() == 'dirs':
            dirs = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]
            if dirs:
                print("Directories in the current directory:")
                for directory in dirs:
                    print(directory)
            else:
                print(f"{Fore.RED}Error: No directories found in the current directory.{Style.RESET_ALL}")

        elif user_input.lower() == 'previous':
            current_directory, previous_directory = previous_directory, current_directory

        elif user_input.lower() == 'help':
            print_help()

        elif user_input.lower() == 'about':
            print_about()

        elif user_input.lower() == 'clear' or user_input.lower() == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')

        elif user_input.startswith('create '):
            _, item_type, name = user_input.split(maxsplit=2)
            user_directory = ensure_user_directory()
            create_item(item_type, name, user_directory)

        elif user_input.startswith('edit '):
            _, file_name = user_input.split(maxsplit=1)
            user_directory = ensure_user_directory()
            edit_file(file_name, user_directory)

        elif user_input.lower() == '':
            continue
            
        elif user_input.startswith('delete '):
            file_name = user_input[7:].strip()
            user_directory = ensure_user_directory()
            delete_file(file_name, user_directory)
            
        elif user_input.startswith('rename '):
            args = user_input.split()[1:]
            if len(args) != 3:
                print(f"{Fore.RED}Error: Invalid syntax. Usage: rename [file/dir] [old_name] [new_name]{Style.RESET_ALL}")
            else:
                item_type, old_name, new_name = args
                rename_item(item_type, old_name, new_name, current_directory)
                
        elif user_input.lower() == 'run':
            run_usage()
            
        elif user_input.lower() == 'license' or user_input.lower() == 'credit':
            license()
            
        elif user_input.lower() == 'space':
            used_space, free_space = calculate_disk_space()
            print(f"Space in PythonOS directory taken up: {used_space}")
            print(f"Space left on drive: {free_space}")

        else:
            print(f"{Fore.RED}'{user_input}' is not recognized as an internal/external command or operable program/script.{Style.RESET_ALL}")

if __name__ == "__main__":
    fullscreen_shell()
    welcome()
    main()

colorama.deinit()
