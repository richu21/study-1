

from PIL import Image
import os 
import imagehash

flag  = 0
orginal_tilt_img= Image.open("munnar-mod.jpg")
rot_img = imagehash.average_hash(Image.open('munnar-mod5.jpg')) 

for angle in range(361) :
    rotated_image1 = orginal_tilt_img.rotate(angle)
    rotated_image1.save('temp.jpg')
    tempimg = imagehash.average_hash(Image.open('temp.jpg')) 
    
    if rot_img - tempimg == 0:
        flag = 1
        os.remove('temp.jpg')
        break
    os.remove('temp.jpg')

if flag == 1 :
    print("Tilted Angle " + str(angle))
else :
    print("images are not similar")



