import random
import string
import shutil
import errno


def random_word(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def copy_files(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


def create_zip(zip_name, path):
    shutil.make_archive(zip_name, 'zip', path)



