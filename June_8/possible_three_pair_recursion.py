'''def print_combinations(lst, start, combination):
    if len(combination) == 3:
        print(combination)
        return
    for i in range(start, len(lst)):
        print_combinations(lst, i + 1, combination + [lst[i]])
def find_combinations(lst):
    print_combinations(lst, 0, [])
lst = [3,2,5,4,1,6,8]
find_combinations(lst)'''


def com(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
    fun([],0)
a=[3,5,1,6,7]
k=3
com(a,k)
