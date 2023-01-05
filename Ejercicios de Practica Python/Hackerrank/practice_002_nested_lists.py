if __name__ == '__main__':
    student_lst =[]
    for _ in range(int(input())):
        l1 = []
        l1.append(input()), l1.append(float(input()))
        student_lst.append(l1)

    lowest_grade = min([grade for name, grade in student_lst])
    second_lowest_grade = min([grade for name, grade in student_lst if grade != lowest_grade])
    student_second_lowest_grade = sorted([name for name, grade in student_lst if grade == second_lowest_grade])

    for i in student_second_lowest_grade:
        print(i)



    # import heapq

    # student_list_no_max = student_lst
    # print(heapq.nlargest(2, student_list_no_max, key=lambda x: x[1]))
    # # student_list_no_max.remove(max(student_list_no_max, key=lambda x: x[1]))

    # print(student_list_no_max)
    
    
    # for i in student_lst:
    #     if max(student_lst, key=lambda x: x[1]):
    #         continue
    #     elif 
    #     print(student_lst)

    # grades = set([student_lst[i][1] for i in student_lst]).sorted()

    # for i in student_lst:
    #     if student_lst[i][1] == grades[1]:
    #         print(student_lst[i][1])
            
# if student_lst[1][1] == student_lst[2][1]:
#     print(student_lst[1][0])
#     print(student_lst[2][0])
# else:
#     print(student_lst[1][0])
