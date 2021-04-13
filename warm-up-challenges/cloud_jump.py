

def count_cloud_jumps(cloud_list):

    end_cloud = len(cloud_list)-1
    current_cloud = 0
    jumps = 0

    print(cloud_list)
    while current_cloud < end_cloud:
        print(f'Current Cloud: {current_cloud}')


        if current_cloud+1 == end_cloud:
            current_cloud += 1
            jumps += 1   
        elif cloud_list[current_cloud+2] == 0:
            current_cloud += 2
            jumps += 1
        elif cloud_list[current_cloud+1] == 0:
            current_cloud += 1
            jumps += 1

    return jumps




if __name__ == '__main__':
    test_input_string = '0 0 0 1 0 0'

    cloud_list = [int(x) for x in test_input_string.split(' ')]

    print(count_cloud_jumps(cloud_list))