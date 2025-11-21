import random

def get():
   point_bot = 0
   point_user = 0
   lis = ["sang" , "kaqaz" , "qeichi"]
   while True:
       user = input("sang & kaqaz & qeichi : ")
       if user not in lis:
           print("please enter correct word")
           continue

       bot = random.choice(lis)
       print("Computer => ",bot)


       if user == bot:
           print("mosavi")
       elif user == "sang":
           if bot == "kaqaz":
               print("Computer win")
               point_bot += 1
               print(f"point's Computer: {point_bot} VS point's You: {point_user}")
               print("\n")
               
           else:
               print("You win")
               point_user += 1
               print(f"point's Computer: {point_bot} VS point's You: {point_user}")
               print("\n")
               
       elif user == "kaqaz":
           if bot == "qeichi":
               print("Computer win!")
               point_bot += 1
               print(f"point's Computer: {point_bot} VS point's You: {point_user}")
               print("\n")
               
           else:
               print("You win!")
               point_user += 1
               print(f"point's Computer: {point_bot} VS point's You: {point_user}") 
               print("\n")
                
       elif user == "qeichi":
           if bot == "sang":
               print("Computer win!")
               point_bot += 1
               print(f"point's Computer: {point_bot} VS point's You: {point_user}")
               print("\n")
               
           else:
               print("You win!")
               point_user += 1
               print(f"point's Computer: {point_bot} VS point's You: {point_user}")
               print("\n")
               
get()               
               








    

  






    

    






