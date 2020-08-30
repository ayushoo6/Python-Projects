import random
print("the rules for the rock paper scissor game is:\n"+"Rock vs paper-->paper wins\n"+"rock vs scissor--> rock wins\n"+"paper vs scissor--> scissor wins\n")
choice_name=""
comp_choice_name=""
while True:
    print("Enter your choice:\n"+"1.Rock\n"+"2.paper\n"+"3.scissor\n")
    ch=int(input("Your turn:"))
    while ch>3 or ch<1:
        ch=int(input("enter your valid input here:"))
        choice_name
        if ch==1:
            choice_name=="rock"
        elif ch==2:
            choice_name=="paper"
        else:
            choice_name=="scissor"
    print("your choice" + choice_name)
    print("\n now computer turn to choice\n")
    comp_choice=random.randint(1,3)
    while comp_choice==ch:
        comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name='rock'
    elif comp_choice==2:
        comp_choice_name='paper'
    else:
        comp_choice_name='scissor'
    print("computer choice is:"+comp_choice_name+"\n")
    print(choice_name+"v/s"+comp_choice_name)
    if((ch==1 and comp_choice==2)or(ch==2 and comp_choice==1)):
        print("paper wins=>",end="")
        result="paper"
    elif((ch==1 and comp_choice==3)or(ch==3 and comp_choice==1)):
        print("rock wins=>",end="")
        result="rock"
    else:
        print("scissor wins=>",end="")
        result="scissor"
    if result==choice_name:
        print("<==you win==>")
    else:
        print("computer wins\n")
    print("wanna play again?(yes/no)")
    ans=input()
    if ans=='no' or ans=='No':
        break
print("\n thaks for playing")
    
                
