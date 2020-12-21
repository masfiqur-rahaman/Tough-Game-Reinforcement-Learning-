from Agent import *

environment = Environment()
agent = DQNAgent()
agent.model = tf.keras.models.load_model("./Pretrained models\Best model SIZE=56X20/Game_size_56X46__1__-200.00max_-200.00avg_-200.00min__1608497085.model")



def play(ENEMY_SPEED):
    episode = 0
    score = 0
    while True:
        print(episode)
        episode += 1
        # Reset environment and get initial state
        current_state = environment.reset(ENEMY_SPEED)

        cv2.waitKey(1000)
        done = False
        while not done:
            cv2.waitKey(100)
            action = np.argmax(agent.get_qs(current_state))
            print("action", action)
            new_state, reward, done = environment.step(action)
            if done and reward==environment.FOOD_REWARD:
                score += 1
            environment.render(episode, score)

            current_state = new_state

play(ENEMY_SPEED=2)