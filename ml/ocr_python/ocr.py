"""
Use opencv-python for OCR pre-processing.
1) Image Inversion
2) Rescaling TODO
3) Binarization
4) Noise Removal
5) Dilation and Erosion
6) Rotation/Deskewing
7) Removing Borders
8) Add Missing Borders
9) Transparency/Alpha Channel TODO

Lastly, use PyTesseract for OCR.

Video Tutorials:
- https://www.youtube.com/watch?v=ADV-AjAXHdc&list=PLGQnPU9E4ZnYhtlmx52yqItsR_V35RlCT&index=2
- https://www.youtube.com/watch?v=4uWp6dS6_G4&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i&index=5
"""
import cv2
import numpy as np
import pytesseract

image_file = "data/page_01.jpg"
img = cv2.imread(image_file)

# CV2 (opencv-python) has a nice built-in image viewer
cv2.imshow("og image", img)
cv2.waitKey(0)

#########
# 1) Image Inversion
# White -> Black
#########
img_inverted = cv2.bitwise_not(img)
cv2.imwrite("transformed/inverted_page_01.jpg", img_inverted)

#########
# 2) Rescaling TODO
#########

#########
# 3) Binarization
# Process of converting an image to black and white. This greatly reduces the noise!
# Converts beige shades to white and various gray shades to black.
#########
# First convert to grayscale.
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img_gray = grayscale(img)
cv2.imwrite("transformed/gray_page_01.jpg", img_gray)

threshold, img_bw = cv2.threshold(img_gray, 200, 230, cv2.THRESH_BINARY)
cv2.imwrite("transformed/bw_page_01.jpg", img_bw)

#########
# 4) Noise Removal
# Remove various spots that don't correspond to characters.
#########
def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

img_no_noise = noise_removal(img_bw)
cv2.imwrite("transformed/no_noise_page_01.jpg", img_no_noise)

#########
# 5) Dilation and Erosion
# Adjusts font sizes (make them thicker or thinner)
#########
# Dilation/Erosion are intended for inverted images (black backgrounds)
# So we invert them, then revert them
def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image

img_eroded = thin_font(img_no_noise)
cv2.imwrite("transformed/eroded_page_01.jpg", img_eroded)


def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image

img_dilated= thin_font(img_no_noise)
cv2.imwrite("transformed/dilated_page_01.jpg", img_dilated)


#########
# 6) Rotation and Deskewing
# Note: border need to be removed first.
#########
img_rotated = cv2.imread("data/page_01_rotated.jpg")

#https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df
def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print ("Num contours:", len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("transformed/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle

def rotateImage(cvImage, angle: float):
    """ Rotate the image around its center """
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)

img_deskewed = deskew(img_rotated)
cv2.imwrite("transformed/deskewed_page_01.jpg", img_deskewed)


#########
# 7) Remove Borders
#########
def remove_borders(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    return crop

img_no_borders = remove_borders(img_no_noise)
cv2.imwrite("transformed/no_borders_page_01.jpg", img_no_borders)


#########
# 8) Add Missing Borders
# Do this if the text is right up against the edge of the image.
# Add border of white padding.
#########
color = [255, 255, 255]  # white
top, bottom, left, right = [150]*4

img_with_border = cv2.copyMakeBorder(img_no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
cv2.imwrite("transformed/with_border_page_01.jpg", img_with_border)


#########
# PyTesseract OCR
#########

raw_img_txt = pytesseract.image_to_string("data/page_01.jpg")
print("\nRAW IMAGE TEXT")
print(raw_img_txt)

preprocessed_img_txt = pytesseract.image_to_string("transformed/no_noise_page_01.jpg")
print("\nPRE-PROCESSED IMAGE TEXT")
print(preprocessed_img_txt)
