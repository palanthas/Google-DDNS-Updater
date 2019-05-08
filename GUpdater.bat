SET USERNAME=Generated-Username-Here
SET PASSWORD=Generated-Password-Here
SET HOSTNAME=Domain.com

FOR /F %%I in ('curl ifconfig.co') do set IP=%%I

curl "https://%USERNAME%:%PASSWORD%@domains.google.com/nic/update?hostname=%HOSTNAME%&myip=%IP%"
