food_list = [
    ["Pizza", "Spam", "Burger", "Pasta"],
    ["Apple", "Banana", "Orange"],
    ["Chicken", "Spam", "Fish", "Beef"],
    ["Salad", "Soup", "Sandwich"],
    ["Ice Cream","Spam",  "Cake", "Cookies", "Spam","Spam"]
]


for meal in food_list:
    if "Spam" in meal:

        for index in range(len(meal) -1, -1, -1):
            if meal[index] == "Spam":
                # print(index, meal)
                del meal[index]
     

        # for index, item in enumerate(meal):
        #    print( index,item)
        #    if item =="Spam":
        #         del meal[index]
        #         print(meal)
       

        print(",".join(meal))    
               
    # else:
    #     print("{} has a spam score of {}".format(meal,meal.count("Spam")))