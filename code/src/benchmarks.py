import sys
import time
import math
#Teste para a primeira função de benchmark

def func1_op(lower_b, upper_b, dimension, x):
        op = sum(pow(x,2))

        return op

def test_with_setup(benchmark):
    def setup():
        return func1_op(-100, 100, 30, 10), {'foo':'bar'}
    benchmark.pedantic(func1_op, setup=setup, rounds=100)