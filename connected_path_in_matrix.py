
'''

1 1 0 0 0 0 1
0 1 0 0 0 0 0
1 0 1 0 0 0 1
0 0 0 1 0 0 0

'''

dim = 10

mem_2d={}

def count_path_helper( map_2d, r, c ):


def count_path ( map_2d, r, c ):

    key = get_key(r,c)
    mem_val = mem_2d.get(key, None)
    if mem_val != None:
        return mem_val
    if (  map_2d[r][c] ==0 ):
        return 0
    if r== dim-1 and c == dim-1 :
        return 1

    r_val= count_path ( map_2d, r +1, c)
    mem_2d[get_key(r_1, c)] = r_val
    c_val = count_path ( map_2d, r, c+1)






if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    count_path(map_2d, 0, 0)