def challenge3(word):
    # one is index for the letters the other tracks highest number and constants tracks the constants
    
    abcs = ' abcdefghijklmnopqrstuvwxyz'
    value = 0
    constants = '' 

    # for loops goes through all the letters

    for i, v in enumerate(word):
            if(v == 'a'):
                constants = constants + " " 
                value = value
            elif(v == 'e'):
                constants = constants + " " 
                value = value
            elif(v == 'i'):
                constants = constants + " " 
                value = value
            elif(v == 'o'):
                constants = constants + " " 
                value = value
            elif(v == 'u'):
                constants = constants + " " 
                value = value
            elif(v == 'y'):
                constants = constants + " " 
                value = value
            else:
                constants = constants + v 
                if(abcs.find(v) > value):
                    value = abcs.find(v)

    # prints out the final text
    print(f"The consonant substrings are: \"{constants}\" and the highest value is {value}")

challenge3('strength')
