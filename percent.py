from decimal import Decimal


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


query_scores = student_marks[query_name]
total_scores = sum(query_scores)
Convert the floats to decimals and average the scores: avg
avg = Decimal(total_scores/3)
Print the mean of the scores, correct to two decimals
print(round(avg,2))
