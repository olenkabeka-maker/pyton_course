# test function  locals()

def test():
    a = 125
    b = 'asb'    
    print(locals())
test()

while True:
    weather = input("What is the weather today? (type 'exit' to stop)").lower()
    
    if weather == 'exit':
        print("Goodbye! See you later! 👋")
        break
    elif weather == 'rainny':
        print("It's raining dance now💃")
    elif weather == 'sunny':
        print("O! It's nice!😎")
    elif weather == 'windy':
        print('Brrrrr...💨')
        print(locals())       # переміщала в різні місця
    else:
        print('But what about this weather?!🤔')
print() 
  