def get_data(filename):
    with open(filename) as file:
        data = []
        for line in file:
            parsed_line = get_tuple(line)
            if parsed_line is not None:
                data.append(parsed_line)
        return data


def get_tuple(line):
    if line[0] == '#' or line[0] == ':':
        return None

    words = line.split()
    data_list = []
    for x in range(5):
        data_list.append(words[x])
    return tuple(data_list)


if __name__ == '__main__':
    print(get_data("Predict.txt"))
