# """
# Loop that keeps asking for input and prints this input until
# the user types 'done', at which point the program stops.
# """
# while True:
#         user_input = input("Kindly enter a word, or 'done' to quit this program: ")
#         print(user_input)
        
#         if user_input == 'done' or 'Done' or 'DONE':
#                 break
        

############################################



while True:
        n = int(input("Kindly enter a positive number or zero, and a negative number to quit: "))

        if n >= 0:
                print(n)
            
        elif n < 0:
                print("Well, That's all folks!")
                break
        
        

    
############################################

while n > 5:
        n = int(input("kindly enter a number: "))
        print(n)
        n -= 1


