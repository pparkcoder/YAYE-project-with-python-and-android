def convert_yolo_bbox(img_size, box) :
    dw = 1./img_size[0]
    dh = 1./img_size[1]
    x = (int(box[1]) + int(box[3]))/2.0
    y = (int(box[2]) + int(box[4]))/2.0
    # x = int(box[1] + int(box[3])/2.0
    # y = int(box[2] + int(box[4])/2.0
    w = abs(int(box[3]) - int(box[1]))
    h = abs(int(box[4]) - int(box[2]))
    x *= dw
    w *= dw
    y *= dh
    h *= dh
    return (x,y,w,h)
