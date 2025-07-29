# f =open("FILE.txt")
# data = f.read()
# print(data)
# f.close()

# # string = "hay hari how are you"
# # f = open("FILE.txt","w")
# # f.write(string)
# # f.close()

# f = open("FILE.txt")

# lines = f.readlines()
# print(lines,type(lines))

# # line1 = f.readline()
# # print(line1,type(line1))

# # line2 = f.readline()
# # print(line2,type(line2))

# # line3 = f.readline()
# # print(line3,type(line3))

# f.close()

# the same can be written as this:  nd don't need to b close :

# with open("FILE.txt") as f:
#     print(f.read())

# import random
# def game ():
#     print("Youare playing a game")
#     score = random.randint(1, 100)
#     with open("FILE.txt") as f:
#         highscore = f.read()
#         if highscore != "":
#             highscore = int(highscore)
#         else:
#             highscore = 0
#     print(f"Your score is {score}")
#     if (score > highscore):
#         with open("FILE.txt", "w") as f:
#             f.write(str(score))
#     return score

# game()




