print('Begin!')
from random import randint

def Positioneer(Size1, Pos1, Pos2):
    spx = Size1[0]+Pos1[0]
    spy = Size1[1]+Pos1[1]

    if Pos2[0] < spx and Pos2[0] > Pos1[0] and Pos2[1]<spy and Pos2[1]>Pos1[1]:
        return True
    else:
        return False
def Touch(SSize, SPos, Siz, Pos):
    Points = [(Pos[0] + Siz[0], Pos[1]),
    (Pos[0], Pos[1] + Siz[1]),
    (Pos[0] + Siz[0], Pos[1] + Siz[1]), Pos]
    for i in range(4):
        IsTouch = Positioneer(SSize, SPos, Points[i-1])
        if IsTouch:
            return True
    return False
print(Touch((20, 20), (50, 50), (20, 20), (54, 49)))
# randpos = (19, 19)
# Touch((30, 30), (20, 20))