# First I create two virtual environment using pip install virtualenv. If you havce already install then i created two virtual environment using virtualenv. Now i have two virtualenv myprojectenv1 and myprojectenv2. So i install some function in first encironment like pygame,flask,Djamngo etc. Now i use pip freeze > function and put these file in requirement.txt. Now u opeen second viryual environment and install these function via pip freeze -r requirement.txt. Thats all.

# print("The name of student is {}, his marks are {} and phone number is {}".format("Vinit","100","1234567890"))

# l=[7,14,21,28,35,42,49,56,63,70]
# print("\n".join(map(str,l)))

# l=[1,3,5,6,87,55,46,568,89,90,8,0,45,335,500,8090,4645,2345,354,3437,44685]
# divisibleby5=lambda n:n%5==0
# print(list(filter(divisibleby5,l)))

# from functools import reduce
# l=[1,3,5,6,87,55,46,568,89,90,8,0,45,335,500,8090,4645,2345,354,3437,44685]
# print(reduce(max,l))

#--> This is result of pip freeze:
# click==8.1.3
# colorama==0.4.5
# Flask==2.2.2
# itsdangerous==2.1.2
# Jinja2==3.1.2
# MarkupSafe==2.1.1
# playsound==1.3.0
# Werkzeug==2.2.2