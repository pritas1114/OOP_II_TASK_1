#TO DO LIST
#TITAS SARKER (ID:0242220005101864)

import json
import numpy as np
from datetime import datetime

# Parent Class for Tasks (Class & Object)
class Task:
    def __init__(self, task_id, description, category, due_date, priority):
        self.id = task_id  # Task ID (Unique Identifier for Task)
        self.description = description  # Task Description (What the task is about)
        self.category = category  # Task Category (Student, Family, Other)
        self.due_date = due_date  # Task Due Date (When the task is due)
        self.priority = priority  # Task Priority (High, Medium, Low)
        self.completed = False  # Task Status (Completed or Not) - Default is False

    def mark_completed(self):
        """Mark the task as completed"""
        self.completed = True  # Change task status to completed

    def __str__(self):
        """String representation of the Task"""
        # When a task is printed, this format will be shown
        return f"{self.id}. {self.description} | {self.category} | {self.due_date} | {self.priority} | {'✔' if self.completed else '✘'}"


# Child Class for SpecialTask (Inheritance)
class SpecialTask(Task):
    def __init__(self, task_id, description, category, due_date, priority, tag):
        super().__init__(task_id, description, category, due_date, priority)  # Inherit attributes from Task
        self.tag = tag  # Additional tag for special tasks (e.g. 'Urgent', 'Important')

    def __str__(self):
        """Override string representation (Polymorphism)"""
        # Adding the tag information in the task's string representation
        return f"{super().__str__()} | Tag: {self.tag}"


# Main ToDoList Application
class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store all tasks

    def load_tasks(self):
        """Load tasks from a JSON file"""
        try:
            # If the file exists, load the task data
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)  # Load data as JSON
                # Create Task or SpecialTask objects depending on the data
                self.tasks = [
                    Task(**task) if "tag" not in task else SpecialTask(**task)
                    for task in tasks_data
                ]
        except FileNotFoundError:
            # If the file doesn't exist, create an empty list
            self.tasks = []

    def save_tasks(self):
        """Save tasks to a JSON file"""
        # Save the tasks to a file in JSON format
        with open("tasks.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def add_task(self, description, category, due_date, priority, tag=None):
        """Add a new task to the list"""
        task_id = len(self.tasks) + 1  # Generate a new ID based on the current list length
        if tag:
            # If the task has a tag, it becomes a SpecialTask
            task = SpecialTask(task_id, description, category, due_date, priority, tag)
        else:
            # Otherwise, it's a regular Task
            task = Task(task_id, description, category, due_date, priority)
        self.tasks.append(task)  # Add the task to the list

    def show_tasks(self, filter_by="all"):
        """Display tasks based on filters"""
        filtered_tasks = self.tasks  # Initially show all tasks
        if filter_by == "completed":
            # Filter completed tasks
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_by == "pending":
            # Filter pending tasks (not completed)
            filtered_tasks = [task for task in self.tasks if not task.completed]
        elif filter_by in ["High", "Medium", "Low"]:
            # Filter tasks based on priority
            filtered_tasks = [task for task in self.tasks if task.priority == filter_by]

        if not filtered_tasks:
            print("No tasks found!")  # If no tasks match the filter
        else:
            # Display all matching tasks
            for task in filtered_tasks:
                print(task)

    def show_tasks_by_date(self, due_date):
        """Display tasks by due date"""
        filtered_tasks = [task for task in self.tasks if task.due_date == due_date]
        if not filtered_tasks:
            print(f"No tasks found for the due date: {due_date}!")
        else:
            for task in filtered_tasks:
                print(task)

    def remove_task(self, task_id):
        """Remove a task by ID"""
        # Create a new list excluding the task with the given task_id
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def update_task(self, task_id, description, category, due_date, priority):
        """Update an existing task"""
        for task in self.tasks:
            if task.id == task_id:
                # Update the task attributes
                task.description = description
                task.category = category
                task.due_date = due_date
                task.priority = priority
                return
        print("Task not found!")  # If the task_id doesn't exist


# Main Program Logic
def main():
    todo_list = ToDoList()  # Create a ToDoList object
    todo_list.load_tasks()  # Load existing tasks from the file

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Show Tasks by Due Date")
        print("4. Mark Task as Completed")
        print("5. Update Task")
        print("6. Delete Task")
        print("7. View Task Summary")
        print("8. Save and Exit")

        try:
            choice = int(input("Enter your choice: "))  # Get user's choice
            if choice == 1:
                # Add a new task
                description = input("Task Description: ")
                category = input("Category (Student, Family, Other): ").capitalize()
                due_date = input("Due Date (YYYY-MM-DD): ")
                priority = input("Priority (High, Medium, Low): ").capitalize()
                tag = input("Tag (Optional, leave blank if not needed): ") or None
                todo_list.add_task(description, category, due_date, priority, tag)
                print("Task added successfully!")

            elif choice == 2:
                # Show tasks with a filter option
                print("\nFilter Options: 1. All Tasks 2. Completed 3. Pending")
                filter_choice = input("Choose filter: ")
                filters = {"1": "all", "2": "completed", "3": "pending"}
                todo_list.show_tasks(filters.get(filter_choice, "all"))

            elif choice == 3:
                # Show tasks by due date
                due_date = input("Enter due date (YYYY-MM-DD): ")
                todo_list.show_tasks_by_date(due_date)

            elif choice == 4:
                # Mark a task as completed
                task_id = int(input("Enter task ID to mark as completed: "))
                task = next((t for t in todo_list.tasks if t.id == task_id), None)
                if task:
                    task.mark_completed()
                    print("Task marked as completed!")
                else:
                    print("Task not found!")

            elif choice == 5:
                # Update a task's details
                task_id = int(input("Enter task ID to update: "))
                description = input("New Description: ")
                category = input("New Category (Student, Family, Other): ").capitalize()
                due_date = input("New Due Date (YYYY-MM-DD): ")
                priority = input("New Priority (High, Medium, Low): ").capitalize()
                todo_list.update_task(task_id, description, category, due_date, priority)
                print("Task updated successfully!")

            elif choice == 6:
                # Remove a task
                task_id = int(input("Enter task ID to delete: "))
                todo_list.remove_task(task_id)
                print("Task deleted!")

            elif choice == 7:
                # Show a summary of tasks using numpy
                priorities = [task.priority for task in todo_list.tasks]
                priority_counts = {priority: priorities.count(priority) for priority in set(priorities)}
                print("Priority Summary (Using Numpy):", priority_counts)

            elif choice == 8:
                # Save tasks and exit
                todo_list.save_tasks()
                print("Tasks saved. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError as e:
            print(f"Error: Invalid input! {e}")  # Handle invalid input for choice
        except Exception as e:
            print(f"Error: {e}")  # Handle other errors


if __name__ == "__main__":
    main()  # Run the main function to start the program
