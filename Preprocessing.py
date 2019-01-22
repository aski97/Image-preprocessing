
#Use prewitt operator fo processing the image
# rem_mean:Bool if true allow to remove the mean from the image
# normalize:Bool if true normalize the image
def prewitt(img,width,height, rem_mean=False,normalize=True):
    import numpy as np
    from scipy.signal import convolve2d

    img = np.reshape(img,(height,width))
    if normalize:
        img=img/255.0
    if rem_mean:
        img -=np.mean(img)

    Hx = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])

    Hy = np.array([[-1, -1, -1],
                   [0, 0, 0],
                   [1, 1, 1]])

    img_x = convolve2d(img, Hx,'same')
    img_y = convolve2d(img, Hy,'same')

    img_out =1-np.sqrt(img_x**2 + img_y**2)

    return img_out


#Use roberts operator fo processing the image
# rem_mean:Bool if true allow to remove the mean from the image
# normalize:Bool if true normalize the image
def roberts(img,width,height, rem_mean=False,normalize=True):
    import numpy as np
    from scipy.signal import convolve2d

    img = np.reshape(img, (height, width))
    if normalize:
        img = img / 255.0
    if rem_mean:
        img -= np.mean(img)

    Hx = np.array([[1, 0],
                   [0, -1]])

    Hy = np.array([[0, +1],
                   [-1, 0]])

    img_x = convolve2d(img, Hx,'same')
    img_y = convolve2d(img, Hy,'same')

    img_out = 1 - np.sqrt(img_x ** 2 + img_y ** 2)

    return img_out
