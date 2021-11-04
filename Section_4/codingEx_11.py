#in this exercise we are to use the continue key word to iterate over numbers 
#that are divisable by 3 or 5

for i in range(0,21):
    if i%3 == 0 or i%5 == 0:
        continue;

    print(i)

    