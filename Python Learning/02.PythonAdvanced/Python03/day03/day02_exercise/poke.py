# 2. 模拟斗地主发牌,牌共54张
#   黑桃('\u2660'), 梅花('\u2663'),方块('\u2665'),红桃('\u2666')
#   大小王
#   A2-10JQK
#   三个人玩，每个人发17张牌，底牌留三张
#   操作:
#     输入回车: 打印第一个人的17张牌
#     输入回车: .....二...........
#     输入回车: .....三...........
#     输入回车: 打印三张底牌


def get_poke():
    '''生成一副扑克'''
    kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
    number = ['A'] + list(
        map(str, range(2, 11))) + list('JQK')
    # print(number)
    L = ['大王', '小王'] + [x + y for x in kinds
             for y in number]
    return L


import random

def poke_games():
    pk = get_poke()
    random.shuffle(pk)
    input("输入回车继续")
    print("第一个人的17张牌是:", pk[:17])
    input("输入回车继续")
    print("第二个人的17张牌是:", pk[17:34])
    input("输入回车继续")
    print("第三个人的17张牌是:", pk[34:51])
    input("输入回车继续")
    print("底牌是:", pk[51:])



poke_games()
