import random
from colorama import Fore, init
import time
init(autoreset=True)

print(Fore.YELLOW + '''
      
                                                                                               
██╗      ██████╗ ████████╗████████╗███████╗██████╗ ██╗   ██╗
██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗╚██╗ ██╔╝
██║     ██║   ██║   ██║      ██║   █████╗  ██████╔╝ ╚████╔╝ 
██║     ██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗  ╚██╔╝  
███████╗╚██████╔╝   ██║      ██║   ███████╗██║  ██║   ██║   
╚══════╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                            
 ██████╗  █████╗ ███╗   ███╗███████╗                        
██╔════╝ ██╔══██╗████╗ ████║██╔════╝                        
██║  ███╗███████║██╔████╔██║█████╗                          
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                          
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                        
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                        
                                                            
      
      
      
      ''')


lottery_numbers = random.sample(range(1,51),6) #! Randomly generate 6 numbers between 1 and 50

lottery_numbers.sort() #! sort into ascending order

users_numbers = [] #! empty list for the users numbers to be store
for i in range(0,6):
    number = int(input(Fore.LIGHTCYAN_EX + "Enter your numbers between 1 and 50: "))
    #! ^ users input for their numbers.
    
    while number in users_numbers or number < 1 or number > 50: #! checking if the numbers are valid and can't be picked twice.
        print(Fore.RED + "Invalid number. Please try again")
        number = int(input(Fore.LIGHTCYAN_EX + "Enter your numbers between 1 and 50: "))

    users_numbers.append(number) #! appending users list to store their 6 numbers

users_numbers.sort()

print(Fore.BLUE + "\n\n>>> TODAYS LOTTERY NUMBERS ARE: ")

print(lottery_numbers) #! printing the generated lottery numbers

print(Fore.LIGHTMAGENTA_EX + "\n\n>>> YOUR NUMBERS ARE: ")
print(users_numbers) #! printing the users lottery numbers

for seconds in range(3, 0, -1): #! i used a timer so it counts down until the results are shown 
        print("\n")
        print(seconds)
        time.sleep(1)

counter = 0 #! counter set to 0 and will increment if users numbers match lottery generated numbers
for number in users_numbers:
    if number in lottery_numbers:
        counter +=1        

print(Fore.GREEN + "You matched: " + str(counter) + " number(s) corectly!") #! print message to display how many numbers were gussed

#! End of program