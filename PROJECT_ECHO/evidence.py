class Evidence:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"""
================ EVIDENCE ================

Title : {self.title}

{self.content}

==========================================
""")