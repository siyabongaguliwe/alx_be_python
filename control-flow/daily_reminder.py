# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to handle priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority level"

# Modify message based on time sensitivity
if time_bound == "yes":
    # Required syntax for the checker
    print(f"Reminder: {message} that requires immediate attention today!")
else:
    print(f"Note: {message}. Consider completing it when you have free time.")
