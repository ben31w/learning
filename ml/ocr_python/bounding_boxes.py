"""
OCR pre-processing for a PDF with 3 columns of text.
This involves different pre-processing techniques to find regions of interest
(ROIs).

Pre-processing steps:
1) Grayscale
2) Blur
3) Threshold (black and white)
4) Dilation

After pre-processing, find contours/bounding boxes/ROIs (opencv-python) and
do OCR (pytesseract).

Video tutorials:
- https://www.youtube.com/watch?v=9FCw1xo_s0I&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i&index=7
- https://www.youtube.com/watch?v=y1iw8c2CEgw&t=645s
"""
import cv2
import pytesseract

img = cv2.imread("data/index_02.jpg")

########## PRE-PROCESSING ##########

# 1) Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("transformed/gray_index_02.jpg", img_gray)

# 2) Blur
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
cv2.imwrite("transformed/blurred_index_02.jpg", img_blur)

# 3) Threshold (black and white)
img_bw = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite("transformed/bw_index_02.jpg", img_bw)

# 4) Dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
img_dilated = cv2.dilate(img_bw, kernel, iterations=1)
cv2.imwrite("transformed/dilated_index_02.jpg", img_dilated)


########## CONTOURS -> OCR ##########
# Find contours, and draw rectangles on top of the relevant (large enough) contours.

def ocr_roi(roi_img):
    """ Perform OCR on a region of interest. Print non-blank lines. """
    ocr_result = pytesseract.image_to_string(roi_img)
    lines = ocr_result.split("\n")
    for line in lines:
        line = line.strip()
        if line != "":
            print(line)

cnts = cv2.findContours(img_dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

green = (36, 255, 12)
roi_idx = 0
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if h > 200 and w > 20:
        roi = img[y:y+h, x:x+w]
        cv2.imwrite(f"transformed/roi_{roi_idx}_index_02.jpg", roi)
        cv2.rectangle(img, (x,y), (x+w, y+h), green, 2)

        print(f"---COL {roi_idx}---")
        ocr_roi(roi)
        roi_idx += 1
cv2.imwrite("transformed/bbox_index_02.jpg", img)


