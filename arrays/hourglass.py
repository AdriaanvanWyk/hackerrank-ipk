



def get_max_hourglass_sum(input_array):

    highest_total = None
    
    for row in range(4):
        for column in range(4):
            values = list()
            values.append(input_array[row][column])
            values.append(input_array[row][column+1])
            values.append(input_array[row][column+2])

            values.append(input_array[row+1][column+1])

            values.append(input_array[row+2][column])
            values.append(input_array[row+2][column+1])
            values.append(input_array[row+2][column+2])

            current_sum = sum(values)

            if highest_total or highest_total==0:
                if current_sum > highest_total:
                    highest_total = current_sum
            else:
                highest_total = current_sum

    
    return highest_total


            




if __name__ == '__main__':

    input_array =   [[1, 1, 1, 0, 0, 0], 
                    [0, 1, 0, 0, 0, 0], 
                    [1, 1, 1, 0, 0, 0], 
                    [0, 0, 2, 4, 4, 0], 
                    [0, 0, 0, 2, 0, 0], 
                    [0, 0, 1, 2, 4, 0]]


    print(get_max_hourglass_sum(input_array))
