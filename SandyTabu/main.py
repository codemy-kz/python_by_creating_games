import random

start_point = 1
end_point = 10

value = random.randrange(start_point, end_point)
info = "Компьютер " + str(start_point) + " ... " + str(end_point) + " сандардың аралығындағы " \
        + " бір санды жасырды. \nСіз сол санды табуыңыз керек. Қалай ойлайсыз, ол қандай сан?! " \
        + "\nЖауабын цифрмен жазыңыз. \n"

print(info)

guess_number = None

while guess_number != value:
    
    guess_number = int(input())
    if guess_number > value:
        print("Сіз жасырылған саннан асып кеттіңіз. Қайта көріңіз")
    elif guess_number < value:
        print("Сіз жасырылған санға жетпедіңіз. Қайта көріңіз")   

print("Құттықтаймын! Сіз жасырылған санды таптыңыз!") 
