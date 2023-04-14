import cv2
import numpy as np

if __name__ == "__main__":

    im = cv2.imread("images/moire-alpha-mask.jpg", cv2.IMREAD_GRAYSCALE)
    im = im > 0.5
    im.astype(float)
    im = np.array([im] * 4)
    

    print(im.shape)
    cv2.imwrite("out/test.png", im)
