from Game import Game


def main(delay, mode=0):
    myGame = Game()
    myGame.initialize_game(delay, mode)
    myGame.run_game(delay)


if __name__ == '__main__':
    main(10, 1)
