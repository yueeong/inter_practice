

def compressor(input_string: str) -> str:
    print(input_string)
    previous_char = ''
    char_count = 0
    char_list = []
    for each in input_string:
        if each == previous_char:
            char_count += 1  
            previous_char = each          
        else:
            if len(previous_char) != 0 :
                char_list.append(str(char_count))
                char_list.append(previous_char)
            previous_char = each
            char_count = 1
    char_list.append(str(char_count))
    char_list.append(previous_char)       
            

    return ''.join(char_list)


def main():
    test_string = 'aaabvvvbbcccc'
    print(compressor(test_string))

if __name__ == "__main__":
    main()