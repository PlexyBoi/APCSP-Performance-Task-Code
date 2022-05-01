list1 = [16, 8, 24, 6, 10]
list2 = [2, 8, 4, 5, 3]
num_problems = len(list1)

def calculate(type):
    score = 0
    for i in range(num_problems):
        print(list1[i], end = " ")
        if(type == "A"):
            print(" + ", end= " ")
            correct = list1[i] + list2[i]
        else:
            print(" - ", end = " ")
            correct = list1[i] - list2[i]
        print(list2[i])
        answer = int(input("Enter your answer:"))
        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print("Good try!")
        print()
    return score

print("Welcome to my Math Quiz!")
type= input("Please select (A)ddition or (S)ubtraction:")
score=calculate(type) * 100 / num_problems

print("Your score on the test: " + str(score) + "%")
