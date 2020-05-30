marks = int(input("Input Your Marks In Programming: "))


def your_grade(grade):
    print(f"You Got: {grade}")


# if marks >= 80:
#     your_grade("A+")
# elif 80 >= marks >= 70:
#     your_grade('A')
# elif 70 > marks >= 60:
#     your_grade("A-")
# elif marks >= 33:
#     your_grade('Passed')
# else:
#     your_grade("Fail")

if marks > 80 or marks < 10:
    print("You are GOOD Or BAD")
    if marks > 80:
        print("You Are GOOD")
    else:
        print("You Are BAD")
else:
    print("You are OK !!")

print("Finished")
