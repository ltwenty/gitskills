#! /usr/bin/python
# coding=utf-8
# import shutil
import os
import sys

os.system("rm -rf ./output_*")

# get current directory's apk files
# see those page below for help :
# http://wangwei007.blog.51cto.com/68019/1104940
# https://docs.python.org/2/library/os.path.html
src_apks = []
for file in os.listdir('.'):
    if os.path.isfile(file):
        extension = os.path.splitext(file)[1][1:]
        if extension in 'apk':
            src_apks.append(file)



if len(sys.argv) >= 2 and sys.argv[1].strip():
    # get pids from cmd arg
    lines = [str(sys.argv[1])]
else: 
    # get pids from confg file
    channel_file = 'info/channel.txt'
    f = open(channel_file)
    lines = f.readlines()
    f.close()

for src_apk in src_apks:
    # file name (with extension)
    src_apk_file_name = os.path.basename(src_apk)

    if ".apk" not in src_apk_file_name:
        continue

    # print src_apk_file_name
    # split file name and suffix
    temp_list = os.path.splitext(src_apk_file_name)
    # name without extension
    src_apk_name = temp_list[0]
    # suffix with "."  e.g   ".apk"
    src_apk_extension = temp_list[1]
    # create output directory by file name
    output_dir = 'output_' + src_apk_name + '/'
    # mkdir if not exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # create an apk file for each pid in channel.txt
    for line in lines:
        # get pid remove "\n"
        target_channel = line.strip()
        print "[" + src_apk_name + src_apk_extension + " channel : " + target_channel + "]"
        # generate an new apk by pid
        target_apk = output_dir + src_apk_name + "-" + target_channel + "-" + "release" + src_apk_extension
        # shutil.copy(src_apk, target_apk)
        cmdLine = "java -jar ./walle-cli-all.jar put -c " + target_channel + " " + src_apk_file_name + " " + target_apk
        # print cmdLine
        os.system(cmdLine)

print '\nCongratulations ...\n'

# raw_input()

