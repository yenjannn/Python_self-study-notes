# coding: utf-8
# 跟電腦猜拳
import numpy as np

player = {'Bye':0, '剪刀':1, '石頭':2, '布':3}
computer = {1:'剪刀', 2:'石頭', 3:'布'}
win = [2, 1, -2]

message = ''
while message != 'Bye':
    message = input("請輸入剪刀、石頭或布，結束遊戲請輸入Bye: ")
    n = np.random.randint(1, 3)
    p = player[message]
    result = n - p
    if message != 'Bye':
        if result in win:
            print("您出", message, "，電腦出", computer[n])
            print("您輸了Q_Q")
            print()
        elif result == 0:
            print("您出", message, "，電腦出", computer[n])
            print("平手!")
            print()
        elif result == -1:
            print("您出", message, "，電腦出", computer[n])
            print("您贏了，恭喜^皿^")
            print()
    elif message == 'Bye':
        print("Bye,歡迎下次再來玩!")
        
# 輸入錯誤的時候，如果想顯示輸入錯誤該怎麼做
