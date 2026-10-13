'''Create a Logic Puzzle game'''

import random

def generate_clues():
    
    even = random.choice([True, False])
    threshold = random.randint(10,50)
    divisor = random.randint(3,30)
    
    while True:
        ndivisor = random.randint(3,divisor + 11)    
        if ndivisor != divisor:
            break
        
    return even, divisor, ndivisor, threshold


def generate_numbers(even, div, ndiv, thr):
    
    nums = []
    
    for i in range(thr, 101):
        
        if even:
            if i%div == 0 and i%ndiv != 0 and i%2 == 0 :
                nums += [i]
        
        else:
            if i%div == 0 and i%ndiv != 0 and i%2 != 0 :
                nums += [i]
                
    if len(nums) > 3:
        ans = random.sample(nums, 3)
    else:
        ans = nums
        
    return ans


def generate_puzzle():
    
    e, d, nd, thr = generate_clues()
    answer = generate_numbers(e, d, nd, thr)
    
    if e:
        parity = 'Even'
    else:
        parity = 'Odd'
    
    print("The parity of the number is :", parity)
    print("The number is greater than", thr)
    print("The number is divisible by", d)
    print("The number is not divisible by", nd)
    
    return answer

inst = "In this game, the engine thinks of a number btwn 1-100, and you have to guess it.\
    To help you, you will be given some clues about the number.\
    In case the clues to indicate multiple numbers, there will be 3 random correct\
    answers. So let's begin, here are your clues! --"
    
print(inst)
print()

answer = generate_puzzle()
print()


while True:
    
    a = int(input("Enter your answer : "))
    print()
    
    if a in answer:
        print("Yessss correct!")
        break
    else:
        print("No, try again, until you get it")
        print("btw, the ans is,", answer)


