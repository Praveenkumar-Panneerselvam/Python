import random
max_num=int(input("Enter the maximum number : "))
randum_num=random.randint(1,max_num)
print(randum_num)
count=0
while count<=3:
    Guess_num=int(input(f"Guess the number between 1 and {max_num} : "))
    count+=1
    if Guess_num<1 or Guess_num>max_num:
        print("Invalid guess")
    elif Guess_num == randum_num:
        print("Your Guess is correct")
        print(f"You had taken {count} attempts to guess correct number")
        break
    elif Guess_num > randum_num:
        print("Your Guess is high")
    elif Guess_num < randum_num:
        print("Your Guess is low")
    
    
