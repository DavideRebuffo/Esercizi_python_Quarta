"""
#funzioni
def nomeFunzione(parametri):
    #codice
    #return

#procedure
def nomeFunzione(parametri):
    #codice
"""


def somma_moltiplicazione(x,y):
    return x+y,x*y
a = 10
b = 4
s,m = somma_moltiplicazione(a, b)
print(s,m)



#lambda function
somma_moltiplicazione2 = lambda x,y:(x+y,x*y)
s,m = somma_moltiplicazione2(a, b)
print(s,m)