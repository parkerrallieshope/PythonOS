import requests
from bs4 import BeautifulSoup
import os
import sys
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def fetch_and_display_text(url):
    try:
        # Redirect stderr to os.devnull
        sys.stderr = open(os.devnull, 'w')

        # Fetch the web page
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all text elements excluding those within script and style tags
        text_elements = soup.find_all(text=True)

        # Filter out text elements within script and style tags
        filtered_text = [element.strip() for element in text_elements if element.parent.name not in ['script', 'style']]

        # Print the filtered text elements in order
        print_html = True
        for element in filtered_text:
            # Skip empty or whitespace only text
            if element:
                if print_html:
                    # Skip printing 'html' if it's at the beginning
                    if element.lower() == 'html':
                        continue
                    else:
                        print_html = False
                print(element)

    except Exception as e:
        print("An error occurred while fetching the webpage:", e)

    finally:
        # Restore stderr
        sys.stderr.close()
        sys.stderr = sys.__stderr__

def main():
    while True:
        clear_screen()
        protocol = input("Do you want to connect via 'insecure' (HTTP) or 'secure' (HTTPS)? Type 'exit' to quit: ").lower()
        
        if protocol == 'exit':
            print("Goodbye!")
            break
        elif protocol == 'insecure' or protocol == 'http':
            insecure_confirm = input("You have chosen to connect via HTTP (insecure). Continue? (yes/no): ").lower()
            if insecure_confirm == 'yes':
                url = input("Enter the URL of the website: ")
                if not url.startswith('http://'):
                    url = 'http://' + url
                clear_screen()
                print("Fetching content from:", url)
                fetch_and_display_text(url)
                input("Press Enter to continue...")
            else:
                continue
        elif protocol == 'secure' or protocol == 'https':
            url = input("Enter the URL of the website: ")
            if not url.startswith('https://'):
                url = 'https://' + url
            clear_screen()
            print("Current URL:", url)
            fetch_and_display_text(url)
            input("Press Enter to continue...")
        else:
            print("Invalid input. Please enter 'insecure', 'secure', or 'exit'.")

if __name__ == "__main__":
    main()
