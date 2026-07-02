from InquirerPy import prompt

# Get user input with Inquirer - 
# Shows what questions the program asks the user and saves their responses into a dictionary.
questions = [
    {"type": "input", "name": "author", "message": "What is your name?"},
    {"type": "input", "name": "contact", "message": "What is your email address?"},
    {"type": "input", "name": "title", "message": "What is your project title?"},
    {"type": "input", "name": "description", "message": "Please provide a description of your project."},
    {"type": "input", "name": "installation", "message": "What are the installation instructions?"},
    {
        "type": "list",
        "name": "license",
        "message": "Please select a license:",
        "choices": ["MIT", "Apache 2.0", "GPL 3.0", "BSD 3-Clause", "None"],
    },
]
# Runs the interview and gathers the responses.
answers = prompt(questions) 




if __name__ == "__main__":

    # Takes the answers and stores them as an object
    readme = Answers(answers["author"], 
                     answers["contact"], 
                     answers["title"], 
                     answers["description"], 
                     answers["installation"], 
                     answers["license"])
