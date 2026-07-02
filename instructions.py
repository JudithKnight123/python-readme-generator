class Answers:
    def __init__(self, author, contact, title, description, installation, license):
        self.author = author
        self.contact = contact
        self.title = title
        self.description = description
        self.installation = installation
        self.license = license

    def display(self):
        print(f"Author: {self.author}, Contact: {self.contact}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Installation: {self.installation}")
        print(f"License: {self.license}")
