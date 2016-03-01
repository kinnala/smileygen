from random import randrange

eye=[':','8','B']
mouth=[')','D','>','C','/','E','S','P','O','o','|','3']

nose=['-','^','{','o']
hat=['<','d','<*','c','>']
chin=['~','~~~','<-<']

smiley=''

if randrange(100)<=30:
    ihat=randrange(len(hat))
    smiley+=hat[ihat]

ieye=randrange(len(eye))
smiley+=eye[ieye]

if randrange(100)<=40:
    inose=randrange(len(nose))
    smiley+=nose[inose]

imouth=randrange(len(mouth))
smiley+=mouth[imouth]

if randrange(100)<=30:
    ichin=randrange(len(chin))
    smiley+=chin[ichin]

print smiley
