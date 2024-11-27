import datetime
import matplotlib.pyplot as plt
import subprocess
from bisect import bisect_right


# Task class
class Task:
    def __init__(self, task_id, name, task_type, start_time, end_time, priority, deadline):
        self.task_id = task_id
        self.name = name
        self.task_type = task_type  # "personal" or "academic"
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        self.deadline = deadline


# Notification system using osascript
import subprocess
def notify(title, message):
    try:
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}" with title "{title}"'
        ])
    except Exception as e:
        print(f"Notification Error: {e}")


# Binary search for the last non-overlapping task
def find_last_non_overlapping(tasks, index):
    """
    Use binary search to find the last task that doesn't overlap with the current task.
    Tasks must be sorted by end_time.
    """
    end_times = [task.end_time for task in tasks]
    pos = bisect_right(end_times, tasks[index].start_time) - 1
    return pos if pos >= 0 else -1


# Dynamic programming for task optimization
def optimize_schedule(tasks):
    """
    Use dynamic programming to find the maximum priority sum of non-overlapping tasks.
    Returns the maximum priority and the list of selected tasks.
    """
    tasks.sort(key=lambda x: x.end_time)
    n = len(tasks)
    dp = [0] * n  # dp[i] stores the maximum priority sum up to task i
    selected_tasks = [None] * n  # To reconstruct the optimal schedule

    dp[0] = tasks[0].priority
    selected_tasks[0] = [tasks[0]]

    for i in range(1, n):
        exclude = dp[i - 1]
        last_compatible = find_last_non_overlapping(tasks, i)
        include = tasks[i].priority
        if last_compatible != -1:
            include += dp[last_compatible]

        if include > exclude:
            dp[i] = include
            selected_tasks[i] = (selected_tasks[last_compatible] if last_compatible != -1 else []) + [tasks[i]]
        else:
            dp[i] = exclude
            selected_tasks[i] = selected_tasks[i - 1]

    return dp[-1], selected_tasks[-1]


# Visualization (Gantt Chart)
def plot_gantt_chart(tasks):
    fig, ax = plt.subplots()
    for i, task in enumerate(tasks):
        color = 'tab:blue' if task.task_type == "academic" else 'tab:green'
        ax.broken_barh([(task.start_time, task.end_time - task.start_time)], (i - 0.4, 0.8), facecolors=color)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task.name for task in tasks])
    ax.set_xlabel('Time (Hours)')
    ax.set_title('Task Schedule')
    plt.show()


# Reminder system
def check_notifications(tasks):
    current_time = datetime.datetime.now().time()  # Get the current time

    for task in tasks:
        task_start = datetime.time(hour=task.start_time)  # Convert start time to datetime.time
        task_end = datetime.time(hour=task.end_time)      # Convert end time to datetime.time

        # Check for upcoming tasks (within 1 hour)
        if task_start > current_time and (datetime.datetime.combine(datetime.date.today(), task_start) - datetime.datetime.now()).seconds <= 3600:
            print(f"Reminder: Upcoming task '{task.name}' starting at {task.start_time}:00.")
            notify("Upcoming Task", f"Task '{task.name}' starts at {task.start_time}:00.")

        # Check for missed tasks
        elif task_end < current_time:
            print(f"Missed Task: You missed '{task.name}', which ended at {task.end_time}:00.")
            notify("Missed Task", f"Task '{task.name}' ended at {task.end_time}:00.")


# Main function
def main():
    print("Welcome to the Task Scheduler!")
    print("Enter tasks to create a Gantt chart and receive reminders.")

    tasks = []
    task_id = 1

    while True:
        print(f"\nEnter details for Task {task_id}:")
        name = input("Task Name: ")
        task_type = input("Task Type (personal/academic): ").lower()
        start_time = int(input("Start Time (e.g., 1 for 1:00): "))
        end_time = int(input("End Time (e.g., 5 for 5:00): "))
        priority = int(input("Priority (e.g., 10): "))
        deadline = int(input("Deadline (e.g., 5 for day 5): "))

        # Add task to the list
        tasks.append(Task(task_id, name, task_type, start_time, end_time, priority, deadline))
        task_id += 1

        another = input("Do you want to add another task? (yes/no): ").lower()
        if another != "yes":
            break

    # Optimize the schedule using dynamic programming
    print("\nOptimizing schedule...")
    max_priority, selected_tasks = optimize_schedule(tasks)

    print(f"\nMaximum Priority: {max_priority}")
    print("Selected Tasks for Optimal Schedule:")
    for task in selected_tasks:
        print(f"- {task.name} (Priority: {task.priority}, Start: {task.start_time}, End: {task.end_time})")

    # Check reminders and missed tasks
    print("\nChecking for reminders and missed tasks...")
    check_notifications(tasks)

    # Generate Gantt Chart
    print("\nGenerating Gantt Chart...")
    plot_gantt_chart(selected_tasks)


# Run the program
if __name__ == "__main__":
    main()
