import yaml,os


def get_data_from_yaml(file_name):
    """
    #根据文件获取data
    :param file_name: 文件名
    :return: data
    """
    with open("./data"+os.sep+file_name, "r", encoding="utf-8") as f:
        return yaml.load(f)

def get_data_lists(file_name,str_key):
    """
    #根据从data中通过key读取list数据
    :param file_name:文件名
    :param str_key: key
    :return: key对应的值（list）
    """
    return get_data_from_yaml(file_name).get(str_key)


