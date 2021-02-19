# pip install pywhatkit

import pywhatkit
import datetime

friend = input("Whom to Send |> ")

message = input("What is the message |> ")


hour = datetime.datetime.now().strftime('%H')
minute = datetime.datetime.now().strftime('%M')

print(f"Sending message to {friend}")

# This is you contact dictionary. Add as many contacts  as you want
mobile = {'contact_name1': '+91XXYYXXYYXX',
          'contact_name2': '+91XYXYXYXYXY'}

if mobile[friend] is None:
    print('Sorry No Contact Found')

try:
    pywhatkit.sendwhatmsg(mobile[friend], message,
                          int(hour), int(minute) + 1, 10, True)

except:
    pass
