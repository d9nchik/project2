from urllib.request import urlopen

COMMENT_CHARS = '#:'


def get_data(url):
    with urlopen(url) as file:
        data = []
        for line in file:
            parsed_line = get_tuple(line.decode())
            if parsed_line is not None:
                data.append(parsed_line)
        return data


def get_tuple(line):
    if line[0] in COMMENT_CHARS:
        return None

    words = line.split()
    data_list = []
    for x in range(5):
        data_list.append(float(words[x]))
    return tuple(data_list)


if __name__ == '__main__':
    print(get_data("ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt"))
