class ProgrammingLanguage:
    """Represent details about programming language"""

    def __init__(self, field, typing, reflection, year):
        """Initialize programming language"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string that represents programming language information"""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine whether programming language is dynamic"""
        return self.typing == "Dynamic"