import random
r = random.randint(1,1000)

def computer_search_for_it(the_random_number):
    guess = 0
    while True:
        if guess == the_random_number:
            print(f"Computer guessed the random number \"{the_random_number}.\"")
            break
        elif guess < the_random_number:
            guess += 100
            continue
        else:
            while guess != the_random_number:
                if guess == the_random_number:
                    print(f"Computer guessed the random number \"{the_random_number}.\"")
                    break
                else:
                    guess -=1

    return the_random_number

computer_search_for_it(r)