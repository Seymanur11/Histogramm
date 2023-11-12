import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = 'image.jpg'
color_image = cv2.imread(image_path)

if color_image is None:
    print(f'Hata: Görüntü "{image_path}" yüklenemedi.')
else:
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    plt.figure('Figure1')
    plt.imshow(gray_image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.show()

    histogram, bins = np.histogram(gray_image.flatten(), bins=256, range=[0,256])

    plt.figure('Figure2')
    plt.bar(bins[:-1], histogram, color='gray', alpha=0.7)
    plt.title('Gri Seviye Görüntü Histogramı')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Sıklık')
    plt.show()