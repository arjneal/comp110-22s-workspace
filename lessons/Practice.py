name: str = (input("What is your name?"))

print("Hello, " + name)

your_age: str = (input("How old are you?"))

print(name + " is " + your_age + " years old.")

personal_gpa: float = float(input("What is your current GPA?"))
average_gpa: float = 3.276
if personal_gpa >= float(3.9):
    print("you have an incredibly high GPA")
else:
    if personal_gpa >= float(3.75):
        print("Your GPA is in the top 13 percent.")
    else:
        if personal_gpa > float(3.5):
            print("You have an above average gpa for UNC-CH")
        else:
            if personal_gpa >= float(3.276): 
                print("you are within the normal GPA bounds for the university")
            else:
                if personal_gpa <= float(2.5):
                    print("You may want to consider transferring to another university.")
