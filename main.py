import re

nama = input("Enter your name : ")
number_task = input("Enter the number of tasks you want to do : ")
all_task = []
total_working = 0
for number in range(1,int(number_task)+1):
    print("-"*50)
    print("Please choose your tasks:")
    print("-"*50)
    print("LG : Login")
    print("RG : Register")
    print("US : User")
    print("EMP : Employee")
    print("TS : TimeSheets")
    task_type = {"LG" : "Login",
                "RG" : "Register",
                "US" : "User",
                "EMP" : "Employee",
                "TS" : "TimeSheets",
                }
    is_valid = False
    while not is_valid:
        task = input(f"Choose a task {number} : ")
        if re.match(r"LG|RG|US|EMP|TS",task):
            float_working_hours = float(input("Enter your working hour for login (in float, e.g 1.5 for 1 hour 30 minutes) : "))
            is_valid = True
        else:
            print("Input invalid, please try again!.")
    days, hours = divmod(float_working_hours,24)
    hours_time, minutes = divmod(hours * 60, 60)  # split to hours and seconds
    minutes, seconds= divmod(minutes * 60, 60)
    if days > 0:
        working_hours = "{} days( {:02.0f}:{:02.0f}:{:02.0f})".format(days,hours_time, minutes,seconds)
    else:
        working_hours = "({:02.0f}:{:02.0f}:{:02.0f})".format(hours_time, minutes,seconds)
    all_task.append(f"Task : {task_type[task]}, Working Hours : {working_hours}")
    total_working += float_working_hours
print(f"Summary of Tasks For {nama}")
for tasks in all_task:
    print(tasks)
total_days, total_hours = divmod(total_working,24)
total_hours, total_minutes = divmod(total_hours * 60, 60) 
total_minutes, total_seconds= divmod(total_minutes * 60, 60)
print(f"Total Working Hours {total_working}")

