import cv2
import glob

images=glob.glob("*.png")

for image in images:
    img=cv2.imread(image)
    re=cv2.resize(img,(1400))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("done/"+image+".jpg", re)