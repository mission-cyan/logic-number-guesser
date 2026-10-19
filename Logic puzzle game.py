'''Create a Logic Puzzle game'''

import random
import time

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
                nums.append(i)
        
        else:
            if i%div == 0 and i%ndiv != 0 and i%2 != 0 :
                nums.append(i)
    
    if len(nums) > 3:
        ans = random.sample(nums, 3)
    else:
        ans = nums
        
    return ans


def generate_puzzle():
    
    answer = []
    while answer == []:
        e, d, nd, thr = generate_clues()
        answer = generate_numbers(e, d, nd, thr)
    
    if e:
        parity = 'Even'
    else:
        parity = 'Odd'
    
    print("The parity of the number is :", parity)
    print("The number is greater than or equal to", thr)
    print("The number is divisible by", d)
    print("The number is not divisible by", nd)
    print()
    
    return answer

def gameplay():
    global score
    
    answer = generate_puzzle()

    try :
       a = int(input("Enter your answer: "))
       if a in range(1,101):
           if a in answer:
               time.sleep(0.6)
               print("\nYesss Correct !!")
               score += 4
               time.sleep(0.8)
           else:
               time.sleep(0.6)
               print("\nNope, Machine didn't guess that!")
               score -= 1
               time.sleep(0.8)
       else:
           print("\nInput must be a number btwn 1-100 only.")
           
    except ValueError:
        
        print("\n##### ERROR!!\nA misclick I assume ?! Next time, type in integers only !")
        
    print()


inst = "In this game, the engine 'thinks' of a number btwn 1-100, and you have to guess it.\
To help you, you will be given some clues about the number.\
Time is set by the engine and your score is evaluated at last (+4 for correct, -1 for incorrect).\
In case the clues to indicate multiple numbers, there will be some (max 3)random correct\
answers, chosen by the machine. So let's begin, here are your clues! -- "
score = 0
    
print(inst, end = "\n")

rounds = int(input("Enter the no. of rounds you wanna play - "))

st_time = time.perf_counter()

for i in range(1, rounds + 1):
    
    print(f"--- ROUND {i} begins ! ---\n")
    gameplay()
    
end_time = time.perf_counter()

time_taken = round(end_time - st_time, 2)
    
print("Thanks for playing !!")
print("Your score is,", score)
print(f"Time taken by the player = {time_taken} seconds")
