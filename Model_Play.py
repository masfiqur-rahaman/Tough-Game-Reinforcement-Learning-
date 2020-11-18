from Agent import *

environment = Environment()
agent = DQNAgent()
agent.model = tf.keras.models.load_model("./Pretrained models/60Kepisodes_BEST_Game_2x256__19800____16.00max_-196.54avg_-353.00min__1605717567.model")



def play():
    episode = 0
    score = 0
    while True:
        print(episode)
        episode += 1
        # Reset environment and get initial state
        current_state = environment.reset()

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

play()