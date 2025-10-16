# test function  locals()

def test():
    a = 125
    b = 'asb'    
    print(locals())
test()

from colorama import Fore, Style, init

init(autoreset=True)   # Ініціалізація кольорів

while True:
    weather = input("What is the weather today? (type 'exit' to stop)").lower()
    
    if weather == 'exit':
        print(Fore.MAGENTA + "Goodbye! See you later! 👋")
        break
    elif weather == 'rainny':
        print(Fore.BLUE + "It's raining dance now💃")
    elif weather == 'sunny':
        print(Fore.YELLOW + "O! It's nice!😎")
    elif weather == 'windy':
        print(Fore.CYAN +'Brrrrr...💨')
        print(locals())       # переміщала в різні місця
    else:
        print('But what about this weather?!🤔')
print() 
  