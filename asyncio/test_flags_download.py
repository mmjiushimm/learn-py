# -*- coding: utf-8 -*-
import os, os.path, time

import requests

flag_list = ['ad', 'ae', 'af', 'ag']
url_base = 'https://www.fluentpython.com/data/flags'
dir_base = 'd:/flags'

def mkdir():
    os.mkdir(file_base)

def get_flag(flag):
    flag_url = '{0}/{1}/{1}.gif'.format(url_base, flag)
    response = requests.get(flag_url)
    return response.content

def save_flag(flag_name, image):
    flag_filename = flag_name + '.gif'
    file = open(os.path.join(dir_base, flag_filename), mode='wb')
    file.write(image)
    file.close()

def download(flag_list):
    for flag in flag_list:
        image = get_flag(flag)
        save_flag(flag, image)
        print(flag + ' has been down')

def main():
    if not os.path.exists(dir_base):
        mkdir()
    t0 = time.time()
    download(flag_list)
    t1 = time.time()
    dt = t1 - t0
    print('spend {:.3f}senconds to download'.format(dt))

if __name__ == '__main__':
    main()
