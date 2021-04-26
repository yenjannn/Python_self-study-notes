# coding: utf-8
from random import randint

# 用法與numpy裡的randint不同，這裡的函式會包含前後值
# 正式進入猜數字遊戲

def game():
    ans = randint(1, 100)
    guess = -1
    
    while guess != ans:
        guess = int(input('請輸入一個數字: '))
        
        if guess > ans:
            print('太大了!')
        elif guess < ans:
            print('太小了!')
        else:
            print('太神了!')
play = True

while play:
    game()
    print('y（^ヮ^）y' * 3)
    again = input('要再玩一次嗎? ')
    if again == 'no':
        play = False
