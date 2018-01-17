#auxiliary function to resize all images to size (720,1280)
from PIL import Image
import os
"""
src_image_size = pickle.load(open('../../Data/videos/' + 'src_image_size.pkl', 'rb')) # contains sizes of images in each directory

"""
for k in [2,37,38,39,40,41,44,45]: # identified via find_dodgy_folders above, TODO write tidier version of this
    path = os.path.join('/data1/jonathan/volleyball/videos/',str(k))
    dirs = os.listdir( path )

    def resize(path,dirs,image_size=(1280,720)):
        for item in dirs:
            full_path = os.path.join(path,item)
            if os.path.isfile(full_path) and item not in ['.DS_Store','annotations.txt','annotations.txt~']:
                im = Image.open(full_path)
                f, e = os.path.splitext(full_path)
                imResize = im.resize(image_size, Image.ANTIALIAS)
                imResize.save(f+'.jpg', 'JPEG')

    for p in dirs:
        print(p)
        if p not in ['.DS_Store','annotations.txt','annotations.txt~']:
            resize(os.path.join(path,p), os.listdir(os.path.join(path,p)))

