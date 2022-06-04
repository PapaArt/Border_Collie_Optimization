import sys
import time
import math
import numpy as np

# Define the function blocks
def prod( it ):
    p= 1
    for n in it:
        p *= n
    return p

def Ufun(x: int, a: int, k: int, m: int) -> int:
        op = k*((x-a)^m) * (x>a) + k * ((-x-a)^m) * (x<(-a))
        
        return op

#Woking
def func1_op(x):
    op = np.sum(np.power(x,2))

    return op
#Working
def func2_op(x):
    op = np.sum(np.abs(x)) + np.prod(np.abs(x))           

    return op
#Not working
def func3_op(x):
    dim = x
    op = 0
    for i in range(len(dim)):
        op += np.power(x,2)
        
    return op
#Working
def func4_op(x):
        
    op = max(abs(x))

    return op
#Not working
def func5_op(x):

    dim = x
    op = (100*x) - np.power(np.power(x,2),2) + np.power((x-1),2)

    return op
#Working
def func6_op(x):
        
    op = sum(np.power(abs(x+0.5), 2))

    return op
#Working
def func7_op(x):

    dim = x
    op = sum(x * np.power(x,4) + np.random.random())

    return op
#Working
def func8_op(x):

    op = np.sum(np.sum(-x) * math.sin(math.sqrt(np.sum(abs(x)))))

    return op
#Not working
def func9_op(x):

    dim = x
    op = sum(-20 * math.exp(-0.2 * math.sqrt(abs(np.power(x,2)/dim))) - math.exp(math.cos(2 * math.pi * np.sum(x))/dim) + 20 + math.exp(1))

    return op
#Not working
def func10_op(x):

    dim = x
    op = (math.pi/dim) * (10* (math.sin(math.pi * 1 + np.power((x + 1)/4)),2)) + np.sum((np.power(((x+1)/4),2)) * (1+10 * ((math.sin(math.pi * float(np.power(1+(x+1)/4,2)))))) + float(np.power((x+1)/4,2))) + np.sum(Ufun(x, 10, 100, 4))

    return op
#Not working
def func11_op(x):

    dim = x
    op = 0.1 * (np.power((math.sin(3*math.pi*x)), 2) + np.sum(np.power((x-1), 2) * np.power(1+(math.sin(3*math.pi*x)), 2)) + np.power((x-1), 2)* np.power(1+(math.sin(2*math.pi*x)), 2)) + np.sum(Ufun(x,5,100,4))

    return op
#Not working
def func12_op(x):

    aS = np.matrix
    bS = [0 for i in range(25)]
        
    for j in range(1, 25):
        #Rever o codigo para ver a necessidade de transpor a matriz
        bS[j] = np.sum(np.power((x - aS[:25,j]),6))

    op = np.power(1/500 + np.sum(1/(bS)),(-1))

    return op
#Working
def func13_op(x):

    aK = [.1957, .1947, .1735, .16, .0844, .0627, .0456, .0342, .0323, .0235, .0246]
    bK = [.25, .5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
        
    for i in range(len(bK)):
        bK[i] = 1/bK[i]
        op = np.sum(np.power(aK[i]-((x * (np.power(bK[i],2)+x*bK[i]))/(np.power(bK[i],2)+x * bK[i]+x)),2))

    return op
#Not working
def func14_op(x):

    op = (1 + np.power((2*x+1),2) * (19-(14*x+3)*np.power(x,2)-(14*x+6*x*x)+3*np.power(x,2))) * (np.power(30+(2*x-3*x),2)*(18-32*x+12*np.power(x,2)+(48*x)-(36*x*x)+27*np.power(x,2)))

    return op
#Working
def func15_op(x):

    aH = [[3, 10, 30], [0.1, 10, 35], [3, 10, 30], [0.1, 10, 35]]
    cH = [1, 1.2, 3, 3.2]
    pH = [[0.3689, 0.117, 0.2673], [0.4699, 0.4387, 0.747], [0.1091, 0.8732, 0.5547], [0.03815, 0.5743, 0.8828]]
    op = 0

    for i in range(1,4):
        op = op - cH[i]*math.exp(-(np.sum(aH[i:]*(np.power(x-pH[i:],2)))))

    return op
#Not working
def func16_op(x):

    aK=[.1957,.1947,.1735,.16,.0844,.0627,.0456,.0342,.0323,.0235,.0246];
    bK=[.25,.5,1,2,4,6,8,10,12,14,16];
    aK=np.asarray(aK);
    bK=np.asarray(bK);
    bK = 1/bK;  
        
    fit=np.sum((aK-((x[0]*(bK**2+x[1]*bK))/(bK**2+x[2]*bK+x[3])))**2);
    
    return fit

#Not working
def func17_op(x):

    aSH = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]]
    cSH = [0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5]
    op = 0

    for i in range(1,5):
        #Apostrofo
        op = op - np.power(((x-aSH[1:])*(x-aSH[i:])+cSH[i]),(-1))

    return op
#Not working
def func18_op(x):

    aSH = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]]
    cSH = [0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5]
    op = 0

    for i in range(1, 7):
        #Apostrofo
        op = op - np.power(((x - aSH[i,:])*(x-aSH[i,:])+cSH[i]),(-1))

    return op
#Not working
def func19_op(x):

    aSH = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]]
    cSH = [0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5]
    op = 0

    for i in range(1, 10):
        #Apostrofo
        op = op - np.power(((x-aSH[i,:])*(x-aSH[i,:]) + cSH[i]),(-1))

    return op

def get_func_details(a):

    #[name, lb, ub, dim]
    param = {   0: ["func1_op", -100, 100, 30],
                1: ["func2_op", -10, 10, 30],
                2: ["func3_op", -100, 100, 30],
                3: ["func4_op", -100, 100, 30],
                4: ["func5_op", -30, 30, 30],
                5: ["func6_op", -100, 100, 30],
                6: ["func7_op", -1.28, 1.28, 30],
                7: ["func8_op", -500, 500, 30],
                8: ["func9_op", -32, 32, 30],
                9: ["func10_op", -50, 50, 30],
                10: ["func11_op", -50, 50, 30],
                11: ["func12_op", -65.536, 65.536, 2],
                12: ["func13_op", -5, 5, 4],
                13: ["func14_op", -2, 2, 2],
                14: ["func15_op", 0, 1, 3],
                15: ["func16_op", 0, 1, 6],
                16: ["func17_op", 0, 10, 4],
                17: ["func18_op", 0, 10, 4],
                18: ["func19_op", 0, 10, 4]
                }
        
    return param.get(a, "nothing")