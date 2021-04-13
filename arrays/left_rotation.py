



def rotate_array(input_array, rotations):


    for i in range(rotations):
        input_array.append(input_array.pop(0))

    
    return input_array


            




if __name__ == '__main__':

    input_array =   [1, 2, 3, 4, 5]

    rotations = 4


    print(rotate_array(input_array, rotations))
