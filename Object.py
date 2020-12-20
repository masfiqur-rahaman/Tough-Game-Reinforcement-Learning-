import numpy as np

class Object:
    def __init__(self, WIDTH, HEIGHT, object_type, object_id=None, n_objects=None, ENEMY_SPEED=1):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        if object_type == "player":
            self.x = int(self.WIDTH/2)
            self.y = 0
        elif object_type == "food":
            self.x = int(self.WIDTH/2)
            self.y = int(self.HEIGHT-1)
        elif object_type == "enemy":
            self.ENEMY_SPEED = ENEMY_SPEED
            lower = int(self.WIDTH/3)
            upper = self.WIDTH-lower
            if n_objects==1:
                self.y = int(self.HEIGHT/2)
            else:
                self.y = int(lower + object_id*(upper-lower)/(n_objects-1))
            # print("object_id", object_id)
            if object_id % 2==0:
                # training
                self.x = np.random.randint(0, self.WIDTH)
                # testing
                # self.x = 0
                self.enemy_direction = 1
            else:
                # training
                self.x = np.random.randint(0, self.WIDTH)
                # testing
                # self.x = self.WIDTH-1
                self.enemy_direction = -1
            # self.y = int(self.HEIGHT/2)
            # self.enemy_direction = 1
        else:
            print("Object type not recogized")
            exit()
        # self.x = np.random.randint(0, self.WIDTH)
        # self.y = np.random.randint(0, self.HEIGHT)

    def __str__(self):
        return f"Blob ({self.x}, {self.y})"

    def __sub__(self, other):
        return (self.x-other.x, self.y-other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def action(self, choice):
        '''
        Gives us 9 total movement options. (0,1,2,3,4,5,6,7,8)
        '''
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)

        elif choice == 4: # right
            self.move(x=1, y=0)
        elif choice == 5: # left
            self.move(x=-1, y=0)

        elif choice == 6: # forward
            self.move(x=0, y=1)
        elif choice == 7: # backward
            self.move(x=0, y=-1)

        elif choice == 8: # no movement
            self.move(x=0, y=0)

    def enemyAction(self):
        if self.enemy_direction == 1:
            self.move(x=self.ENEMY_SPEED, y=0, isEnemy=True)
        elif self.enemy_direction == -1:
            self.move(x=-self.ENEMY_SPEED, y=0, isEnemy=True)



    def move(self, x=False, y=False, isEnemy=False):

        # # If no value for x, move randomly
        # if not x:
        #     self.x += np.random.randint(-1, 2)
        # else:
        #     self.x += x
        #
        # # If no value for y, move randomly
        # if not y:
        #     self.y += np.random.randint(-1, 2)
        # else:
        #     self.y += y
        if isEnemy:
            self.x += x
            self.y += y
            # If we are out of bounds, fix!
            if self.x < 0:
                self.x = 1
                self.enemy_direction *= -1
            elif self.x > self.WIDTH - 1:
                self.x = self.WIDTH - 2
                self.enemy_direction *= -1

        else:
            # Human play
            self.x += x
            self.y += y

            # Model play
            """
            # If no value for x, move randomly
            if not x:
                self.x += np.random.randint(-1, 2)
            else:
                self.x += x
            # If no value for y, move randomly
            if not y:
                self.y += np.random.randint(-1, 2)
            else:
                self.y += y
            """


            # If we are out of bounds, fix!
            if self.x < 0:
                self.x = 0
            elif self.x > self.WIDTH - 1:
                self.x = self.WIDTH - 1

            if self.y < 0:
                self.y = 0
            elif self.y > self.HEIGHT - 1:
                self.y = self.HEIGHT - 1


