import time
import datetime

# , => add a comma to the number
# .2 => round to 2 decimal places
# e => scientific notation
seconds_since_epoch = time.time()
print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation")

# %b => month name (3 letters), %d => day of the month, %Y => year
curent_date = datetime.datetime.now()
print(f"{curent_date.strftime('%b %d %Y')}")
