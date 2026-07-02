from InquirerPy import prompt

# Get user input with Inquirer
questions = [
    {"type": "input", "name": "name", "message": "What is your name?"},
    {"type": "input", "name": "color", "message": "What is your favorite color?"},
]
answers = prompt(questions)
