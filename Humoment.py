#Nhom12B#Nhom12B#Nhom12B#Nhom12B#Nhom12B
#Nhom12B                        #Nhom12B
#Nhom12B                        #Nhom12B
#Nhom12B#Nhom12B#Nhom12B#Nhom12B#Nhom12B
import cv2
import sys
import os
from math import copysign, log10

def main():
    showLogTransformedHuMoments = True

    folder_name = "class1"
    output_folder = "output_images"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_files = sorted([f for f in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, f))], key=lambda x: int(os.path.splitext(x)[0]))

    print(f"{'ID':<4} {'S1':>10} {'S2':>10} {'S3':>10} {'S4':>13} {'S5':>13} {'S6':>13} {'S7':>10}")

    for idx, filename in enumerate(image_files, start=1):
        file_path = os.path.join(folder_name, filename)
        im = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        _, im_binary = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY_INV)  # Sử dụng THRESH_BINARY_INV để đảo ngược
        moment = cv2.moments(im_binary)
        huMoments = cv2.HuMoments(moment)

        print(f"{idx:<4}", end='')

        for i in range(0, 7):
            hu_value = huMoments[i][0]
            if showLogTransformedHuMoments:
                hu_value = -1 * copysign(1.0, hu_value) * log10(abs(hu_value))
            print(f"{hu_value:>12.5f}", end=' ')
        print()

        if idx <= 5:
            output_path = os.path.join(output_folder, f"binary_image_{idx}.png")
            cv2.imwrite(output_path, im_binary)
#Nhom12B
if __name__ == "__main__": #Nhom12B
    main()