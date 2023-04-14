import cv2
import numpy as np

if __name__ == "__main__":

    im = cv2.imread("images/moire-alpha-mask.jpg", cv2.IMREAD_GRAYSCALE)
    im = np.where(im > 256/2, 255, 0)
    im = np.array([im] * 4)
    
    im = np.moveaxis(im, [0], [2])

    bw = im[:,:,0]
    im[:,:,3] = np.where(bw == 0, 255, 0)
    
    cv2.imwrite("out/test.png", im)
    print("done")