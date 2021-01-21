##########################################################
# >> Version : pass_proc_1.0.1 
# >> Created by : Tharun
# >> Description : Open source password manager
# >> Docs : 
# >> Support : bc1qcxpjnznn7zmq3xyxnafqjn39j46e5j33seu3dz
##########################################################
# importing
import os
from sys import exit
from func import *

try:
    import hashlib 
    import pyfiglet
except:
    install()
try:
    # finally calling the my_main func
    my_main('','')
except KeyboardInterrupt:
    print('\nEXITTING....\n')
except:
    print("\n!!! AN ERROR ACURED !!!")

