"""
CP1404 - Practical 7
Name: <Arun Parajuli>
"""
class Guitar:
    """Represents a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Check if the guitar is vintage."""
        return self.get_age(current_year) >= 50


def load_guitars(filename):
    """Load guitars from a file."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(guitars, filename):
    """Save guitars to a file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    """Display guitars."""
    for index, guitar in enumerate(guitars):
        print(f"{index + 1}. {guitar}")


def main():
    """Main function."""
    filename = "my_guitars.csv"  # Change this to your actual file name
    guitars = load_guitars(filename)

    print("Loaded guitars:")
    display_guitars(guitars)


if __name__ == "__main__":
    main()
