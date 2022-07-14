def fifthFunction(width, height):
    
    print(f'Периметр прямоугольника, равен', width+width+height+height)
    
width, height = map(int, input().split())

fifthFunction(width, height)