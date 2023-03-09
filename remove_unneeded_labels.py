import os
import shutil
from glob import glob

def remove_unneeded_labels(label_path, remain_label_list):
    new_label_path = label_path + '_new'
    shutil.copytree(label_path, new_label_path)
    label_list = glob(os.path.join(new_label_path, '*'))
    print('Start to process...')
    for label_name in label_list:
        print(label_name)
        fp = open(label_name, 'r')
        lines = fp.readlines()
        lines_tmp = []
        fp.close()
        for line in lines:
            cls = line.split(' ')[0]
            if cls in remain_label_list:
                lines_tmp.append(line)
        if 0 == len(lines_tmp):
            os.remove(label_name)
            continue
        fp = open(label_name, 'w')
        fp.writelines(lines_tmp)
        fp.close()
    print('Finish processing...')
    print('New labels path: ', new_label_path)

    
def main():
    label_path = r''
    remain_label_list = ['0', '1']
    
    remove_unneeded_labels(label_path, remain_label_list)

    
if __name__ == '__main__':
    main()
