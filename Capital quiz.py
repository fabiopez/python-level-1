#1 output "What is the capital of England?"
#2 store the answer
#3 check if they have the correct answer
#4 if they do, print "Well done"
#5 if they don't, print("Try again")
answer = input("What is the capital of England?")
while (answer != "london"):
  print("Try again")
  answer = input("What is the capital of England?")
print("Well done!")