import cv2

def getImageAsArray(path):
    #TODO: convert the picture to black and white ---- digit dataset in sklearn
    img = cv2.imread(path) #FIXME: change to path
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('jack_nicholson_gray.png', img_gray) #only if we want the option to save an image FIXME:  get image name

    # data = cv2.imread('jack_nicholson_gray.png',cv2.IMREAD_GRAYSCALE)
    #TESTS:
    print(img_gray.shape)
    print(img_gray.reshape(img_gray.shape[0]*img_gray.shape[1]).shape)

    # return img_gray.reshape(img_gray.shape[0]*img_gray.shape[1])

getImageAsArray('./unitTest/imgTst/img2.png')