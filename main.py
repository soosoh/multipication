coins = 0
retry_ = 0
score = 0

import quiz

print("2x2")
quizname = "2x2"
reply = input("answer: ")
ans = "4"
score = 10
quiz.quiz(reply)

print("4x5?")
quizname = "4x5?"
reply = input("answer: ")
ans = "20"
score = 20
quiz.quiz(reply)

print("12x12")
quizname = "12x12"
reply = input("answer: ")
ans = "144"
score = 40
quiz.quiz(reply)
