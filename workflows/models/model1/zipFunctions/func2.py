def getTrend(node):
    
    data = node.getData()
    slopes = []
    for i in range(0, len(data)-2):
        p1 = data[i]
        p2 = data[i+1]
        slopes.append(p2 - p1)
    return sum(slopes) / len(slopes)

        

    