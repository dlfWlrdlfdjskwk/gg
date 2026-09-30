# 빼놓을 수 없는 히스토그램
# 가로축은 0~255 밝기 값, 세로축은 픽셀 수
import cv2
import matplotlib.pyplot as plt

color = cv2.imread('road.jpg')
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
print('hist.shape :', hist.shape)
eq = cv2.equalizeHist(gray)

cv2.imshow('gray', gray)
cv2.imshow('eq', eq)

print(gray.min(), gray.max(), round(gray.mean()), 1)
print(eq.min(), eq.max(), round(eq.mean()), 1)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(hist, color='red')

plt.plot(hist, color='gray')
plt.xlim([0,256])
plt.show()