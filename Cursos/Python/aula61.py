# Iterator and Next = __iter__ ; __next__ ou iter(); next()
# e hasattr() and getattr() 

# string = 'Luiz'
# metodo = 'upper'

# if hasattr(string,metodo):
#     print('Eu tenho o método Upper')
#     print(getattr(string, metodo)())
# else:
#     print(f'Não existeo método: {metodo}')

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

for itens in iterator:
    print(itens)