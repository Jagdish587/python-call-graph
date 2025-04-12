
#!/usr/bin/python3

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def my_add(valA, valB):
    return valA + valB

def my_sub(valA, valB):
    return valA - valB

def my_mul(valA, valB):
    return valA * valB

def my_div(valA, valB):
    return valA / valB

def mycallculator():
    print("value is ", my_add(5,3))
    print("value is ", my_sub(5,3))
    print("value is ", my_mul(5,3))
    print("value is ", my_div(10,2))




if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        mycallculator()
