from subprocess import *

data = check_output('netsh wlan show profiles') # יוצר אובייקט שבתוכו רשימת רשתות
data = data.decode('utf-8') # מפענח את האובייקט מבייטים למחרוזת
data = data.split('\n')

networks = []

for i in data:
    if "All User Profile" in i:
    x = i.split(":")[1][1:-1]
    networks.append(x)

for i in networks:
    print(i + '\n')
    password = check_output(f"netsh wlan show profile {i} key=clear")
    password = password.decode('utf-8')
    password = password.split('\n')

print(password[32])