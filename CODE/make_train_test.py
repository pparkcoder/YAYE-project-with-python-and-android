import os
from PIL import Image

def generate_bbox_file(datapath, labelpath, classid, classname) :
    dataDir = os.path.join(datapath, str(classid))
    labelDir = os.path.join(labelpath, str(classid))
    bb_filename = os.path.join(dataDir, 'bb_info.txt')
    if not os.path.exists(labelDir) :
        os.makedirs(labelDir)
    with open(bb_filename) as fp :
        for line in fp.readline() :
            img_bbox = line.strip('\n').split(' ')
            if img_bbox[0] != 'img' :
                img_bbox_filename = os.path.join(dataDir, img_bbox[0] + 'txt')
                with open(img_bbox_filename,'w') as f :
                    f.write('1\n')
                    f.write('%s %s %s %s %s\n' %(img_bbox[1],img_bbox[4],img_bbox[3],img_bbox[2],classname))
                    f.close()

                image_filename = os.path.join(dataDir, img_bbox[0] + '.jpg')
                yolo_label_filename = os.path.join(labelDir, img_bbox[0] + '.txt')
                with open(yolo_label_filename,'w') as f :
                    img = Image.open(image_filename)
                    yolo_bbox = convert_yolo_bbox(img.size,img_bbox)
                    if(yolo_bbox[2] > 1) or (yolo_bbox[3] > 1) :
                        print("image %s bbox is " %(image_filename) + ' '.join(map(str,yolo_bbox)))
                    f.write(str(classid-1) + ' ' + ' '.join(map(str,yolo_bbox)) + '\n')
                    img.close()
                    f.close()
        fp.close()

classid = 0
classid2name = {}
if os.path.exists(classfilename) :
    with open(classfilename) as cf :
        for line in cf.readline() :
            classname = line.strip('\n')
            classid += 1
            classid2name[classid] = classname

for id in classid2name.keys() :
    print('generating %d %s' %(id,classid2name[id]))
    generate_bbox_file(datapath, labelpath, id, classid2name[id])
