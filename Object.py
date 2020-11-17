import numpy as np

class Object:
    def __init__(self, size, object_type, object_id=None, n_objects=None):
        self.size = size
        if object_type == "player":
            self.x = int(self.size/2)
            self.y = 0
        elif object_type == "food":
            self.x = int(self.size/2)
            self.y = int(self.size-1)
        elif object_type == "enemy":
            lower = int(self.size/3)
            upper = size-lower
            if n_objects==1:
                self.y = int(size/2)
            else:
                self.y = int(lower + object_id*(upper-lower)/(n_objects-1))
            print("object_id", object_id)
            if object_id % 2==0:
                self.x = 0
                self.enemy_direction = 1
            else:
                self.x = size-1
                self.enemy_direction = -1
            # self.y = int(self.size/2)
            # self.enemy_direction = 1
        else:
            print("Object type not recogized")
            exit()
        # self.x = np.random.randint(0, size)
        # self.y = np.random.randint(0, size)

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
            self.move(x=1, y=0, isEnemy=True)
        elif self.enemy_direction == -1:
            self.move(x=-1, y=0, isEnemy=True)



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
            elif self.x > self.size - 1:
                self.x = self.size - 2
                self.enemy_direction *= -1

        else:
            self.x += x
            self.y += y
            # If we are out of bounds, fix!
            if self.x < 0:
                self.x = 0
            elif self.x > self.size-1:
                self.x = self.size-1

            if self.y < 0:
                self.y = 0
            elif self.y > self.size-1:
                self.y = self.size-1

