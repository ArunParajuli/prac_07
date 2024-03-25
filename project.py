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
