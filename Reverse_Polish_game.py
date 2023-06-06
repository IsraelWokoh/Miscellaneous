import random

def pick_operator():
    op=random.randrange(3)
    if op==0:
        return "+"
    if op==1:
        return "x"
    if op==2:
        return "-"

def pick_number():
    return random.randrange(9)+1

def set_question():
    question=""
    for i in range(len(expression)):
        question=question+str(expression[i])+" "
    print(question) 

game_on=True
level=1

while game_on:
    expression=[]
    numbers=0
    operators=0
    difficulty=level*2+1
    for i in range(difficulty):
        # Must have at least two numbers to start with
        if (operators+2)>numbers:
            expression.append(pick_number())
            numbers=numbers+1
        # Fill in with operators towards the end if needed
        elif (i*2>difficulty) and (numbers*2)==difficulty+1:
            expression.append(pick_operator())
            operators=operators+1
        else:
            # Choose randomly between number and operator
            num_or_op=random.randrange(2)
            if num_or_op==0:
                expression.append(pick_number())
                numbers=numbers+1
            else:
                expression.append(pick_operator())
                operators=operators+1
    print("Level",level)
    set_question()
    
    # Evaluate expression
    stack=[]
    for i in range(len(expression)):
        item=expression[i]
        # Check if operator or number
        if item=="+" or item=="-" or item=="x":
            first_item=stack[len(stack)-2]
            second_item=stack[len(stack)-1]
            stack.pop()
            stack.pop()
            if item=="-":
                stack.append(first_item-second_item)
            if item=="+":
                stack.append(first_item+second_item)
            if item=="x":
                stack.append(first_item*second_item)
        else:
            stack.append(item)
    actual_answer=stack[0]
    their_answer=int(input("Please enter the answer:"))
    if actual_answer!=their_answer:
        game_on=False
    else:
        level=level+1
        print("**************")
        print("* Well done! *")
        print("**************")
print("Incorrect, the answer was",actual_answer)
print("Game over, you reached level",level)
