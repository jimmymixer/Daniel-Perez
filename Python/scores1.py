import random
def grades():
    num_scores= 12

    for scores in range(1, num_scores):
        random_num= random.random()
        random_num= random.randint(60,100)

        if (random_num < 70):
            print "Score: ", random_num, "Your grade is a D"
        elif ((random_num > 69) & (random_num < 80)):
            print "Score: ", random_num, "Your grade is a C"
        elif ((random_num > 79) & (random_num <=89)):
            print "Score ", random_num, "Your grade is a B"
        else:
            print "Score: ", random_num, "your grade is an A"


    print "END of PROG"

grades()
