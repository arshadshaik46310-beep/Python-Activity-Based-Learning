n = int(input("Enter number of subjects: "))
pass_mark = 40
failed = []
for i in range(n):
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks: "))
    if marks < pass_mark:
        failed.append(subject)
attendance = float(input("Enter attendance percentage: "))
prerequisites = input(
    "Are all prerequisites completed? (yes/no): "
).lower()
print("\n--- Academic Progression Report ---")
if failed:
    print("Failed Subjects:", ", ".join(failed))
else:
    print("All subjects passed.")
if attendance < 75:
    print("Outstanding Requirement: Attendance below 75%")
if prerequisites != "yes":
    print("Outstanding Requirement: Complete prerequisites")
if not failed and attendance >= 75 and prerequisites == "yes":
    print("Progression Status: Eligible")
else:
    print("Progression Status: Not Eligible")

