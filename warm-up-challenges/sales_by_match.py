



def get_number_of_pairs(sock_list: list):

    pair_count = 0
    while sock_list:
        sock = sock_list[0]
        if sock_list.count(sock) > 1:
            sock_list.remove(sock)
            sock_list.remove(sock)
            pair_count += 1
        else:
            sock_list.remove(sock)
    return pair_count

if __name__ == '__main__':
    input = [4,5,5,5,6,6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
    print(get_number_of_pairs(input))