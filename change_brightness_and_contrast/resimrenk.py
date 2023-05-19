#change the brightness and contrast of pictures

import cv2
import os

# read the input image 
folder ="images"
output_folder ="kaydet" # saving folder

for file_name in os.listdir(folder):
    path_name=os.path.join(folder,file_name)
    image = cv2.imread(path_name)
    # cv2.imshow("orjinal",image)
    # define the alpha and beta
    alpha = 1.5 # Contrast control
    beta = 10 # Brightness control

    # call convertScaleAbs function
    adjusted = cv2.convertScaleAbs(image, 
                                   alpha=alpha, 
                                   beta=beta)

    # display the output image
    # cv2.imshow('adjusted', adjusted)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    imgName = file_name

    cv2.waitKey(0)

    output_path_name = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path_name, adjusted)
    
cv2.destroyAllWindows()
