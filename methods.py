import math
# distance function ergh, doesn't quite work. so close
def distance1(maxx, minx, maxy, miny):
    # my math is horrid and it doesn't work
    # To find the CONSTANT_distancetocm variable, I basically had to manually measure
    # distance of objects from the camera, then divided the distance from the camera with a number gained
    # from the equation (m/(1-(a/b))) m - distance between when a and b were measured, a -
    SizeX = (maxx - minx)
    SizeY = (maxy - miny)
    pixeltomm = 145.6 / SizeY
    ObjectCenterX = (minx - maxx) / 2
    CONSTANT_distancetocm = 698
    OffCenterX = int(maxx - (SizeX / 2)) - int(imageWidth / 2)
    OffCenterY = int(maxy - (SizeY / 2)) - int(imageHeight / 2)
    DistanceC = math.sqrt(pow(OffCenterX, 2) + pow(OffCenterY, 2))
    DistanceA = ((TARGETYSIZEMM * FOCALLENGTH) / SizeY)
    DistanceB = math.sqrt(pow(DistanceA, 2) + pow(DistanceC, 2))
    Distance = ((TARGETYSIZEMM * FOCALLENGTH) / SizeY)
    return LateralDistance, Distance, OffCenterX, OffCenterY

# not being used, maybe make another equation later on
def distance2(maxx, minx, maxy, miny):
    SizeX = (maxx - minx)
    SizeY = (maxy - miny)
    OffCenterX = int(maxx - (SizeX / 2)) - int(imageWidth / 2)
    OffCenterY = int(maxy - (SizeY / 2)) - int(imageHeight / 2)
    magnification = TARGETYSIZEMM / (maxy - miny)
    Distance = FOCALLENGTH / magnification
    DistanceMM = Distance / 25.4
    return LateralDistance, Distance, OffCenterX, OffCenterY

# this is the only one that works, has golden number(my number)

def distance3(maxx, minx, maxy, miny):
    THEODORS_NUMBER = 0.0516657316
    SizeX = (maxx - minx)
    SizeY = (maxy - miny)
    OffCenterX = int(maxx - (SizeX / 2)) - int(imageWidth / 2)
    OffCenterY = int(maxy - (SizeY / 2)) - int(imageHeight / 2)

    LateralDistance = (TARGETYSIZE * FOCALLENGTH) / SizeY
    LateralDistance = LateralDistance/THEODORS_NUMBER

    Apx = SizeY
    Amm = 72.8
    MM__PX = Apx/Amm
    Bpx = math.sqrt(pow(OffCenterX, 2) + pow(OffCenterY, 2))
    Bmm = Bpx*MM__PX
    Cpx = math.sqrt(pow(Bpx, 2) + pow(Apx, 2))
    Cmm = Cpx*MM__PX
    
    Distance = math.sqrt(pow(Cmm, 2) + pow(LateralDistance, 2))
    
    return LateralDistance, Distance, OffCenterX, OffCenterY

