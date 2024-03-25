"""
CP1404 - Practical 7
Name: <Arun Parajuli>
"""
class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def supports_pointer_arithmetic(self):
        """Check if the language supports pointer arithmetic."""
        return self.pointer_arithmetic


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, True)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)

    languages = [ruby, python, visual_basic]

    print("Languages:")
    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("\nThe languages that support pointer arithmetic are:")
    for language in languages:
        if language.supports_pointer_arithmetic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
