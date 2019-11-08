from funciones1nivel import sumaTodos

print(sumaTodos(3, lambda x: x*3))

'''
También podría ser:
triple = lambda x: x*3
print(sumaTodos(3, triple))
'''
print(sumaTodos(100, lambda x: x*3))

