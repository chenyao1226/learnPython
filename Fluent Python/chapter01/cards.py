#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 14:30
# @Author  : ChenYao
# @File    : cards.py

import collections
from random import choice

'''namedtuple
构建只有少数属性但是没有方法的对象，利用namedtuple再合适不过了
'''

'''
仅仅实现了一个__getitem__方法，我们构建的对象就变成了可迭代的对象
'''

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()  # 黑桃，方块，梅花，红桃

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

'''
排序
'''

suit_values = dict(spades=3, hearts=2, diamonds=1 , clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == "__main__":
    deck = FrenchDeck()
    print(len(deck))
    # 随机选择一张牌
    print(choice(deck))
    # 正向迭代
    for card in deck:
        print(card)
    # 反向迭代
    for car in reversed(deck):
        print(card)

    '''即使没有实现__contains__方法，如果它是可迭代的， 那么in运算就会按照顺序做一次迭代搜索
    '''
    print(Card(rank='3', suit='hearts') in deck)

    # 对牌进行排序
    for card in sorted(deck, key=spades_high):
        print(card)


'''
如果是自定义对象，使用len方法会调用类中的__len__方法，如果是python内置的类list，dict，那么Cpython会抄近路，
直接返回ob_size属性，这个方法更快，是用c语言实现的
'''