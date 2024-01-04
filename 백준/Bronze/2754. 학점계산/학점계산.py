g_dic = { "A":4, "B":3, "C":2, "D":1, "F":0 }
grade = input()

score = g_dic.get(grade[0])
if (grade != "F"):
    if (grade[1] == "+"):
        score += 0.3
    elif (grade[1] == "-"):
        score -= 0.3
        
print(float(score))