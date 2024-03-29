import time
from datetime import datetime 

a = time.time() #get seconds since 1970 January 1
z = datetime.now() 

#OUTPUT
#Notes: %b =abbreviated of month name such as September > Sep
#strftime = string format time 

print(f"Seconds since January 1, 1970: {a:,.4f} or {a:.2e} in scientific notation")
print(f"{z.strftime('%b %d %Y')}")