# daily_reminder.py

# Prompt the user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine the base message using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Adjust the reminder based on time sensitivity
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Print the final customized reminder
print(f"\nReminder: {reminder}")
