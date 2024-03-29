if __name__ == '__main__':
    n = int(input()) # Number of student input
    student_marks = {} # Empty Dictionary 
    for _ in range(n): # Creates a for 
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average_query = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f'{average_query:.2f}')

    # student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}