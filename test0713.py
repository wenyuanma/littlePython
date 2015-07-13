#-*- coding: utf-8 -*- 

#随机抽取扑克牌的程序，调用该脚本，每输入一次回车就会随机返回一张扑克牌
import random

values = range(1, 11) + "Jack Queen King".split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (k, s) for k in values for s in suits]
random.shuffle(deck)
while deck:
    raw_input(deck.pop())
