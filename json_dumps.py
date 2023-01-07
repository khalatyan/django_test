from example import tariff_info


def json_to_string(data, indent):
    if type(data) == list:
        for item in data:
            json_to_string(item, indent)

    elif type(data) == dict:
        for key in data:
            if key != 'children':
                print(indent * '\t', key)
            indent += 1
            json_to_string(data[key], indent)

    elif type(data) == str:
        print(indent * '\t', data)


if __name__ == '__main__':
    json_to_string(tariff_info, 0)