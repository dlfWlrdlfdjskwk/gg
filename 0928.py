import cv2

path = str('road.jpg')
color = cv2.imread(path)
cv2.imshow('COLOR', color)
result = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
result = cv2.resize(result, (400, 300))
print(result.min(), result.max(), result.mean())
cv2.imshow('GRAY', result)
cv2.waitKey(0)
cv2.destroyAllWindows()