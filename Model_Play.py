from Agent import *

environment = Environment()
agent = DQNAgent()
agent.model = tf.keras.models.load_model("./Pretrained models\Best model SIZE=30/60Kepisodes_Game_size_30__8700____-3.00max__-74.08avg_-355.00min__1608435267.model")



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