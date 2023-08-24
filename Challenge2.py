def greaterthan3(a, b, c):
    # counter tracks if the letters are bigger than 0
    counter = 0

    # we use the if statements to go through each and check

    if(a > 0):
        counter =+ 1
    if(b > 0):
        counter += 1
    if(c > 0):
        counter += 1

    # how we decide if done or not

    if(counter == 2):
        return True

    else:
        return False

