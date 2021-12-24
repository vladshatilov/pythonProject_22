csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def reading_file(file):
    return [i.split(';') for i in file.split('\n')]


def sorting_by_age(data):
    return sorted(data, key=lambda x: int(x[1]))


def filtering_by_age(data):
    return list(filter(lambda x: int(x[1]) > 10, data))


def get_users_list():
    data = reading_file(csv)
    _new_data = sorting_by_age(data)
    result_data = filtering_by_age(_new_data)
    return result_data


if __name__ == '__main__':
    print(get_users_list())
