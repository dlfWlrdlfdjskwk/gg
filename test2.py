import cv2
color = cv2.imread('road.jpg')
gray = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)
grayPath = 'road_gray.jpg'

saveResult = cv2.imwrite(grayPath, gray) # saveResult : 저장 성공 여부

if saveResult:
    print(f'Image saved successfully at {grayPath}')
    gray2 = cv2.imread(grayPath)
    cv2.imshow('GRAY',gray2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Fail to save image')
# ok = cv2.imwrite('path', gray) # ok : 저장 성공 여부
# chechk = cv2.imread('path', cv2.IMREAD_GRAYSCALE) # check : 저장된 이미지 읽기
