


def repeated_string(input_string, number_of_chars_to_check):

    input_string_as_list = list(input_string)
    a_occurences = input_string_as_list.count('a')

    all_a_occurences = a_occurences*(number_of_chars_to_check // len(input_string_as_list))

    all_a_occurences += input_string_as_list[:number_of_chars_to_check%len(input_string_as_list)].count('a')

    return all_a_occurences


if __name__ == '__main__':

    input_string = 'epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'
    n = 549382313570

    print(repeated_string(input_string, n))


