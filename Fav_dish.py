love_food = input("What is your favourite dish? please pick one: spaghetti,tuna maki,butter chicken.   ")
print("I love {} too!".format(love_food))
if love_food == "spaghetti":
    print("If you love",love_food,"You should totally try Cubanelle and Veal Bolognese!")
elif love_food == "tuna maki":
    print("Yum! Where I can find the best restaurant for {} in Toronto?".format(love_food))
else:
    print("Lol I lied, I've never tried {} before, but I'd love to give it a shot!".format(love_food))
print("Glad to know your faviourite dish is {}!".format(love_food))