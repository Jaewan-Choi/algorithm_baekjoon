c = int(input())
test_list = []
n = 0
while n < c:
    test_list.append(input())
    n += 1

for test in test_list:
    student_num = int(test.split()[0])
    student_score_list = test.split()[1:]
    
    total_score = 0
    for student_score in student_score_list:
        total_score += int(student_score)
    
    avg_score =  total_score / student_num
    
    high_score_student = 0
    for student_score in student_score_list:
        if int(student_score) > avg_score:
            high_score_student += 1

    rate_high_score_student = high_score_student / student_num * 100

    print('%.3f%%' % rate_high_score_student)