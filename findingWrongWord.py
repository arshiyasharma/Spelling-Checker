userinp = str(input('Input a string: ')).lower()
converted = userinp.split()
wrdfound=0

for x in converted:
    with open('dictionary.txt', 'r') as file:
        for line in file:
            for word in line.split():  # every word in the array of all words sep by space
                if word == x or word+'.' == x or word+',' == x:
                    wrdfound=wrdfound+1


    if(wrdfound == 0):
        print('\nWrong word found: '+x)
        print('\nDID YOU MEAN: ')
        xlen=len(x)
        seg=x
        for i in range(1,xlen):
            seg = x[:-(i)]
            with open('dictionary.txt', 'r') as file:
                for line in file:
                    for word in line.split():  # every word in the array of all words sep by space
                        if word == seg:
                            print(seg)
    wrdfound=0

