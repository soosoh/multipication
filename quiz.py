def quiz(reply):
    from main import coins
    from main import score
    from main import ans
    from main import quizname
    if ans == reply:
        print("right!")
        print("you received " + str(score) + " coins")
        from main import score
        coins = coins + score
        if reply != ans and reply != "coins":
            print("Wrong")
            if coins >= 50:
                print("you have " + str(coins) + "coins" +
                      ".Do you wish to use 50 coins to retry? (yes/no)")
                retry_ = input(":")
                if retry_ == "yes":
                    print(quizname)
                    reply = input("answer: ")
                    quiz(ans, reply)
                    from main import coins
                    coins = coins - 50
                else:
                    print("too bad")
            else:
                print("too bad")
    if reply == "coins":
        from main import coins
        print(str(coins))
        print(quizname)
        reply = input("answer: ")
        quiz(reply)
