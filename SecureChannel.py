#!/bin/python3
  
import math
import os
import random
import re
import sys
 
# Complete the secureChannel function below.
def secureChannel(operation, message, key):
    if len(message)==0 or len(key)==0:
        return "-1"
  
    strRet=""
  
    if operation==1:
        index=0
        for keyVal in key:
            nKeyVal=int(keyVal)
            if index>=len(message):
                return strRet
            strRet=strRet+message[index]*nKeyVal
            index=index+1
        if index < len(message):
            strRet=strRet+message[index:]
  
    elif operation==2:
        index=0
        for keyVal in key:
            nKeyVal=int(keyVal)
            if index>=len(message):
                return strRet
            for i in range(0,nKeyVal):
                if (index+i)>=len(message):
                    return "-1"
                if message[index] != message[index+i]:
                    return "-1"
            strRet=strRet+message[index]
            index=index+nKeyVal
        if index < len(message):
            strRet=strRet+message[index:]
  
    else:
        return "-1"
 
    return strRet
  
if _name_ == '_main_':
    print(secureChannel(1, 'Open',  '123'))
    print(secureChannel(2, 'Oppeeen',  '123'))
