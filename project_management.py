"""
CP1404 - Practical 7
Name: <Arun Parajuli>
"""
import datetime

class Project:
    """Represents a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Return a string representation of the Project."""
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percent}%"

    def is_completed(self):
        """Check if the project is completed."""
        return self.completion_percent >= 100

    def is_started(self, date):
        """Check if the project has started."""
        project_start_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        return project_start_date <= date

    def update_completion_percent(self, new_completion_percent):
        """Update the completion percent of the project."""
        self.completion_percent = new_completion_percent

    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion_percent = parts
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percent)))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percent}\n")


def display_projects(incomplete_projects, completed_projects):
    """Display incomplete and completed projects."""
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(" ", project)
    print("Completed projects:")
    for project in completed_projects:
        print(" ", project)


def filter_projects_by_date(projects, filter_date):
    """Filter projects that start after the given date."""
    filtered_projects = [project for project in projects if project.is_started(filter_date)]
    sorted_filtered_projects = sorted(filtered_projects, key=lambda x: datetime.datetime.strptime(x.start_date, "%d/%m/%Y"))
    return sorted_filtered_projects


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percent = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percent))


def update_project(projects):
    """Update completion percent and priority of a project."""
    print("Choose a project to update:")
    for index, project in enumerate(projects):
        print(index, project)
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_completion_percent = input("New Percentage: ")
    if new_completion_percent:
        project.update_completion_percent(int(new_completion_percent))
    new_priority = input("New Priority: ")
    if new_priority:
        project.update_priority(int(new_priority))


def main():
    """Main function."""
    filename = "projects.txt"
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            incomplete_projects = [project for project in projects if not project.is_completed()]
            completed_projects = [project for project in projects if project.is_completed()]
            display_projects(incomplete_projects, completed_projects)
        elif choice == 'f':
            filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yyyy): "), "%d/%m/%Y").date()
            filtered_projects = filter_projects_by_date(projects, filter_date)
            for project in filtered_projects:
                print(" ", project)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects("projects.txt", projects)
                print(f"Saved {len(projects)} projects to projects.txt")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
