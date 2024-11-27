
### Group Members:
- Muwanguzi Priscila Denise   M23B23/010
- Mawejje JohnPaul                M23B23/049
- Nicole Johnson                     S23B23/020

## Overview
The **Task Scheduler Program** is designed to help users manage their tasks efficiently by allowing them to create, optimize, and visualize a schedule based on task priorities and time slots. The program uses dynamic programming to select an optimal set of non-overlapping tasks. It also includes a notification system that alerts users about upcoming tasks and missed tasks, as well as a Gantt chart for visualizing the task schedule.

## Features
- **Dynamic Task Scheduling**: Automatically selects an optimal set of non-overlapping tasks based on priority using dynamic programming.
- **Notifications**: Alerts for upcoming tasks (within the next hour) and missed tasks.
- **Task Visualization**: Generates a Gantt chart to visualize the task schedule.
- **User-Friendly**: Allows users to input and manage tasks interactively.

## Requirements
- **Python 3.x**
- **Libraries**:
  - `matplotlib` - For generating Gantt charts.
  - `datetime` - For handling and manipulating date and time.
  - `subprocess` - To generate system notifications on macOS.
  - `bisect` - To perform binary search on sorted lists.

To install the required libraries, use the following:
```bash
pip install matplotlib
```

## Usage

1. **Run the Program**:  
   Start the program by running the script:
   ```bash
   python task_scheduler.py
   ```

2. **Input Task Details**:  
   The program will prompt you to input the details for each task:
   - **Task Name**: Name of the task (e.g., "Math Homework").
   - **Task Type**: Type of task, either `personal` or `academic`.
   - **Start Time**: The starting hour of the task (e.g., 9 for 9:00 AM).
   - **End Time**: The ending hour of the task (e.g., 11 for 11:00 AM).
   - **Priority**: Task priority (integer value).
   - **Deadline**: Task deadline (day of the month).

3. **Task Optimization**:  
   After entering the task details, the program will automatically optimize the schedule to select the maximum priority set of non-overlapping tasks using dynamic programming.

4. **Notifications**:  
   The program will check for upcoming tasks (tasks starting within an hour) and missed tasks (tasks that have already ended). Notifications will be displayed for these tasks.

5. **Gantt Chart**:  
   The program will generate and display a Gantt chart representing the selected tasks with bars indicating the start and end times of each task.

6. **Add More Tasks**:  
   After entering a task, you can choose to add more tasks. The program will continue prompting you until you decide to stop.

## Example
**User Input:**
```plaintext
Task Name: "Math Homework"
Task Type: "Academic"
Start Time: 9 (9:00 AM)
End Time: 11 (11:00 AM)
Priority: 10
Deadline: 5
```

**Program Output:**
- **Optimal Schedule**: 
  - Maximum Priority: 20
  - Selected Tasks:
    - "Math Homework" (Priority: 10, Start: 9:00 AM, End: 11:00 AM)
- **Notifications**: Alerts for upcoming and missed tasks.
- **Gantt Chart**: A chart displaying the task "Math Homework" from 9:00 AM to 11:00 AM.

## Error Handling
- If invalid data is entered (e.g., non-numeric values for time or priority), the program will prompt the user to re-enter the correct information.
- If the system does not support notifications (e.g., non-macOS systems), the program will handle the exception gracefully and display an error message.

## Future Improvements
- Support for multiple task deadlines (not just day-based).
- Add functionality to allow users to modify or delete tasks.
- Implement notification system for non-macOS platforms (e.g., Windows, Linux).
- Enhance the user interface for better task management.

## Contributing
Feel free to fork the repository and contribute by submitting a pull request. Suggestions and bug reports are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

