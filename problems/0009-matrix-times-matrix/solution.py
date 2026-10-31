def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(b) != len(a[0]):
        return -1
    
    product = []
    
    for i in range(len(a)):
        prodel = []
        
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]
        
            prodel.append(s)
        product.append(prodel)

    return product
        