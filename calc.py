num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# হিসাবগুলো আলাদা আলাদা লাইনে (খুবই গুরুত্বপূর্ণ)
sum_res = int(num1) + int(num2)
sub_res = int(num1) - int(num2)
mul_res = int(num1) * int(num2)
div_res = int(num1) / int(num2)

# এবার ফলাফলগুলো দেখাবে
print("The total is: " + str(sum_res))
print("The subtraction is: " + str(sub_res))
print("The multiplication is: " + str(mul_res))
print("The division is: " + str(div_res))