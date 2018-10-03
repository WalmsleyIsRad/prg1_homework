homework_to_do = []
homework_due_dates = []

test_quizzes = []
tests_quiz_dates = []

while(True):
    print("Welcome to Saint John's Northwestern Military Academy!")
    print("This is your Academic Planner Program that will help you keep your assignments in line")
    print("Please enter in the either the number 1, 2, or 3")
    
    number = int(input("number"))

    if(number == 1):
        homework = input("Describe the homework")
        homework_to_do.append(homework)
        hdd = input("When is it due?")
        homework_due_dates.append(hdd)
    if(number == 2):
        qat = input("Describe the quiz or test")
        test_quizzes.append(qat)
        qatdd = input("When will the test or quiz be taken")
        tests_quiz_dates.append(qatdd)
    if(number == 3):
        print("Here is all the homework you have completed")
        print(homework_to_do)
        print(homework_due_dates)
        print("Here are all the tests/quizzes you have taken")
        print(test_quizzes)
        print(tests_quiz_dates)
        
        

    

        


