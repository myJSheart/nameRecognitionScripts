import glob
all_files = glob.glob('/Users/chenxuzhao/Desktop/nameRecognitionProject/standardNameResults/tagged_files/*.json')

for file_name in all_files:
    from pathlib2 import Path
    file_parent_path = Path(file_name).parent
    import os
    head, tail = os.path.split(file_name)
    file_destination_path = str(file_parent_path) + '/json/' + str(tail)
    os.rename(file_name, file_destination_path)
