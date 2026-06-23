def calculate_grade(average):
    if average >= 90:
        return "A", "Excellent! Outstanding performance! 🌟"
    elif average >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif average >= 70:
        return "C", "Good Job! Keep improving! 😊"
    elif average >= 60:
        return "D", "You Passed! Put in a little more effort. 📚"
    else:
        return "F", "Don't give up! Success comes with practice. 💪"


def performance_status(average):
    if average >= 90:
        return "Outstanding"
    elif average >= 80:
        return "Very Good"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


print("=" * 65)
print("               STUDENT GRADE CALCULATOR")
print("=" * 65)

student_name = input("Enter Student Name: ").strip()

subjects = [
    "Mathematics",
    "Science",
    "English",
    "Social Science",
    "Computer Science"
]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter Marks for {subject} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("❌ Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Invalid input! Please enter numeric marks.")

total = sum(marks)
average = total / len(marks)

grade, message = calculate_grade(average)
status = performance_status(average)

print("\n" + "=" * 65)
print(f"                 RESULT FOR {student_name.upper()}")
print("=" * 65)

for i in range(len(subjects)):
    print(f"{subjects[i]:18}: {marks[i]:.0f}")

print("-" * 65)
print(f"Total Marks       : {total:.0f}/500")
print(f"Average Marks     : {average:.2f}/100")
print(f"Grade             : {grade}")
print(f"Performance       : {status}")
print(f"Feedback          : {message}")

print("\n" + "=" * 65)
print("                   PERFORMANCE SUMMARY")
print("=" * 65)

print(f"Hello {student_name},")
print(f"You scored {total:.0f} marks out of 500.")
print(f"Your average score is {average:.2f}.")
print(f"You secured Grade {grade}.")
print(f"Your overall performance is classified as '{status}'.")

if grade == "A":
    print("You have demonstrated exceptional academic performance.")
elif grade == "B":
    print("You have performed very well. Keep aiming higher.")
elif grade == "C":
    print("You are doing well. Consistent practice will help you improve.")
elif grade == "D":
    print("You passed successfully. Focus on strengthening weak areas.")
else:
    print("Do not lose confidence. Regular study and practice will help you succeed.")

print("\n🎯 Keep learning, keep growing, and strive for excellence!")
print("=" * 65)
print("             THANK YOU FOR USING THE PROGRAM")
print("=" * 65)