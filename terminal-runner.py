import os

def main():
    print("Welcome to the terminal command executor. Type 'exit' to quit.")
    while True:
        # Prompt the user to enter a command
        user_input = input("> ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the terminal command executor. Goodbye!")
            break
        
        # Execute the command using os.system
        os.system(user_input)

if __name__ == "__main__":
    main()
