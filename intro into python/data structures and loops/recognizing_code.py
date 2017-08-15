def check_one(my_answers,answers):
    results = []
    i = 0
    while i < len(my_answers):
        if my_answers[i] == answers[i]:
            results.append(True)
        else:
            results.append(False)
        i = i + 1
    
    return (results)    





def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = check_one(my_answers,answers)
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
        
print (check_answers([1,2,3,4,5],[1,3,3,6,5]))        