import cv2

path = str('road.jpg')
color = cv2.imread(path)

gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
threshold_value = gray.mean() # 평균값으로 임계값 설정
print(gray.min(), gray.max(), gray.mean())
# threshold_value = 120
_, binary = cv2.threshold(gray, threshold_value, 255,cv2.THRESH_BINARY)
cv2.imshow('GRAY', gray)
cv2.imshow('BINARY', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()