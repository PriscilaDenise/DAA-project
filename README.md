

```markdown
# Task Scheduler with Optimization and Reminders

## Project Overview

This project demonstrates the use of dynamic programming and scheduling algorithms to optimize task management. The **Task Scheduler** program allows users to input tasks, optimize their schedule based on task priorities, and receive notifications about upcoming or missed tasks. It also generates a Gantt chart to visually represent the optimized task schedule.

The task scheduling optimization uses a dynamic programming approach to find the maximum priority sum of non-overlapping tasks. This project is ideal for demonstrating real-world applications of algorithms and data structures in managing tasks efficiently.

## Key Concepts Covered

- **Dynamic Programming**: Used to select the maximum priority set of non-overlapping tasks.
- **Binary Search**: Used to efficiently find the last non-overlapping task, improving the dynamic programming approach.
- **Task Scheduling**: A real-world application of scheduling algorithms.
- **Visualization**: Creating Gantt charts to visualize the task schedule over time.

## Project Features

- **Task Creation**: Users can enter tasks with attributes like name, type (personal/academic), start time, end time, priority, and deadline.
- **Task Optimization**: The program uses dynamic programming to find an optimal schedule by selecting tasks with the highest priority that don't overlap.
- **Task Notifications**: The program will notify the user of upcoming tasks within the next hour or missed tasks.
- **Gantt Chart Visualization**: The program generates a Gantt chart to visualize the optimized task schedule.

## Requirements

To run the program, make sure Python 3.x is installed on your machine, along with the following libraries:

- `matplotlib`: For generating the Gantt chart.
- `subprocess`: For sending notifications.
- `bisect`: For binary search functionality.
- `datetime`: For handling time-based operations.

You can install the necessary libraries by running:

```bash
pip install matplotlib
```

## Program Flow

1. **Task Input**: Users are prompted to input details for each task, including name, type, start time, end time, priority, and deadline.
2. **Task Optimization**: Once all tasks are entered, the program optimizes the schedule to maximize the total priority of non-overlapping tasks using dynamic programming.
3. **Notifications**: The program checks for tasks that are about to start or have already ended, sending notifications to the user accordingly.
4. **Gantt Chart**: After optimization, a Gantt chart is displayed, showing the optimized task schedule over time.

## Example Usage

```bash
Welcome to the Task Scheduler!
Enter tasks to create a Gantt chart and receive reminders.

Enter details for Task 1:
Task Name: Study
Task Type (personal/academic): academic
Start Time (e.g., 1 for 1:00): 9
End Time (e.g., 5 for 5:00): 12
Priority (e.g., 10): 10
Deadline (e.g., 5 for day 5): 5
Do you want to add another task? (yes/no): yes

Enter details for Task 2:
Task Name: Exercise
Task Type (personal/academic): personal
Start Time (e.g., 1 for 1:00): 13
End Time (e.g., 5 for 5:00): 14
Priority (e.g., 10): 7
Deadline (e.g., 5 for day 5): 5
Do you want to add another task? (yes/no): no

Optimizing schedule...
Maximum Priority: 17
Selected Tasks for Optimal Schedule:
- Study (Priority: 10, Start: 9, End: 12)
- Exercise (Priority: 7, Start: 13, End: 14)

Checking for reminders and missed tasks...
Generating Gantt Chart...
```

## Learning Objectives

- **Dynamic Programming for Task Scheduling**: Understand how dynamic programming can be used to optimize task selection based on priorities and time constraints.
- **Binary Search Application**: Learn how binary search can be used to solve the problem of finding the last non-overlapping task efficiently.
- **Visualization with Gantt Charts**: Create visual representations of task schedules to help in real-world scheduling scenarios.
- **Notification System**: Implement a simple reminder and notification system for task management.

## Running the Program

To run the program, use the following steps:

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the program:

```bash
python task_scheduler.py
```

4. Follow the on-screen prompts to enter task details and view the optimized schedule and notifications.

## Notes

- The notification system uses `osascript` for notifications, which is macOS-specific. If you're using a different operating system, you may need to modify the notification system.
- The Gantt chart provides a simple visual representation of the task schedule and can be customized further if needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

This version focuses on the learning objectives and how the project relates to algorithmic concepts, making it suitable for class presentations and assignments.
