import random
r = random.randint(1,1000) #randomize the missing number

def computer_search_for_it(the_random_number):
    guess = 0
    while True:
        if guess == the_random_number:
            print(f"Computer guessed the random number \"{the_random_number}.\"")
            break
        elif guess < the_random_number: #if the number it seek is higher than current guess, it increment the value by 100
            guess += 100
            continue
        else: #if the number it seek is lower than current guess, keep decrementing it by 1 until it reached right value
            while guess != the_random_number:
                if guess == the_random_number:
                    print(f"Computer guessed the random number \"{the_random_number}.\"")
                    break
                else:
                    guess -=1

    return the_random_number

computer_search_for_it(r)