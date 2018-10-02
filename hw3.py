while(True):
    print("Welcome to Saint John's Northwestern Military Academy!")
    print("This is your Academic Planner Program that will help you keep your assignments in line")
    print("Please enter in the either the number 1, 2, or 3")
    
    number = int(input("number"))

    if(number == 1):
        hwtd = str(input("Describe the homework"))
        hdd = str(input("When is it due?"))
        
        homework = (hwtd+hdd)
    if(number == 2):
        qot = str(input("Describe the quiz or test"))
        qotdd = str(input("When will the test or quiz be taken"))
        tests=(qot+qotdd)
            
        homework_and_tests=[
                homework,
                tests
        ]
    if(number == 3):
        print("Here are all the assignments, tests, and quizzes that you have entered")
        print(homework_and_tests)
