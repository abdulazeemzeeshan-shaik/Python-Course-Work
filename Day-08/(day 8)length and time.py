"""A system checks password length. If length is 8 or more, password accepted. 
Otherwise, rejected. Display result."""
password="zeeshannn"

if len(password)>=8:
    print("ACCEPTED")
else:
    print("password length is less")
    print("REJECTED")


"""3. A system checks password length. If length is 8 or more, password accepted. 
Otherwise, rejected. Display result. """

hours=int(input("enter"))
minutes=int(input("enter"))
if hours==12:
    print("12pm")
elif hours>= 12:
    time=hours-12
    print(f"{time}:{minutes}pm")
else:
    print(f"{hours}:{minutes}am")