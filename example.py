from matplotlib import pyplot as plt
import cv2
import Preprocessing

def plot_examples(path):
    img = cv2.imread(
        path,
        cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]
    img_prewitt=Preprocessing.prewitt(img,width,height,True)
    img_roberts= Preprocessing.roberts(img,width,height,True)
    plt.imshow(img_prewitt, cmap = 'Greys')
    plt.title('Prewitt operator')
    plt.show()
    plt.imshow(img_roberts, cmap='Greys')
    plt.title('Roberts operator')
    plt.show()

plot_examples('images/prova.jpg')
