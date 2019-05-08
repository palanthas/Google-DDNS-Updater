# Google-DDNS-Updater
Batch Script for updating Google's Dynamic DNS Synthetic Records

I created this for a friend who needed to be able to update his Google Dynamic DNS records from his Windows desktop. I opted for a batch file because I didn't have a whole lot of time to write anything else that I could guarantee would work on his computer.

How to use
1. Copy the GUpdater.bat file to your computer
2. Fill in the Username/Password fields with the generated credentials from your synthetic record
3. Fill in the Hostname field with your domain name or sub-domain from your synthetic record
4. Run the script to update your DNS

That's pretty much it. Granted, you'll want to consider creating a scheduled task to run the script on a regular basis.

I'm using ifconfig.co to get the public IP. Per their page we can use their service so long as we don't exceed 1 request per minute. 

Considering that your public IP shouldn't change very frequently I opted to set my friend's schedule to run only once per hour. The only downside to this is if you force your IP to change (like replacing your router) then you may have to manualy run the updater once to instantly change your DNS records.
