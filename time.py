import datetime
from colorama import init, Fore

# Initialize colorama
init()

# Get current time
current_time = datetime.datetime.now()

# Format time as 3:14 PM/AM
formatted_time = current_time.strftime("%I:%M %p")

# Print the formatted time in cyan color
print(Fore.CYAN + formatted_time)
