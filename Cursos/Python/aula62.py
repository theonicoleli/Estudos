# Estudando os conceitos de yield

# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n+= 1

#         if n >= maximum:
#             return
    

# gen = generator(n=20, maximum=30)
# for n in gen:
#     print(n)


def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    print('FINALIZOU GEN1')


def gen2(gen=None):
    print('COMEÇOU GEN2')
    if gen!= None:
        yield from gen()
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    print('FINALIZOU GEN2')

g2 = gen2(gen1)
g3 = gen2()
for n in g2:
    print(n)
for n in g3:
    print(n)