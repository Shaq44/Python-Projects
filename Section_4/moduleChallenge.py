import random;


highest = 10;
answer = random.randint(1,highest);

print("please guess a number between 1 and {}".format(highest));
guess = int(input());


while guess != answer:
    if guess == answer:
     print("Correct");
    elif guess < answer:
        print("too low");
    elif guess > answer:
        print("too high");
    else:
        print("Sorry wrong answer");

    if guess == 0:
        break;
     
