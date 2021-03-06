'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_a_1.py
@time: 2021/5/25 10:13
@Email: Warron.Wang
'''

'''
运行方式：
1 python解释器
2 pytest运行
'''

'''
命令：
pytest --help查看
pytest test_a_1.py -v
pytest -k test_b -v
pytest -k 'test_b or test_a' -v

'''

import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_answer1():
    assert func(4) == 5



class TestDemo:
    # def __init__(self):
    #     pass
    def test_a(self):
        print("a")

    def test_b(self):
        print("b")

    def c(self):
        print("c")

if __name__ == '__main__':
    # pytest.main(['test_a_1.py'])
    pytest.main(['test_a_1.py::TestDemo', '-v'])
