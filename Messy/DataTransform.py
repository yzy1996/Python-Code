from xml.etree.ElementTree import parse
import os

db_dir = './data/VMS/'    #更改为自己的目录地址
anno_path = db_dir
fileList = os.listdir(anno_path)
if not os.path.exists(anno_path):
    os.makedirs(anno_path)
for file_name in fileList:
    if file_name[len(file_name)-3:] != 'xml':
        continue
    filePath = db_dir + file_name
    print(filePath)
    tree = parse(filePath)
    root = tree.getroot()
    parsed = []
    for annot in root.iter('annotation'):
        for obj in annot.findall('object'):
            label = obj.findtext('name')
            for coord in obj.findall('bndbox'):
                x_max = float(coord.findtext('xmax'))
                x_min = float(coord.findtext('xmin'))
                y_max = float(coord.findtext('ymax'))
                y_min = float(coord.findtext('ymin'))
            parsed = parsed + [str(label) + ',' + str(x_min) + ',' + str(y_min) + ','+ str(x_max) + ',' + str(y_max)]
    fp = open(anno_path + '/' + file_name[:-3] + 'txt','w')
    for elem in parsed:
        print>>fp, elem
    fp.close()
