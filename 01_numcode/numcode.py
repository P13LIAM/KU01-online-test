def transform_x2y(N: int, binary_list: list):
    y_list = []
    for i, e in enumerate(binary_list):
        e = int(e)
        if i == 0:
            y_i = N + (-1)**(e+1)
        else:
            y_i_lag = y_list[-1]
            y_i = y_i_lag + (-1)**(e+1)
        
        y_list.append(y_i)
    
    return y_list


def transform_y2z(y_list: list):
    z_list = []
    for i, y_i in enumerate(y_list):
        y_i = int(y_i)
        if i == 0:
            z_i = y_i
        else:
            y_i_lag = y_list[i-1]
            z_i = y_i + y_i_lag*(int(y_i > y_i_lag) + 1)
        
        z_list.append(z_i)
    
    return z_list


def inv_transform_x2y(N: int, y_list: list):
    binary_list = []
    for i, y_i in enumerate(y_list):
        y_i = int(y_i)
        if i == 0:
            e = int(N < y_i)
        else:
            y_i_lag = y_list[i-1]
            e = int(y_i_lag < y_i)
        
        binary_list.append(e)
    
    return binary_list


def inv_transform_y2z(z_list: list):
    y_list = []
    for i, z_i in enumerate(z_list):
        z_i = int(z_i)
        if i == 0:
            y_i = z_i
        else:
            y_i_lag = y_list[-1]            
            y_i = z_i - y_i_lag
            if y_i > y_i_lag:
                y_i = z_i - 2*y_i_lag
        y_list.append(y_i)
    
    return y_list
    
if __name__ == "__main__":
    x = str(input())
    N, method = x.split(" ")
    N = int(N)
    input_seq = [int(input()) for e in range(N)]
  
    if method == '1':
        output = inv_transform_x2y(N, input_seq)
        # print("\n\nOutput:")
        for e in output:
            print(e)
    
    else:
        y_list = inv_transform_y2z(input_seq)
        output = inv_transform_x2y(N, y_list)
        # print("\n\nOutput:")
        for e in output:
            print(e)
            