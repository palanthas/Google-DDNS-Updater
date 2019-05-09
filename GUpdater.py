from requests import get

USERNAME = "Generated-Username-Here"
PASSWORD = "Generated-Password-Here"
HOSTNAME = "Domain.com"
IP = get('http://ifconfig.co/ip').text

update = get("https://{}:{}@domains.google.com/nic/update?hostname={}&myip={}".format(USERNAME, PASSWORD, HOSTNAME, IP)).text

print update

