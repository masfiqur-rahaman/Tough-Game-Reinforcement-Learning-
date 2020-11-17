from Agent import *
import pygame
import keyboard

pygame.init()
environment = Environment()
# environment.init_render()
agent = DQNAgent()
# agent.model = tf.keras.models.load_model("./models best/40Kepisodes_BEST_2x256____25.00max__-37.16avg_-407.00min__1604741142.model")

def pressed_to_action():
    # action = None
    # if key[273] == 1:  # forward
    #     action = 6
    # if key[274] == 1:  # backward
    #     action = 7
    # if key[275] == 1:  # left
    #     action = 5
    # if key[276] == 1:  # right
    #     action = 4
    # else:
    #     action = 8

    action = None
    if keyboard.is_pressed('w'):  # forward
        action = 5
    elif keyboard.is_pressed('s'):  # backward
        action = 4
    elif keyboard.is_pressed('a'):  # left
        action = 7
    elif keyboard.is_pressed('d'):  # right
        action = 6
    else:
        action = 8

    return action

def play():
    episode = 0
    # set game speed to 30 fps
    # environment.clock.tick(30)
    while True:

        print(episode)
        episode += 1
        # Reset environment and get initial state
        current_state = environment.reset()
        cv2.waitKey(600)
        done = False
        while not done:
            cv2.waitKey(100)
            # get pressed keys, generate action
            # get_pressed = pygame.key.get_pressed()

            action = pressed_to_action()
            # calculate one step
            environment.step(action)
            # render current state
            environment.render()

play()