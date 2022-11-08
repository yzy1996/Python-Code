# 一文解释 图像读取

> 希望通过本文帮助你了解一些基础用法，本质数据类型。常用的库包括了`Pillow`,`OpenCV`,`Matplotlib`,`torchvision`.





## Pillow

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

```python
from PIL import Image

# read
pil_img = Image.open("your_image.jpg")  # RGB

# grayscale
pil_img = Image.open("your_image.jpg").convert("L")

# save
pil_img.save("new_image.jpg")

# save a JPEG image with specific quality
pil_img.save("new_image.jpg", quality=95)
```



```python
# Pillow image to OpenCV image

cv2_img = np.array(pil_img)
cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
```



## Opencv

>  OpenCV images are actually NumPy arrays

```python
import cv2

img = cv2.imread("your_image.jpg")  # BGR

img = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite("new_image.jpg", img)

cv2.imwrite("new_image.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])


cv.imshow(img)
cv.waitKey(0)
```

```python
# OpenCV image to Pillow image

cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(cv2_img
```



## Matplotlib

学习资料

https://github.com/rougier/matplotlib-tutorial

https://github.com/matplotlib/cheatsheets

https://github.com/matplotlib/cheatsheets

```python

plt.show()
```



ref: https://medium.com/analytics-vidhya/the-ultimate-handbook-for-opencv-pillow-72b7eff77cd7



