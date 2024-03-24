import sys
import decimal

def count_score(grade):
    score = 0.0
    if grade.startswith('A'):
        score += 4
    elif grade.startswith('B'):
        score += 3
    elif grade.startswith('C'):
        score += 2
    elif grade.startswith('D'):
        score += 1
    
    if grade.endswith('+'):
        score += 0.3
    elif grade.endswith('-'):
        score -= 0.3
    
    return score

n = int(sys.stdin.readline())

total_credit = 0
total_score = 0
for i in range(n):
    lecture, credit, grade = sys.stdin.readline().rstrip('\n').split()
    total_credit += int(credit)
    total_score += int(credit) * count_score(grade)
result = decimal.Decimal(total_score) / decimal.Decimal(total_credit)

print(round(result, 2))