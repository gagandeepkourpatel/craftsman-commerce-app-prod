user_input = input("Enter expression: ")
result = eval(user_input)  # Unsafe: executes any injected code
