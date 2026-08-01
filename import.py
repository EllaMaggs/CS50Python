# import random
# coin = random.choice (["Heads","Tails"])
# print(coin)

# import sys
# if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
## 0 ommited as it is the name of the script
# for arg in (sys.argv) [1:]:
#    print ("Hello, my name is", arg)

import cowsay
import sys
if len(sys.argv) == 2:
    print(cowsay.cow("Hello, my name is " + sys.argv[1]))
