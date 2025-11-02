#Codechum
#Emails Details Display

recipient = input("Enter the recipient: ")
message = input("Enter the message: ")
name = input("Enter the name: ")
subject = input("Enter the subject: ")
version = float(input("Enter the version: "))
discount = float(input("Enter the discount: "))
status = input("Enter the status: ")
code = input("Enter the code: ")
location = input("Enter the location: ")
age = int(input("Enter the age: "))
company_name = input("Enter the company name: ")
website = input("Enter the website: ")
phone = input("Enter the phone: ")
job_title = input("Enter the job title: ")
department = input("Enter the department: ")


print(f"Dear {recipient}, I hope this email finds you well.")
print(message)
print("Subject:",subject)
print("Sender:" ,name)
print("Version:",version)
print(f"Discount: {discount:.2f}%")
print("Status:",status)
print("Code:",code)
print("Location:",location)
print("Age:",age)
print("Company:",company_name)
print("Website:",website)
print("Phone:",phone)
print("Job Title:",job_title)
print("Department:",department)


#Name input

name = input("Enter your name: ")

print("Welcome, " + name + "!")


#Personal Information

name = str(input("Enter your name: "))
age = str(input("Enter your age: "))
city = str(input("Enter your city: "))

print("Name: " + name)
print("Age: " + age)
print("City: " + city)

#Book Reservation 

book = input("Enter the book title: ")
author = str(input("Enter the author: "))
year = int(input("Enter the year of publication: "))
genre = str(input("Enter the genre: "))
library = str(input("Enter the library: "))
member = int(input("Enter your member ID: "))
date = str(input("Enter the return date: "))

print("You have successfully reserved the book", "'" + book + "'", "by", author + ".")
print("Year of Publication:",year)
print("Genre:",genre)
print("Library:",library)
print("Member ID:",member)
print("Return Date:",date)


#Social Media Post Scheduler

date = input("Enter Post Date: ")
time = input("Enter Post Time: ")
reach = float(input("Enter Post Reach: "))
engagement = float(input("Enter Post Engagement: "))
duration = float(input("Enter Post Duration: "))
category = input("Enter Post Category: ")

print("\nPost Scheduled:")
print(f"Date: {date}")
print(f"Time: {time}")
print(f"Reach: {reach:.2f}")
print(f"Engagement: {engagement:.2f}")
print(f"Duration: {duration:.2f}")
print(f"Category: {category}")