# -*- encoding: utf-8 -*-
########################################
# Created on 28 July 2019
# @author: Yan Gu
# A script to draw Cupid's Arrow
########################################
#heart

from turtle import *
from time import sleep


def go_to(x, y):
    '''将画笔移动到指定位置'''
    up()
    goto(x, y)
    down()


def big_Circle(size):  #函数用于绘制心的大圆
    speed(0)
    for i in range(150):
        forward(size)
        right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
    speed(0)
    for i in range(210):
        forward(size)
        right(0.786)

def line(size):
    '''画直线'''
    speed(4)
    forward(51 * size)

def heart(x, y, size):
    '''画出心形，拼接圆和直线'''
    go_to(x, y)
    left(150)     # 顺时针移动150°
    begin_fill()
    line(size)
    big_Circle(size)
    small_Circle(size)
    left(120)
    small_Circle(size)
    big_Circle(size)
    line(size)
    end_fill()

def arrow():
    pensize(4)
    setheading(0)
    go_to(-470, -20)
    left(15)
    forward(150)
    go_to(269, 158)
    forward(150)

def arrowHead():
    pensize(1)
    speed(5)
    color('red', 'red')
    begin_fill()
    left(120)
    forward(20)
    right(150)
    forward(35)
    right(120)
    forward(35)
    right(150)
    forward(20)
    end_fill()


def main():
    pensize(2)
    color('red', 'pink')
    #getscreen().tracer(30, 0) #取消注释后，快速显示图案
    heart(130, -20, 1)             #画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    setheading(0)                 #使画笔的方向朝向x轴正方向
    heart(-150, -120, 1.5)      #画出第二颗心
    arrow()                         #画出穿过两颗心的直线
    arrowHead()                    #画出箭的箭头
    go_to(-310, -260)
    write("Miss Ye, ", move=True, align="left", font=("Ink Free", 21, "normal"))
    go_to(-200, -260)
    write("I LOVE YOU ", move=True, align="left", font=("Ink Free", 26, "bold"))
    go_to(20, -260)
    write("Three Thousand Times!", move=True, align="left", font=("Ink Free", 21, "normal"))
    done()
    # sleep(5000)

main()