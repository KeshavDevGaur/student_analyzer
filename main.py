import numpy as np


# 1. Data

marks = np.array([
    [85, 78, 92],
    [70, 88, 80],
    [60, 65, 70],
    [90, 92, 95],
    [75, 85, 82]
])

students = np.array(["A", "B", "C", "D", "E"])
subjects = np.array(["Math", "Science", "English"])


# 2. Student-wise Analysis

total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)
percentage = (total / (marks.shape[1] * 100)) * 100


# 3. Subject-wise Analysis

subject_avg = np.mean(marks, axis=0)


# 4. Ranking

rank_indices = np.argsort(-total)


# 5. Grading + Performance Label

grades = []
performance = []

for avg in average:
    if avg >= 85:
        grades.append("A")
        performance.append("Excellent")
    elif avg >= 70:
        grades.append("B")
        performance.append("Good")
    elif avg >= 50:
        grades.append("C")
        performance.append("Average")
    else:
        grades.append("F")
        performance.append("Poor")


# 6. Pass/Fail + Failed Subjects

pass_fail = np.all(marks >= 40, axis=1)

failed_subjects = []
for i in range(len(students)):
    failed = subjects[marks[i] < 40]
    failed_subjects.append(failed)


# 7. Topper & Weakest

topper = students[np.argmax(total)]
weakest = students[np.argmin(total)]


# 8. Subject Toppers

subject_toppers = students[np.argmax(marks, axis=0)]


# 9. Class Statistics

class_avg = np.mean(total)
highest_score = np.max(total)
lowest_score = np.min(total)


# 10. DISPLAY OUTPUT

print("\n===== STUDENT REPORT =====")

for i in range(len(students)):
    print(f"\nStudent: {students[i]}")
    print(f"Marks: {marks[i]}")
    print(f"Total: {total[i]}")
    print(f"Average: {average[i]:.2f}")
    print(f"Percentage: {percentage[i]:.2f}%")
    print(f"Grade: {grades[i]} ({performance[i]})")
    
    status = "Pass" if pass_fail[i] else "Fail"
    print(f"Status: {status}")
    
    if not pass_fail[i]:
        print(f"Failed Subjects: {failed_subjects[i]}")


# Ranking

print("\n===== RANKING =====")
for i, idx in enumerate(rank_indices):
    print(f"Rank {i+1}: {students[idx]} (Total: {total[idx]})")


# Subject-wise

print("\n===== SUBJECT ANALYSIS =====")
for i in range(len(subjects)):
    print(f"{subjects[i]} Avg: {subject_avg[i]:.2f}, Topper: {subject_toppers[i]}")

#
# Class Summary

print("\n===== CLASS SUMMARY =====")
print(f"Class Average: {class_avg:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Topper: {topper}")
print(f"Weakest: {weakest}")
