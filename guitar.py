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

    def __lt__(self, other):
        """Implement less than comparison based on year."""
        return self.year < other.year


def load_guitars(filename):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display guitars in the list."""
    for index, guitar in enumerate(guitars, 1):
        print(f"{index}. {guitar}")


def add_guitar(guitars):
    """Add a new guitar to the list."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    """Save guitars to a file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    """Main function."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("All guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Add a new guitar
    add_guitar(guitars)

    # Save guitars to file
    save_guitars(filename, guitars)


if __name__ == "__main__":
    main()
