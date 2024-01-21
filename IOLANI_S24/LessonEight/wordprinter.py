while True:
    user_input = input("Enter a word (type 'exit' to end): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the loop. Goodbye!")
        break
    
    print(f"You entered: {user_input}")
