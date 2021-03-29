import os

root = 'my_project'
folds = ['settings', 'main_app', 'admin_app', 'auth_app']


def create_fold(main_fold='my_project', *args):
    if not os.path.exists(main_fold):
        os.mkdir(main_fold)

    for _ in args:
        for fold in _:
            if not os.path.exists(fold):
                os.mkdir(os.path.join(main_fold, fold))


if __name__ == '__main__':
    create_fold(root, folds)
