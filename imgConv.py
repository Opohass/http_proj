import cv2
# from keras.datasets import mnist

def getImageAsArray(path):

    # img = cv2.imread(path)
    img = cv2.imdecode(path, cv2.IMREAD_UNCHANGED)

    height,width=img.shape[:2]
    if height!=28 or width!=28: #convet the image to 28X28
        img=cv2.resize(img,(28,28))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('jack_nicholson_gray.png', img_gray) #only if we want the option to save an image FIXME:  get image name
    #TESTS:
    # print(img_gray.shape)
    # print(img_gray.reshape(img_gray.shape[0]*img_gray.shape[1]).shape)

    return img_gray.reshape(img_gray.shape[0]*img_gray.shape[1])

# getImageAsArray('./unitTest/imgTst/img2.png')
