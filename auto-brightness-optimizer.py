import cv2

img = cv2.imread('./data/bird.jpg')
mean = img.mean()
fixed = cv2.convertScaleAbs(img, alpha = 150 / mean)

print('Old mean:', int(mean))
print('New mean:', int(fixed.mean()))
cv2.imwrite('./data/bird-brightned.jpg', fixed)
