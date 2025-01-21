student_scores = [180, 124, 165, 173, 189, 169, 146]

#Write a program to print total scores

#Method 1
total_score = sum(student_scores)
print(total_score)

#Method 2
total = 0
for score in student_scores:
    total += score
print(total)

#Write a program to find maximum score

#Method 1
max_score = max(student_scores)
print(max_score)

#Method 2
maximum = student_scores[0]
for score in student_scores:
    if score > maximum:
        maximum = score
print(maximum)