from random import randrange

def getsmiley():
    eye=[':','8','B',';','x','=']
    mouth=[')','D','>','C','Z','/','E','S','P','O','o','|','3','\\','X','s',']','[']

    nose=['-','^','{','0','\'']
    hat=['<','d','<*','c','>']
    chin=['~','~~','~~~','<-<','-G<']

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

    return smiley
