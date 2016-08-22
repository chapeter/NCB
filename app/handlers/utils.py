"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

    2016 - Cisco Systems inc.
"""
import random
import string
import shutil
import errno


"""
Common functions
"""
__author__ = 'Santiago Flores Kanter (sfloresk@cisco.com)'


def random_word(length):
    """
    Create a random word. Useful to create unique IDs
    :param length: length of the word to be returned
    :return: random word
    """
    return ''.join(random.choice(string.lowercase) for i in range(length))


def copy_files(src, dst):
    """
    Copy files from one directory to another
    :param src: file/directory to copy from
    :param dst: file/directory to copy to
    :return: None
    """
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


def create_zip(zip_name, path):
    """
    Create a zip file
    :param zip_name: name of the file
    :param path: directory where is going to be saved
    :return: None
    """
    shutil.make_archive(zip_name, 'zip', path)



