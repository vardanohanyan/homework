#Problem 8

#Bob wants to go to university.


#Bob can be accepted if his math exam score is 10 or more and his english exam score is 10 or more.
#Bob can also be accepted if his math score is 15 or more and his english score is 5 or more
#                            or his math score is 5 or more and his english score is 15 or more.
#Bob can also be accepted if one of the scores is 20.
#Bob cannot be accepted if both scores are 0.

#(Exam scores are from 0-20)

math = int(input("input your math exam score"))
eng = int(input("input your english exam score"))

if math >= 10 and eng >= 10:
    print("you accepted")
elif math >= 15 and eng >= 5:
    print("you accepted")
elif math >= 5 and eng >= 15:
    print("you accepted")
elif math == 20 and eng ==0 or math == 0 and eng == 20:
    print("you accepted")
else:
    print("you failed exam")