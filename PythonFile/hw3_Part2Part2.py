pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
print("Welcome to the House of Pies! Here are our pies: ")
for index , value in enumerate(pie_list):
  # print(index, value)
  print(f"({str(index+1)})  {pie_list[index]}")
my_selection = [0,0,0,0,0,0,0,0,0,0]
answer = 'y'
while answer == 'y' or answer == 'Y' : 
  user_selection = input("What pie would you like to order? Enter a number ")
  print(f"Great! We'll have {pie_list[int(user_selection)-1]} right out for you! ")
  my_selection[int(user_selection)-1]+=1
  answer = input(" Do you want to make another order? y(es) or n(o) ")
print("--------------------------------------------")
print(f"Hey! This is your pie selection:")
for index in range(len(pie_list)):
  count = my_selection[index]
  pie = pie_list[index]
  print(f"{count} {pie} ")