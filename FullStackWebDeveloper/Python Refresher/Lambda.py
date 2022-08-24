add = lambda x , y : x + y

add(5,7)


def double(x):
    return  x *2

new_list = [1,2,3,4,5]

doubled = list(map(double,new_list))

print(list(map(lambda x : x ** 2,new_list)))

print(doubled)