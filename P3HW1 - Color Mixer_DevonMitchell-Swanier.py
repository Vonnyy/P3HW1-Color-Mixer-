# CTI -110
# P3HW1 - Color Mixer
# Devon Mitchell-Swanier
# 4/8/2020
#  When you mix primary colors you will get a secondary color. (Primary = Red, blue, yellow)

#Type in the two primary colors
primaryColor1 = input('Enter primary color 1: ')
primaryColor2 = input ('Enter primary color 2: ')

if primaryColor1 == "red" and primaryColor2 == "blue" or primaryColor1 == "blue" and primaryColor2 == "red":
 print('The color is purple ')
else:
    if primaryColor1 == "red" and primaryColor2 == "yellow" or primaryColor1 == "yellow" and primaryColor2 == "red": 
     print('The color is orange ')
    else:
        if primaryColor1 == "yellow" and primaryColor2 == "blue" or primaryColor1 == "blue" and primaryColor2 == "yellow":
         print('The color is green ') 
