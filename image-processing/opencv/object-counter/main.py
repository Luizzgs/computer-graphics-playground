import cv2
import imutils
import numpy as np

def is_circular(contour, min_circularity=0.6):
    area = cv2.contourArea(contour)
    print('area:', area)
    
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return False
    circularity = 4 * np.pi * (area / (perimeter ** 2))
    return circularity > min_circularity




image = cv2.imread("images/moedas/m5.jpg")
image = cv2.resize(image, (600, 600))
cv2.imshow("1 original", image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("2 gray", image_gray)

image_blur = cv2.medianBlur(image_gray, 1)
#cv2.imshow("3 mediana", image_blur)

image_res ,image_thresh = cv2.threshold(image_blur,230,255,cv2.THRESH_BINARY_INV + 
                                            cv2.THRESH_OTSU)
print("Limiar: ", image_res)
cv2.imshow("4 limiar", image_thresh)

kernel = np.ones((5,5),np.uint8)
morpho = cv2.morphologyEx(image_thresh,cv2.MORPH_DILATE ,kernel)
cv2.imshow("5 morfologia: ", morpho)

kernel2 = np.ones((5,5),np.uint8)
morpho = cv2.morphologyEx(morpho,cv2.MORPH_DILATE ,kernel2)
cv2.imshow("6 morfologia: ", morpho)

cnts = cv2.findContours(morpho.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)

min_area = 3100
filtered_cnts = []
for c in cnts:
    if cv2.contourArea(c) > min_area:
        if is_circular(c):
            filtered_cnts.append(c)

objects = str(len(filtered_cnts))
text = "Objetos encontrados:" + objects
cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

for c in filtered_cnts:
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

print(objects)
cv2.imshow("5 contagem", image)

cv2.waitKey(0)