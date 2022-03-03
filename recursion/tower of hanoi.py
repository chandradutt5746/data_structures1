def tower(n,from_rod,aux_rod,to_rod):
    if(n == 0):
        return     
    
    tower(n-1,from_rod,to_rod,aux_rod)
    print('move',n,'from',from_rod,' to ',to_rod)
    tower(n-1,aux_rod,from_rod,to_rod)
n=1
tower(n,'a','b','c')