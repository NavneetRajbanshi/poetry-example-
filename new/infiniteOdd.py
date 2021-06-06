class infinteOdd:
    def get_infinteOdd():
        n1 = 1
        
        while True:
            n1 += 1
            yield n1
           

    seq = get_infinteOdd(10)

    print(next(seq))
    print(next(seq))   
    print(next(seq))   
    print(next(seq))   
    print(next(seq))   
    print(next(seq)) 
    print(next(seq)) 
    print(next(seq))     
    print(next(seq)) 
    print(next(seq))  