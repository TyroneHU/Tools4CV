import os
import shutil
import numpy as np
from glob import glob


def split_train_val(all_path, split_ratio):
    all_image_path = os.path.join(all_path, 'images')
    all_label_path = os.path.join(all_path, 'labels')

    train_image_path = os.path.join(all_path, 'train', 'images')
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path, 0o777)
    train_label_path = os.path.join(all_path, 'train', 'labels')
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path, 0o777)

    val_image_path = os.path.join(all_path, 'val', 'images')
    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path, 0o777)
    val_label_path = os.path.join(all_path, 'val', 'labels')
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path, 0o777)

    all_image_list = glob(os.path.join(all_image_path, '*.jpg'))
    all_image_num = all_image_list.__sizeof__()
    trainset_num = np.random.randint(0, all_image_num-1, int(split_ratio * all_image_num))

    print('Start to split dataset...')
    for i in range(all_image_list):
        print(all_image_list[i])
        image_name = all_image_list[i].split('\\')[-1]
        label_name = image_name.split('.')[0] + '.txt'
        if i in trainset_num:
            shutil.copy(all_image_list[i], train_image_path)
            shutil.copy(os.path.join(all_label_path, label_name), train_label_path)
        else:
            shutil.copy(all_image_list[i], val_image_path)
            shutil.copy(os.path.join(all_label_path, label_name), val_label_path)

    print('Finish split dataset...')
    print('The train set path: ', train_image_path)
    print('The val set path: ', val_image_path)



def main():
    all_path = r''
    split_ratio = 0.95

    split_train_val(all_path, split_ratio)



if __name__ == '__main__':
    main()



























