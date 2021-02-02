#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import shutil
from xml.dom import minidom
from xml.dom.minidom import parse
import cv2
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def change_xml(src_path, dst_path):
    xml_list = os.listdir(src_path)
    i=0
    for xml_f in xml_list:
        if xml_f.endswith('.xml'):
            w_x1=0
            w_x2=0
            src_xml = src_path + xml_f
            dst_xml = dst_path + xml_f
            doc = minidom.Document()
            booklist = doc.createElement("annotation")
            doc.appendChild(booklist)
            #f = file(dst_xml, 'w')
            f = open(dst_xml, 'w')
            doc.writexml(f)
            f.close()
            src_domTree = parse(src_xml)
            dst_domTree = parse(dst_xml)
            #根元素
            #s_rootNode = src_domTree.documentElement
            annotation_node = dst_domTree.documentElement
          
            annotations = src_domTree.getElementsByTagName('annotation')
            annotation = annotations[0]
            #annotation_node = dst_domTree.createElement('annotation')

            folder = annotation.getElementsByTagName('folder')
            folder_v = folder[0].childNodes[0].data
            folder_node = dst_domTree.createElement('folder')
            d_folder_v = dst_domTree.createTextNode(folder_v)
            folder_node.appendChild(d_folder_v)
            annotation_node.appendChild(folder_node)

            filename = annotation.getElementsByTagName('filename')
            filename_v = filename[0].childNodes[0].data
            vect_name = filename_v.split('.')
            filename_v = vect_name[0]+'.jpg'
            filename_node = dst_domTree.createElement('filename')
            d_filename_v = dst_domTree.createTextNode(filename_v)
            filename_node.appendChild(d_filename_v)
            annotation_node.appendChild(filename_node)

            source = annotation.getElementsByTagName('source')[0]     #source
            source_node = dst_domTree.createElement('source')
            annotation_node.appendChild(source_node)

            database = source.getElementsByTagName('database')
            database_v = '0'
            database_node = dst_domTree.createElement('database')
            d_database_v = dst_domTree.createTextNode(database_v)
            database_node.appendChild(d_database_v)
            source_node.appendChild(database_node)

            size = annotation.getElementsByTagName('size')[0]              #size
            size_node = dst_domTree.createElement('size')
            annotation_node.appendChild(size_node)

            width = size.getElementsByTagName('width')
            width_v = width[0].childNodes[0].data
            width_node = dst_domTree.createElement('width')
            d_width_v = dst_domTree.createTextNode(width_v)
            width_node.appendChild(d_width_v)
            size_node.appendChild(width_node)

            height = size.getElementsByTagName('height')
            height_v = height[0].childNodes[0].data
            height_node = dst_domTree.createElement('height')
            d_height_v = dst_domTree.createTextNode(height_v)
            height_node.appendChild(d_height_v)
            size_node.appendChild(height_node)

            depth = size.getElementsByTagName('depth')
            depth_v = depth[0].childNodes[0].data
            depth_node = dst_domTree.createElement('depth')
            d_depth_v = dst_domTree.createTextNode(depth_v)
            depth_node.appendChild(d_depth_v)
            size_node.appendChild(depth_node)


            segmented = annotation.getElementsByTagName('segmented')        #segmented
            segmented_v = '0'
            segmented_node = dst_domTree.createElement('segmented')
            d_segmented_v = dst_domTree.createTextNode(segmented_v)
            segmented_node.appendChild(d_segmented_v)
            annotation_node.appendChild(segmented_node)


            object_list = annotation.getElementsByTagName('object')
            #object
           
            for objecti in object_list:
                name = objecti.getElementsByTagName('name')
                name_v = name[0].childNodes[0].data
                i_v = name_v
                flag_skip = False

                if i_v == 'doctor':
                    name_v = 'people'
                elif i_v == 'patient':
                    name_v = 'people'
                    #name_v = 'hand_mop_yellow_vehicle'
                #else:
                #    flag_skip = True
                #if flag_skip == True:
                #    continue
                '''
                if i_v == 'Protective cloth hang':
                    
                    objecti_node = dst_domTree.createElement('object')
                    annotation_node.appendChild(objecti_node)
                    
                    name_node = dst_domTree.createElement('name')
                    d_name_v = dst_domTree.createTextNode(name_v)
                    name_node.appendChild(d_name_v)
                    objecti_node.appendChild(name_node)
                    
                    pose = objecti.getElementsByTagName('pose')
                    pose_v = pose[0].childNodes[0].data
                    pose_node = dst_domTree.createElement('pose')
                    d_pose_v = dst_domTree.createTextNode(pose_v)
                    pose_node.appendChild(d_pose_v)
                    objecti_node.appendChild(pose_node)
                    
                    truncated = objecti.getElementsByTagName('truncated')
                    truncated_v = truncated[0].childNodes[0].data
                    truncated_node = dst_domTree.createElement('truncated')
                    d_truncated_v = dst_domTree.createTextNode(truncated_v)
                    truncated_node.appendChild(d_truncated_v)
                    objecti_node.appendChild(truncated_node)
                    
                    difficult = objecti.getElementsByTagName('difficult')
                    difficult_v = difficult[0].childNodes[0].data
                    difficult_node = dst_domTree.createElement('difficult')
                    d_difficult_v = dst_domTree.createTextNode(difficult_v)
                    difficult_node.appendChild(d_difficult_v)
                    objecti_node.appendChild(difficult_node)
                    
                    bndbox = objecti.getElementsByTagName('bndbox')[0]              #bndbox
                    bndbox_node = dst_domTree.createElement('bndbox')
                    objecti_node.appendChild(bndbox_node)
                    
                    
                    xmin = bndbox.getElementsByTagName('xmin')
                    xmin_v = '265'
                    xmin_node = dst_domTree.createElement('xmin')
                    d_xmin_v = dst_domTree.createTextNode(xmin_v)
                    xmin_node.appendChild(d_xmin_v)
                    bndbox_node.appendChild(xmin_node)
                    if i_v == 9:
                        w_x1 = int(xmin_v)
                
                    ymin = bndbox.getElementsByTagName('ymin')
                    ymin_v = '343'
                    ymin_node = dst_domTree.createElement('ymin')
                    d_ymin_v = dst_domTree.createTextNode(ymin_v)
                    ymin_node.appendChild(d_ymin_v)
                    bndbox_node.appendChild(ymin_node)
                    
                    xmax = bndbox.getElementsByTagName('xmax')
                    xmax_v = '511'
                    xmax_node = dst_domTree.createElement('xmax')
                    d_xmax_v = dst_domTree.createTextNode(xmax_v)
                    xmax_node.appendChild(d_xmax_v)
                    bndbox_node.appendChild(xmax_node)
                    if i_v == 9:
                        w_x2 = int(xmax_v)
        
                    ymax = bndbox.getElementsByTagName('ymax')
                    ymax_v = '596'
                    ymax_node = dst_domTree.createElement('ymax')
                    d_ymax_v = dst_domTree.createTextNode(ymax_v)
                    ymax_node.appendChild(d_ymax_v)
                    bndbox_node.appendChild(ymax_node)
                else:
                    objecti_node = dst_domTree.createElement('object')
                    annotation_node.appendChild(objecti_node)
                    
                    name_node = dst_domTree.createElement('name')
                    d_name_v = dst_domTree.createTextNode(name_v)
                    name_node.appendChild(d_name_v)
                    objecti_node.appendChild(name_node)
                    
                    pose = objecti.getElementsByTagName('pose')
                    pose_v = pose[0].childNodes[0].data
                    pose_node = dst_domTree.createElement('pose')
                    d_pose_v = dst_domTree.createTextNode(pose_v)
                    pose_node.appendChild(d_pose_v)
                    objecti_node.appendChild(pose_node)
                    
                    truncated = objecti.getElementsByTagName('truncated')
                    truncated_v = truncated[0].childNodes[0].data
                    truncated_node = dst_domTree.createElement('truncated')
                    d_truncated_v = dst_domTree.createTextNode(truncated_v)
                    truncated_node.appendChild(d_truncated_v)
                    objecti_node.appendChild(truncated_node)
                    
                    difficult = objecti.getElementsByTagName('difficult')
                    difficult_v = difficult[0].childNodes[0].data
                    difficult_node = dst_domTree.createElement('difficult')
                    d_difficult_v = dst_domTree.createTextNode(difficult_v)
                    difficult_node.appendChild(d_difficult_v)
                    objecti_node.appendChild(difficult_node)
                    
                    bndbox = objecti.getElementsByTagName('bndbox')[0]              #bndbox
                    bndbox_node = dst_domTree.createElement('bndbox')
                    objecti_node.appendChild(bndbox_node)
                    
                    
                    xmin = bndbox.getElementsByTagName('xmin')
                    xmin_v = xmin[0].childNodes[0].data
                    xmin_node = dst_domTree.createElement('xmin')
                    d_xmin_v = dst_domTree.createTextNode(xmin_v)
                    xmin_node.appendChild(d_xmin_v)
                    bndbox_node.appendChild(xmin_node)
                    if i_v == 9:
                        w_x1 = int(xmin_v)
                    
                    ymin = bndbox.getElementsByTagName('ymin')
                    ymin_v = ymin[0].childNodes[0].data
                    ymin_node = dst_domTree.createElement('ymin')
                    d_ymin_v = dst_domTree.createTextNode(ymin_v)
                    ymin_node.appendChild(d_ymin_v)
                    bndbox_node.appendChild(ymin_node)
                    
                    xmax = bndbox.getElementsByTagName('xmax')
                    xmax_v = xmax[0].childNodes[0].data
                    xmax_node = dst_domTree.createElement('xmax')
                    d_xmax_v = dst_domTree.createTextNode(xmax_v)
                    xmax_node.appendChild(d_xmax_v)
                    bndbox_node.appendChild(xmax_node)
                    if i_v == 9:
                        w_x2 = int(xmax_v)
                    
                    ymax = bndbox.getElementsByTagName('ymax')
                    ymax_v = ymax[0].childNodes[0].data
                    ymax_node = dst_domTree.createElement('ymax')
                    d_ymax_v = dst_domTree.createTextNode(ymax_v)
                    ymax_node.appendChild(d_ymax_v)
                    bndbox_node.appendChild(ymax_node)
                '''
                objecti_node = dst_domTree.createElement('object')
                annotation_node.appendChild(objecti_node)
                
                name_node = dst_domTree.createElement('name')
                d_name_v = dst_domTree.createTextNode(name_v)
                name_node.appendChild(d_name_v)
                objecti_node.appendChild(name_node)
                
                pose = objecti.getElementsByTagName('pose')
                pose_v = pose[0].childNodes[0].data
                pose_node = dst_domTree.createElement('pose')
                d_pose_v = dst_domTree.createTextNode(pose_v)
                pose_node.appendChild(d_pose_v)
                objecti_node.appendChild(pose_node)
                
                truncated = objecti.getElementsByTagName('truncated')
                truncated_v = truncated[0].childNodes[0].data
                truncated_node = dst_domTree.createElement('truncated')
                d_truncated_v = dst_domTree.createTextNode(truncated_v)
                truncated_node.appendChild(d_truncated_v)
                objecti_node.appendChild(truncated_node)
                
                difficult = objecti.getElementsByTagName('difficult')
                difficult_v = difficult[0].childNodes[0].data
                difficult_node = dst_domTree.createElement('difficult')
                d_difficult_v = dst_domTree.createTextNode(difficult_v)
                difficult_node.appendChild(d_difficult_v)
                objecti_node.appendChild(difficult_node)
                
                bndbox = objecti.getElementsByTagName('bndbox')[0]              #bndbox
                bndbox_node = dst_domTree.createElement('bndbox')
                objecti_node.appendChild(bndbox_node)
                
                
                xmin = bndbox.getElementsByTagName('xmin')
                xmax = bndbox.getElementsByTagName('xmax')
                
                width_v1=width_v.encode("utf-8")
                width_v1_int=int(width_v1)
                
                #plainstring1 = unicode(utf8string, "utf-8")
                
                xmin_v = xmin[0].childNodes[0].data
                xmin_v1=xmin_v.encode("utf-8")
                xmin_v1_int=int(xmin_v1)
                #print(xmin_v1_int)
                #print(type(xmin_v1_int))
                
                
                xmax_v = xmax[0].childNodes[0].data
                xmax_v1=xmax_v.encode("utf-8")
                xmax_v1_int=int(xmax_v1)
                
                xmin_v2_int = width_v1_int -xmax_v1_int
                xmin_v2 = unicode(str(xmin_v2_int), "utf-8")
                xmax_v2_int = width_v1_int -xmin_v1_int
                xmax_v2 = unicode(str(xmax_v2_int), "utf-8")
                
                xmin_node = dst_domTree.createElement('xmin')
                d_xmin_v = dst_domTree.createTextNode(xmin_v2)
                xmin_node.appendChild(d_xmin_v)
                bndbox_node.appendChild(xmin_node)
                if i_v == 9:
                    w_x1 = int(xmin_v)

                        
                ymin = bndbox.getElementsByTagName('ymin')
                ymin_v = ymin[0].childNodes[0].data
                ymin_node = dst_domTree.createElement('ymin')
                d_ymin_v = dst_domTree.createTextNode(ymin_v)
                ymin_node.appendChild(d_ymin_v)
                bndbox_node.appendChild(ymin_node)
                
                xmax_node = dst_domTree.createElement('xmax')
                d_xmax_v = dst_domTree.createTextNode(xmax_v2)
                xmax_node.appendChild(d_xmax_v)
                bndbox_node.appendChild(xmax_node)
                if i_v == 9:
                    w_x2 = int(xmax_v)
        
                ymax = bndbox.getElementsByTagName('ymax')
                ymax_v = ymax[0].childNodes[0].data
                ymax_node = dst_domTree.createElement('ymax')
                d_ymax_v = dst_domTree.createTextNode(ymax_v)
                ymax_node.appendChild(d_ymax_v)
                bndbox_node.appendChild(ymax_node)
        
                
            
            '''
            objecti_node = dst_domTree.createElement('object')
            annotation_node.appendChild(objecti_node)
                
            name_node = dst_domTree.createElement('name')
            d_name_v = dst_domTree.createTextNode('Protective cloth hang')
            name_node.appendChild(d_name_v)
            objecti_node.appendChild(name_node)
                
            pose = objecti.getElementsByTagName('pose')
            pose_v = pose[0].childNodes[0].data
            pose_node = dst_domTree.createElement('pose')
            d_pose_v = dst_domTree.createTextNode(pose_v)
            pose_node.appendChild(d_pose_v)
            objecti_node.appendChild(pose_node)
                
            truncated = objecti.getElementsByTagName('truncated')
            truncated_v = truncated[0].childNodes[0].data
            truncated_node = dst_domTree.createElement('truncated')
            d_truncated_v = dst_domTree.createTextNode(truncated_v)
            truncated_node.appendChild(d_truncated_v)
            objecti_node.appendChild(truncated_node)
                
            difficult = objecti.getElementsByTagName('difficult')
            difficult_v = difficult[0].childNodes[0].data
            difficult_node = dst_domTree.createElement('difficult')
            d_difficult_v = dst_domTree.createTextNode(difficult_v)
            difficult_node.appendChild(d_difficult_v)
            objecti_node.appendChild(difficult_node)
                
            bndbox = objecti.getElementsByTagName('bndbox')[0]              #bndbox
            bndbox_node = dst_domTree.createElement('bndbox')
            objecti_node.appendChild(bndbox_node)
                
            #xmin = bndbox.getElementsByTagName('xmin')
            xmin_v = '285'
            xmin_node = dst_domTree.createElement('xmin')
            d_xmin_v = dst_domTree.createTextNode(xmin_v)
            xmin_node.appendChild(d_xmin_v)
            bndbox_node.appendChild(xmin_node)
        
            #ymin = bndbox.getElementsByTagName('ymin')
            ymin_v = '367'
            ymin_node = dst_domTree.createElement('ymin')
            d_ymin_v = dst_domTree.createTextNode(ymin_v)
            ymin_node.appendChild(d_ymin_v)
            bndbox_node.appendChild(ymin_node)
                
            #xmax = bndbox.getElementsByTagName('xmax')
            xmax_v = '473'
            xmax_node = dst_domTree.createElement('xmax')
            d_xmax_v = dst_domTree.createTextNode(xmax_v)
            xmax_node.appendChild(d_xmax_v)
            bndbox_node.appendChild(xmax_node)
            
            #ymax = bndbox.getElementsByTagName('ymax')
            ymax_v = '540'
            ymax_node = dst_domTree.createElement('ymax')
            d_ymax_v = dst_domTree.createTextNode(ymax_v)
            ymax_node.appendChild(d_ymax_v)
            bndbox_node.appendChild(ymax_node)
            '''

            print('dst_xml',dst_xml)
            #f = file(dst_xml, 'wb')
            f = open(dst_xml, 'wb')
            dst_domTree.writexml(f,addindent='    ', newl='\n')
            f.close()
            #with open(dst_xml, 'w') as f:
                #dst_domTree.writexml(f,encoding='utf-8')
            #f.close()
                 
                           
            

if __name__ == '__main__':

    base_path = '/Users/zhangjiaxuan/Desktop/test_xml/'
    dst_txt_path = '/Users/zhangjiaxuan/Desktop/save_xml/'

    change_xml(base_path, dst_txt_path)




