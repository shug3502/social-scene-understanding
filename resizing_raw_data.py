#auxiliary function to resize all images to size (720,1280)
from PIL import Image
import os
"""
path = '../../Data/videos/'
dirs = os.listdir( path )

def find_dodgy_folders(path,dirs,image_size=(1280,720)):
    for item in dirs:
        full_path = os.path.join(path,item)
        if os.path.isfile(full_path) and item.endswith('.jpg'):
            im = Image.open(full_path)
            if im.size!=image_size:
                print(im.size)
                print(full_path)

for q in dirs:
    if os.path.isdir(os.path.join(path,q)):
        d = os.listdir(os.path.join(path, q))
        for p in d:
            if os.path.isdir(os.path.join(path,q,p)):
                find_dodgy_folders(os.path.join(path,q,p),os.listdir(os.path.join(path,q,p)))

src_image_size = pickle.load(open('../../Data/videos/' + 'src_image_size.pkl', 'rb')) # contains sizes of images in each directory

"""
for k in [2,37,38,39,40,41,44,45]`; # identified via find_dodgy_folders above, TODO write tidier version of this
    path = os.path.join('../../Data/videos/',str(k))
    dirs = os.listdir( path )

    def resize(path,dirs,image_size=(1280,720)):
        for item in dirs:
            full_path = os.path.join(path,item)
            if os.path.isfile(full_path) and item not in ['.DS_Store','annotations.txt']:
                im = Image.open(full_path)
                f, e = os.path.splitext(full_path)
                imResize = im.resize(image_size, Image.ANTIALIAS)
                imResize.save(f+'.jpg', 'JPEG')

    for p in dirs:
        print(p)
        if p not in ['.DS_Store','annotations.txt']:
            resize(os.path.join(path,p), os.listdir(os.path.join(path,p)))

