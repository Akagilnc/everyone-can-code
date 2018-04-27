def he(height):
    hei = height * height
    return hei

information = "please input your height(cm):"
height = int(input(information))
square = he(height)
question = "Please input your weight(kg): "
weight = int(input(question))
bmi = int(weight / square)
print("your BMI is {}".format(bmi))





