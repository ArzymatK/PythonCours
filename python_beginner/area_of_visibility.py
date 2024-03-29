N = 100
width, height = 1000, 500

def my_func(lst):
    global N #Меняем глобальную переменную в локальной области видиимости
    N= 20
    for x in lst:
        n = x + 1 + N 
        print(n)

my_func([1,2,3])
print(N)