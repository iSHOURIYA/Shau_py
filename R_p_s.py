import random
print("Lets's Play Rock Paper and Siscor")
a = int(input('''
Choose :
"1" For ROCK
"2" For Paper
"3" For Scissor
=> '''))
mlst = [1 , 2 , 3]
mdict = {1 : "Rock" , 2 : "Paper" , 3 : "Scissor"}
b = random.choice(mlst)

print(f'You Choose {mdict[a]} And I Chose {mdict[b]}')
if a == b :
    print("It's A Tie")
if (a == 1 and b == 3) :
      print(" You Won !! ")
if (a == 1 and b == 2) :
    print(" I Won !! ")
if (a == 2 and b == 1) :
    print(" You Won !! ")
if (a == 2 and b == 3) :
    print(" I Won !! ")
if (a == 3 and b == 1) :
    print(" I Won !! ")
if (a == 3 and b == 2) :
    print(" You Won !! ")