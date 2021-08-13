import os
import os.path
from xml.dom.minidom import Document


def writeXml(imgname, w, h, boxes, label):

    doc = Document()
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    # owner
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    folder_txt = doc.createTextNode(label)
    folder.appendChild(folder_txt) 

    # Filename
    filename = doc.createElement('filename')
    annotation.appendChild(filename)
    filename_txt = doc.createTextNode(imgname)
    filename.appendChild(filename_txt) 

    # Size tag
    size = doc.createElement('size')
    annotation.appendChild(size)

    width = doc.createElement('width')
    size.appendChild(width)
    width_txt = doc.createTextNode(str(w))
    width.appendChild(width_txt)

    height = doc.createElement('height')
    size.appendChild(height)
    height_txt = doc.createTextNode(str(h))
    height.appendChild(height_txt)

    depth = doc.createElement('depth')
    size.appendChild(depth)
    depth_txt = doc.createTextNode("3")
    depth.appendChild(depth_txt)

    #segmented
    segmented = doc.createElement('segmented')
    annotation.appendChild(segmented)
    segmented_txt = doc.createTextNode("0")
    segmented.appendChild(segmented_txt)   
     
    # Append boxes
    for i in range(int(len(boxes))):
        objbuds=boxes[i]
        if len(objbuds) ==0:
            break
        objbuds = objbuds[i]

        # threes
        object_new = doc.createElement("object")
        annotation.appendChild(object_new)

        name = doc.createElement('name')
        object_new.appendChild(name)
        name_txt = doc.createTextNode(label)
        name.appendChild(name_txt)

        pose = doc.createElement('pose')
        object_new.appendChild(pose)
        pose_txt = doc.createTextNode("Unspecified")
        pose.appendChild(pose_txt)

        truncated = doc.createElement('truncated')
        object_new.appendChild(truncated)
        truncated_txt = doc.createTextNode("0")
        truncated.appendChild(truncated_txt)

        difficult = doc.createElement('difficult')
        object_new.appendChild(difficult)
        difficult_txt = doc.createTextNode("0")
        difficult.appendChild(difficult_txt)

        # threes-1#
        bndbox = doc.createElement('bndbox')
        object_new.appendChild(bndbox)
        
        x1 = float(objbuds[0])
        y1 = float(objbuds[1])
        w1 = float(objbuds[2])
        h1 = float(objbuds[3])
        
        xmin = doc.createElement('xmin')
        bndbox.appendChild(xmin)
                    
        xmin_txt = doc.createTextNode(str(x1))
        xmin.appendChild(xmin_txt)

        ymin = doc.createElement('ymin')
        bndbox.appendChild(ymin)
        ymin_txt = doc.createTextNode(str(y1))
        ymin.appendChild(ymin_txt)

        xmax = doc.createElement('xmax')
        bndbox.appendChild(xmax) 
        xmax_txt = doc.createTextNode(str(w1))
        xmax.appendChild(xmax_txt)

        ymax = doc.createElement('ymax')
        bndbox.appendChild(ymax)
        ymax_txt = doc.createTextNode(str(h1))
        ymax.appendChild(ymax_txt)

    # This is to create the xml with correct indent            
    tempfile = "temp.xml"
    xmlfile = imgname.split(".")[0] + ".xml"
    with open(tempfile, "w") as f:
        f.write(doc.toprettyxml(indent='\t'))

    # Now rewrite the xml file with all tags
    rewrite = open(tempfile, "r")
    lines = rewrite.read().split('\n')
    newlines = lines[1:len(lines) - 1]
    fw = open(os.path.join(label,xmlfile), "w")
    for i in range(0, len(newlines)):
        fw.write(newlines[i] + '\n')

    # Close all opened files
    fw.close()
    rewrite.close()