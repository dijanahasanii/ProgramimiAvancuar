# Import necessary module for date and time functionality
import datetime

def get_user_name():
    """
    Prompt the user for their name with input validation.
    
    This function repeatedly asks for input until a non-empty name is provided.
    It handles empty input and trims whitespace from the input.
    
    Returns:
        str: The validated user name
    """
    while True:
        try:
            name = input("Please enter your name: ").strip()
            if name:  # Check if name is not empty after stripping whitespace
                return name
            else:
                print("Error: Name cannot be empty. Please try again.")
        except KeyboardInterrupt:
            # Handle cases where user cancels input (Ctrl+C)
            print("\nInput canceled. Exiting program.")
            exit()

# Main program execution
if __name__ == "__main__":
    # 1. Print initial greeting
    print("Hello, World!")
    
    # 2. Get user's name with validation
    user_name = get_user_name()
    
    # 3. Personalized greeting
    print(f"Hello, {user_name}! Welcome to the program.")
    
    # 4. Get and display current date/time
    try:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current date and time: {formatted_time}")
    except Exception as e:
        print(f"Error retrieving date/time: {e}")