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

# Modules
from instructions import Answers #this imports the instructions.py file
from file_operations import read_file, write_file

if __name__ == "__main__":

    # Takes the answers and stores them as an object
    readme = Answers(answers["author"], 
                     answers["contact"], 
                     answers["title"], 
                     answers["description"], 
                     answers["installation"], 
                     answers["license"])


    # Defined the variables 
    output_file = "README_to_file_test.md"  
    collection = f"Name: {readme.author}, Contact: {readme.contact}, Title: {readme.title}, Description: {readme.description}, Installation: {readme.installation}, License: {readme.license}"
    
    # File operations
    # Writes the README.md file with the readme object
    write_file(output_file, collection )
    # Print the content of the README.md file
    print("File content:", read_file(output_file))  