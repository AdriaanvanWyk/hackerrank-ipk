


def count_valleys(path):

    sea_level = 0
    valley_count  =0

    for step in path:
        previous_sea_level = sea_level
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        
        if previous_sea_level < 0 and sea_level >= 0:
            valley_count += 1
        
    return valley_count


if __name__ == '__main__':
    input_string = 'DDUUDDUDUUUD'

    path = list(input_string)
    print(path)
    print(count_valleys(path))