import cv2
from pyzbar.pyzbar import decode

def BarcodeReader(image_path):
    # Read the image in numpy array using cv2
    img = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if img is None:
        print("Error: Unable to load image. Check the file path.")
        return

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If no barcodes are detected, print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        # Traverse through all the detected barcodes in the image
        for barcode in detectedBarcodes:
            # Locate the barcode position in the image
            (x, y, w, h) = barcode.rect

            # Draw a rectangle around the barcode using cv2
            cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)

            # Print the barcode data and type
            print("Data:", barcode.data.decode('utf-8'))
            print("Type:", barcode.type)

    # Display the image with the barcode highlighted
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the image
    image_path = "Img.jpg"
    BarcodeReader(image_path)
