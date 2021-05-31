def count(lst):
    more = 0
    less = 0

    for i in lst:
        if len(i)>5:
            more+=1
        else:
            less+=1
    return more,less

lst =[(input())for i in range(10)]
more,less = count(lst)
print(f'more :{more} & less :{less}')