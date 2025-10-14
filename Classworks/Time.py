import time     #час, різниця в часі, пауза системи
from datetime import datetime
adate = datetime.today()
time.sleep(3)
bdate = datetime.today()
print(adate)
print(bdate)
print(bdate-adate)
print(type(bdate-adate))


#версія системи
import sys      
sys.version

print('version')