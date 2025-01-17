from Object import *
from PIL import Image
import cv2
import pygame

class Environment:
    # SIZE = 30  # It was 10 before


    # Polygon environment---------------
    # height = 22
    # width = 46
    # # 20X12
    # vertices = np.array(
    #     [[0, 0], [0, 21], [12, 21], [12, 17], [37, 17], [37, 4], [39, 4], [39, 21], [45, 21], [45, 0], [33, 0], [33, 4],
    #      [8, 4], [8, 17], [6, 17], [6, 0]],
    #     np.int32
    # )

    height = 20
    width = 56
    # 20X4
    vertices = np.array(
        [[0, 0], [0, 19], [16, 19], [16, 16], [43, 16], [43, 4], [45, 4], [45, 19], [55, 19], [55, 0], [39, 0], [39, 3],
         [12, 3], [12, 15], [10, 15], [10, 0]],
        np.int32
    )
    isClosed = True
    color = (255, 0, 0)
    thickness = 1
    #-----------------------------------

    window_width = 570
    window_height = 260
    n_enemies = 4
    enemies = np.ndarray(n_enemies, dtype=Object)
    RETURN_IMAGES = True
    MOVE_PENALTY = 1
    ENEMY_PENALTY = 300
    FOOD_REWARD = 25
    OBSERVATION_SPACE_VALUES = (height, width, 3)  # 4
    ACTION_SPACE_SIZE = 9
    PLAYER_N = 1  # player key in dict
    FOOD_N = 2  # food key in dict
    ENEMY_N = 3  # enemy key in dict
    # the dict! (colors)
    d = {1: (255, 175, 0),
         2: (0, 255, 0),
         3: (0, 0, 255)}

    def reset(self, ENEMY_SPEED=1):
        self.player = Object(self.height, self.width, "player", vertices=self.vertices)
        self.food = Object(self.height, self.width, "food", vertices=self.vertices)
        # while self.food == self.player:
        #     self.food = Object(self.height, self.width, "food")
        for i in range(self.n_enemies):
            self.enemies[i] = Object(self.height, self.width, "enemy", vertices=self.vertices, object_id=i, n_objects=self.n_enemies, ENEMY_SPEED=ENEMY_SPEED)
            # print(self.enemies[i])
            # print(i, self.enemies[i])
        # while self.enemy == self.player or self.enemy == self.food:
        #     self.enemy = Object(self.height, self.width, "enemy")

        self.episode_step = 0

        if self.RETURN_IMAGES:
            observation = np.array(self.get_image())
        else:
            observation = (self.player-self.food) + (self.player-self.enemy)
        return observation

    def step(self, action):
        self.episode_step += 1
        self.player.action(action)
        for i in range(self.n_enemies):
            self.enemies[i].enemyAction()

        #### MAYBE ###
        #enemy.move()
        #food.move()
        ##############

        if self.RETURN_IMAGES:
            new_observation = np.array(self.get_image())
        else:
            new_observation = (self.player-self.food) + (self.player-self.enemy)

        flag = False
        for i in range(self.n_enemies):
            if self.player == self.enemies[i]:
                reward = -self.ENEMY_PENALTY
                flag = True
                break
        if not flag:
            if self.player == self.food:
                reward = self.FOOD_REWARD
            else:
                reward = -self.MOVE_PENALTY

        done = False
        if reward == self.FOOD_REWARD or reward == -self.ENEMY_PENALTY or self.episode_step >= 200:
            done = True

        return new_observation, reward, done

    # def init_render(self):
    #     import pygame
    #     pygame.init()
    #     self.window = pygame.display.set_mode((self.window_width, self.window_height))
    #     self.clock = pygame.time.Clock()

    # def cvimage_to_pygame(image):
    #     """Convert cvimage into a pygame image"""
    #     return pygame.image.frombuffer(image.tostring(), image.shape[1::-1], "RGB")

    def render(self, episode=-1, score=-1):
        img = self.get_image()
        img = cv2.resize(img, (self.window_width, self.window_height))  # resizing so we can see our agent in all its glory.
        img = cv2.putText(np.array(img), "Episode: "+str(episode), (0,15), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.5,
                  color=(0,0,255), thickness=1, lineType=cv2.LINE_AA)
        img = cv2.putText(np.array(img), "Score: " + str(score), (self.window_width-100, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                          fontScale=.5, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # img = cv2.putText(np.array(img), 'OpenCV Tuts!', (0, 130), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
        # cv2.imshow("image", np.array(img))  # show it!
        cv2.imshow("ToughG", img)  # show it!
        cv2.waitKey(1)

    # FOR CNN #
    def get_image(self):
        # print(self.player.x, self.player.y)
        env = np.zeros((self.height, self.width, 3), dtype=np.uint8)  # starts an rbg of our size
        img = cv2.polylines(env, [self.vertices], self.isClosed, self.color, self.thickness)

        # env[self.food.y][self.food.x] = self.d[self.FOOD_N]  # sets the food location tile to green color
        start_point = (self.food.x - 1, self.food.y - 1)
        end_point = (self.food.x + 1, self.food.y + 1)
        img = cv2.rectangle(img, start_point, end_point, color=self.d[self.FOOD_N], thickness=-1)
        for i in range(self.n_enemies):
            # print(self.enemies[i].x, self.enemies[i].y)
            # env[self.enemies[i].y][self.enemies[i].x] = self.d[self.ENEMY_N]  # sets the enemy location to red
            img = cv2.circle(img, (self.enemies[i].x, self.enemies[i].y), radius=1, color=self.d[self.ENEMY_N], thickness=-1)
        # env[self.player.y][self.player.x] = self.d[self.PLAYER_N]  # sets the player tile to blue

        start_point = (self.player.x - 1, self.player.y - 1)
        end_point = (self.player.x + 1, self.player.y + 1)
        # print(start_point, end_point)
        img = cv2.rectangle(img, start_point, end_point, color=self.d[self.PLAYER_N], thickness=-1)

        # img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
        return img