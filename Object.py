import numpy as np
# from Game_Environment import Environment

from shapely.geometry import Point, Polygon


class Object:
    def __init__(self, height, width, object_type, vertices, object_id=None, n_objects=None, ENEMY_SPEED=1):
        self.height = height
        self.width = width
        self.vertices = vertices

        if object_type == "player":
            # When game starts player stays at "Home". When player wins a match, player stays as "Goal"
            self.player_position = "Home"
            self.x = 14
            self.y = 5
        elif object_type == "food":
            self.x = 44
            self.y = 2
        elif object_type == "enemy":
            self.ENEMY_SPEED = ENEMY_SPEED
            lower = 4
            upper = 15
            horiz_lower = 13
            horiz_upper = 42
            if n_objects==1:
                self.y = int(self.height/2)
            else:
                self.y = lower + 1 + object_id*3
                # self.y = int(lower + object_id*(upper-lower)/(n_objects-1))
            # print("object_id", object_id)
            if object_id % 2==0:
                # training
                # self.x = np.random.randint(horiz_lower, horiz_upper)
                self.x = horiz_lower + 1 + np.random.randint(1, 10)*3
                # Play
                # self.x = horiz_lower + 1
                self.enemy_direction = -1
            else:
                # training
                # self.x = np.random.randint(horiz_lower, horiz_upper)
                self.x = horiz_lower + 1 + np.random.randint(1, 10)*3
                # Play
                # self.x = horiz_upper-1
                self.enemy_direction = 1
        else:
            print("Object type not recogized")
            exit()
        # self.x = np.random.randint(0, self.height)
        # self.y = np.random.randint(0, self.width)

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
        # if choice == 0:
        #     self.move(x=1, y=1)
        # elif choice == 1:
        #     self.move(x=-1, y=-1)
        # elif choice == 2:
        #     self.move(x=-1, y=1)
        # elif choice == 3:
        #     self.move(x=1, y=-1)

        # elif choice == 6: # right
        #     self.move(x=1, y=0)
        # elif choice == 7: # left
        #     self.move(x=-1, y=0)
        # elif choice == 4: # forward
        #     self.move(x=0, y=1)
        # elif choice == 5: # backward
        #     self.move(x=0, y=-1)

        if choice == 6: # right
            self.move(x=3, y=0)
        elif choice == 7: # left
            self.move(x=-3, y=0)
        elif choice == 4: # forward
            self.move(x=0, y=3)
        elif choice == 5: # backward
            self.move(x=0, y=-3)

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

            poly = Polygon(self.vertices)
            if not poly.contains(Point(self.x, self.y)):
                # print("Enemy outside polygon ------------------------->")
                # print(self.vertices)
                # print((self.x, self.y))
                self.x -= x
                self.y -= y
                self.enemy_direction *= -1
                # print(self.x, self.y)

            # # If we are out of bounds, fix!
            # if self.y < self.border_thickness:
            #     self.y = self.border_thickness + 1
            #     self.enemy_direction *= -1
            # elif self.y > self.width - self.border_thickness - 1:
            #     self.y = self.width - self.border_thickness - 2
            #     self.enemy_direction *= -1

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



            poly = Polygon(self.vertices)
            if not  poly.contains(Point(self.x, self.y)) :
                self.x -= x
                self.y -= y
                # print("player outside polygon ------------------------->")
                # print(self.x, self.y)
            """
            # If we are out of bounds, fix!

            # if No movement or player position is elsewhere
            # (self.player_position!="Home" and self.player_position!="Goal")
            if (x==0 and y ==0) or self.player_position=="Other":
                if (self.x > self.height - self.border_thickness - 1) and self.y==self.border_thickness:
                    self.player_position = "Home"
                    print("Inside player home region")
                elif (self.x < self.border_thickness) and (self.y==self.height - self.border_thickness - 1):
                    self.player_position = "Goal"
                    print("Inside food/Goal region")
                else:
                    self.player_position = "Other"
                    print("Inside Other region")
            elif (x!=0 or y!=0):
                self.player_position = "Other"
                print("Inside Other region")
                if self.x < self.border_thickness:
                    self.x = self.border_thickness
                elif self.x > self.height - self.border_thickness - 1:
                    self.x = self.height - self.border_thickness - 1

                if self.y < self.border_thickness:
                    self.y = self.border_thickness
                elif self.y > self.width - self.border_thickness - 1:
                    self.y = self.width - self.border_thickness - 1
            else:
                print("ELSE")
                exit()
            """


