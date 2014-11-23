

'''
Windows Registry Editor Version 5.00

[-HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.srt\UserChoice]

[HKEY_CLASSES_ROOT\srt_auto_file\shell\Reverse]
@="Reverse Punctuation"

[HKEY_CLASSES_ROOT\srt_auto_file\shell\Reverse\command]
@="C:\\Python27\\python.exe C:\\Users\\Asaf\\Desktop\\reverse-subtitles\\rev.py %1"
'''

import os.path
import sys

REG_FILE_NAME = 'add_to_reg.reg'
REG_FILE_NAME_REMOVE = 'remove_from_reg.reg'
START_REG = 'Windows Registry Editor Version 5.00\n' \
            '\n' \
            '[-HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\.srt\UserChoice]\n' \
            '\n' \
            '[HKEY_CLASSES_ROOT\\srt_auto_file\\shell\\Reverse]\n' \
            '@="Reverse Punctuation"\n' \
            '\n' \
            '[HKEY_CLASSES_ROOT\\srt_auto_file\\shell\\Reverse\\command]\n'

REMOVE_REG = 'Windows Registry Editor Version 5.00\n\n[-HKEY_CLASSES_ROOT\\srt_auto_file\\shell\\Reverse]'


def run():
    # check if reg already exists
    if os.path.exists(REG_FILE_NAME):
        # do nothing
        pass
    with open(REG_FILE_NAME, 'w') as f:
        f.write(START_REG)
        f.write(r'@="{} {} %1"'.format(sys.executable.replace('\\', '\\\\'),
                                       os.path.abspath('rev.py').replace('\\', '\\\\')))
    with open(REG_FILE_NAME_REMOVE, 'w') as f:
        f.write(REMOVE_REG)


if __name__ == '__main__':
    run()




