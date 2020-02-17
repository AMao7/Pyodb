import os
#
# working_dir = os.getcwd()
# print(working_dir)
# os.open('pycharm')

def encode_path(file):
    return os.fsencode(file)

def decode_path(file):
    return os.fsdecode(file)

result_coded = encode_path('README.md')
print(result_coded)