def posible_layer_num(layer, L, max_num):
    x = []
    for num in layer:
        for l in range(-L, L + 1):
            new_num = num + l
            if (new_num >= 1) and (new_num <= max_num):
                if len(x) == 0:
                    x.append(new_num)
                elif x[-1] < new_num:
                    x.append(new_num)
    return x
    

def check_layer_match_huhu(n_wood_list, L, max_num):
    layer_match = posible_layer_num(n_wood_list[0], L, max_num)
    for layer in n_wood_list[1:]:
        layer_match2 = posible_layer_num(layer, L, max_num)

        layer_match = list(set(layer_match).intersection(set(layer_match2)))
    
    return int(len(layer_match) != 0)
            
            
if __name__ == "__main__":
    n_layers, max_num, L = list(map(int, input().split(" ")))
    n_wood_list = [list(map(int, input().split(" ")))[1:] for i in range(n_layers)]
    print(check_layer_match_huhu(n_wood_list, L, max_num))