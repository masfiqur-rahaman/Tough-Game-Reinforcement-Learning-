import numpy as np
from PIL import Image
import cv2



# env = np.zeros((10, 10, 3), dtype=np.uint8)  # starts an rbg of our size
# env[9][1] = 255  # sets the food location tile to green color
# # env[self.enemy.x][self.enemy.y] = self.d[self.ENEMY_N]  # sets the enemy location to red
# # env[self.player.x][self.player.y] = self.d[self.PLAYER_N]  # sets the player tile to blue
# img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
#
# img = img.resize((300, 300))  # resizing so we can see our agent in all its glory.
# cv2.imshow("image", np.array(img))  # show it!
# cv2.waitKey(100000)

for i in range(100):
    print(np.random.randint(0,2))