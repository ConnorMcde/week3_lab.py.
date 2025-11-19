"""Week 3 exercise 4 menu driven calculator"""
    
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)    
      
    
while True:
        print(f"{Fore.GREEN}---Calculator Menu---{Style.RESET_ALL}")
        print(f"{Fore.RED}1.{Style.RESET_ALL} Add")
        print(f"{Fore.RED}2.{Style.RESET_ALL} Subtract")
        print(f"{Fore.RED}3.{Style.RESET_ALL} Quit")
        
        choice=int(input("Enter your choice: "))
        if choice == 1:
            number1 = int(input("Number to add to: "))
            number2 = int(input("Number to add: "))
            print(number1 + number2)
        elif choice ==2:
            number1 = int(input("Number to subtract from: "))
            number2 = int(input("Number to subtract: "))
            print(number1 - number2)
        else:
            break
            
        
    