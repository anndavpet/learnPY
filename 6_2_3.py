def number(bus_stops):
    # Good Luck!
    lst = []
    
    for i in range(len(bus_stops)):
        for j in bus_stops[i]:
            lst.append(j)

    x = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    y = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    
    return sum(x) - sum(y)

print(number([[10,0],[3,5],[5,8]]))
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))