# daily_reminder.py

# Prompt for the task
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to handle different priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Use if statement to modify the reminder based on time sensitivity
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Print the final customized reminder
print(reminder)


