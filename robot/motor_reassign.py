from DXLConfig import DXLConfig
from motor import Motor
import time
from leg import Leg
conf = DXLConfig("COM9")
conf.open()
# print(conf.findIDs())

# current = conf.findFirstID()
# new = 18

# m = Motor(current)
# answer = input(f"Reassigning motor {current} to {new}. Continue?")
# if answer == "y":
#     print("reassiging.")
#     m.reset(new)
conf.close()


