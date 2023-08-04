import numpy as np
student_scores = np.array([[80, 85, 70, 90],[75, 88, 92, 78],[90, 82, 87, 95],[72, 67, 73, 84],[69, 77, 89, 93],[97, 99, 98, 91]])
average_scores = np.mean(student_scores, axis=0)
highest_average_subject_index = np.argmax(average_scores)
subjects = ['Math', 'Science', 'English', 'History']
subject_with_highest_average_score = subjects[highest_average_subject_index]
print("Average Scores for each subject:")
for subject, average_score in zip(subjects, average_scores):
    print(f"{subject}: {average_score}")
print(f"\nThe subject with the highest average score is: {subject_with_highest_average_score}")
