# Prompt for task description
task = input("Enter your task: ")

# Prompt for task priority
priority = input('Priority (high/medium/low): ')

# Prompt for time sensitivity
time_bound = input('Is it time-bound?(yes/no): ')

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print(f"Please set if the task is time-bound")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print(f"Please set if the task is time-bound")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print(f"Please set if the task is time-bound")
