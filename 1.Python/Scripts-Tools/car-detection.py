
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import cvlib.object_detection import draw_bbox
im = cv2.imread('cars _ image. jpeg')

bbox, label, conf = cvimagedetect_common_objects(im)
output_image = draw_bbox( im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print( 'Number of cars in the image is '+
                str( label. count('car')))
                
