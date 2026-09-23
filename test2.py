import cv2
color = cv2.imread('road.jpg')
gray = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)
grayPath = 'road_gray.jpg'

saveResult = cv2.imwrite(grayPath, gray) # saveResult : 저장 성공 여부

if saveResult:
    print(f'Image saved successfully at {grayPath}')
    # gray2 = cv2.imread(grayPath) #채널 수 3개
    gray2 = cv2.imread(grayPath, cv2.IMREAD_GRAYSCALE) # 채널 수 1개로 만들기
    print('shape:', gray2.shape) # gray2 = cv2.imread(grayPath) 이거 일 때는 채널 수 3개
    print('gray dhape', gray.shape)
    # 기능구현


    cv2.imshow('GRAY',gray2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Fail to save image')
# ok = cv2.imwrite('path', gray) # ok : 저장 성공 여부
# chechk = cv2.imread('path', cv2.IMREAD_GRAYSCALE) # check : 저장된 이미지 읽기
