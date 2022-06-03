'''
There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer pairs.
Elements of each pair represent number of people get into bus (The first item) and
number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after
the last bus station (after the last array).

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.

'''

def number(bus_stops):
    # Good Luck!
    lst = []
    
    for i in range(len(bus_stops)):
        for j in bus_stops[i]:
            lst.append(j)

    x = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    y = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    
    return sum(x) - sum(y)

foo = number([[10,0],[3,5],[5,8]])
bar = number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
baz = number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])

print(foo, bar, baz, sep='\n')