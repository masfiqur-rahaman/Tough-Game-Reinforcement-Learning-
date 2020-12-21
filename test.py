import numpy as np
import cv2
from PIL import Image

vertices = np.array(
        [[0,0], [0,15], [9, 15], [9, 12], [31, 12], [31, 2], [33,2], [33, 15], [39,15], [39,0], [29,0], [29,2], [7,2], [7,12], [5,12], [5,0]],
        np.int32
    )
print(vertices)

# pts = vertices.reshape((-1, 1, 2))
# print(pts)
isClosed = True
color = (255,0,0)
thickness = 1

env = np.zeros((20, 44, 3), dtype=np.uint8)
# img = Image.fromarray(env, 'RGB')
img = cv2.polylines(env, [vertices], isClosed, color, thickness)
img = cv2.putText(np.array(img), "o", (5, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                          fontScale=.1, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)
img = cv2.resize(img, (440, 200))
# Displaying the image
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break