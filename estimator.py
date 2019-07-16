#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Desc: 根据身高、体重、滑行方式生成滑雪板参考参数

# TODO 增加该程序估算完成后 直接生成配置文件, 通过配置文件直接生成对应的导出文件
# TODO 该计算方法较为粗糙简陋，需要进一步与骑手和厂商进行改进


def find(weight, height):
    """

    :param weight: 体重(单位: kg)
    :param height: 身高(单位: cm)
    :return:
    """
    print("你的身高: {}cm, 体重: {}kg".format(height, weight))


def find_stance_width(feet, inch):
    recommended_stance_width = feet * 10 + inch
    print(recommended_stance_width)


def find_length(feet, inch):
    """

    :param feet: 英尺
    :param inch: 英寸
    :return:
    """
    # Freestyle & Park Board Length
    a = 26 * feet + inch * 2

    # Free Ride Board Length
    b = 27 * feet + inch * 2

    # Big Mountain Riding Board Length
    c = 28 * feet + inch * 2
    print(a, b, c)


if __name__ == "__main__":
    find_length(5, 5)
    find_stance_width(5, 5)
