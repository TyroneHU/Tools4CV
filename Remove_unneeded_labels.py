import os
import shutil
from glob import glob

def remove_unneeded_labels(label_path, remain_label_list):
    new_label_path = label_path + '_new'
    shutil.copytree(label_path, new_label_path)
    label_list = glob(os.path.join(new_label_path, '*'))
    print('Start to select needed label...')
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
    print('Finish selecting needed labels...')
    print('New labels path: ', new_label_path)


def update_images(label_path, image_path):
    new_label_path = label_path + '_new'
    new_image_path = image_path + '_new'
    if not os.path.exists(new_image_path):
        os.mkdir(new_image_path)
    new_label_list = glob(os.path.join(new_label_path, '*'))
    image_list = glob(os.path.join(image_path, '*'))
    print('Start to select needed image...')
    for image_name in image_list:
        print(image_name)
        label_name = (image_name.split('\\')[-1]).split('.')[0] + '.txt'
        label_name = os.path.join(new_label_path, label_name)
        if label_name in new_label_list:
            shutil.copy(image_name, new_image_path)
    print('Finish selecting needed image...')
    print('New images path: ', new_image_path)



def main():
    label_path = r''
    remain_label_list = ['0', '1']
    image_path = r''

    remove_unneeded_labels(label_path, remain_label_list)
    update_images(label_path, image_path)

if __name__ == '__main__':
    main()
