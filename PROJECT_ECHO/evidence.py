from utils import print_header


class Evidence:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print_header("Evidence File")

        print(f"""Title : {self.title}
{self.content}
""")
