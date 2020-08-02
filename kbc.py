
question_list = ["how many contries are there",
                "what is the capital of india?",
                "ng mei kon se course padhate hai"]

options_list = [["four","nine","seven","eight"],
                ["chandighad","bhopal","chennai","delhi"],
                ["software engineering","counsling","toursim","agruculture"]]

solution_list = [3,4,1]
new_list = [["four","seven"],["bhopal","delhi"],["software engineering","counsling"]]
new_solution = [2,2,1]
i = 0
count = 1

while i < len(question_list):
    print("aapka sawal hai:")
    print ("Q"+str(i+1)+(" ")+question_list[i])
    b=0
    c=0
    print("aapka options ye hai")

    while b < len(options_list[i]):
        print (b+1,options_list[i][b])
        b=b+1
    user = int(input("enter your answer "))
    if user==(solution_list[i]):
        print("congreats")
    elif user==int("5050"):
        if count == 1:
            c=0
            while c < len(new_list[i]):
                print (c+1,new_list[i][c])
                c=c+1
            user2 = int(input("choose you ans "))
            if user2==(new_solution[i]):
                print("right answer hai")
            else:
                print("wrong answer hai")
                break
            count= count+1
        else:
            print("aap already lifeline use kr chuke hai")
            break
    else:
        print("sadly aapka javab galat hai")
        break
    i=i+1
    print("")


