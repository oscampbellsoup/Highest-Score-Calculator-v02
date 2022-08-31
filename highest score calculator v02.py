# Ask for list of student scores as separate string values.
student_scores = input("Input a list of student scores ").split()
# Determine a range of the values stored in student_scores variable.
for n in range(0, len(student_scores)):
# Change list values from str to int.
  student_scores[n] = int(student_scores[n])
# Print a list of the scores inputted by the user to confirm their trust in the outcome.
print(student_scores)
# Max_score variable is created. Set at 0 until scores among the list are compared in value.
max_score = 0
# Create a loop and assign a new variable.
for score in student_scores:
# Compare the value of two scores.
    if score > max_score:
# If score is greater than max_score, score becomes new max_score.
        max_score = score
# Output message with max_score among student_scores.
print(f"The highest score in the class is: {max_score}")