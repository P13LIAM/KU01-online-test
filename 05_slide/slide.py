def total_cuts(order_list):
    sum_cut = 0
    for i, e in enumerate(order_list):
        cuts = 0
        for e2 in order_list[i+1:]:
            if e2 > e:
                cuts += 1
        sum_cut += cuts
    
    return sum_cut
    
    
if __name__ == "__main__":
    n = int(input())
    order_list = [int(input()) for i in range(n)]
    
    sum_cut = total_cuts(order_list) 
    
    print(sum_cut)