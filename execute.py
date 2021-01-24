##########################################################
# >> Version : pass_proc_1.0.1 
# >> Created by : Tharun
# >> Description : Open source password manager
# >> Docs : https://github.com/Tharunkumarmuthu/Pass_proc
# >> Support : bc1qcxpjnznn7zmq3xyxnafqjn39j46e5j33seu3dz
##########################################################

# IMPORTING
import os
from sys import exit
from func import *

# CHECKING MODULES
try:
    import hashlib 
    import pyfiglet
except:
    install()

try:
    # CALLING MAIN FUNCTION
    my_main('','')
except KeyboardInterrupt:
    print('\nEXITTING....\n')
except:
    print("\n!!! AN ERROR ACURED !!!")

