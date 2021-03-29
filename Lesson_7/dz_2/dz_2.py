import yaml
import os

with open('config.yaml') as con:
    config = yaml.safe_load(con)


def make_dir_list(direct, list_):
    for i in list_:
        if isinstance(i, str):
            if not os.path.exists(os.path.join(direct, i)):
                with open(os.path.join(direct, i), 'w', encoding='utf-8') as file:
                    pass
        elif isinstance(i, dict):
            make_dir_dict(direct, i)


def make_dir_dict(string, dic):
    for key, val in dic.items():
        os.mkdir(os.path.join(string, key))
        if isinstance(val, dict):
            make_dir_dict(key, val)

        elif isinstance(val, str):
            if not os.path.exists(os.path.join(string, key)):
                with open(os.path.join(string, key), 'w', encoding='utf-8') as file:
                    pass
        elif isinstance(val, list):
            make_dir_list(os.path.join(string, key), val)


make_dir_dict('', config)
