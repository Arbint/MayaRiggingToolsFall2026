import maya.cmds as mc
import maya.mel as mel

def GetParent(objectToGetParent):
    parent = mc.listRelatives(objectToGetParent, p=True)
    if not parent or len(parent) == 0:
        return None

    return parent[0]

def CreateFKCircleControllerForJnt(jnt, size=10):
    ctrlName = "ac_fk_" + jnt
    mc.circle(n=ctrlName, r=size, nr=(1,0,0))
    
    ctrlGrp = ctrlName + "_grp"
    mc.group(n=ctrlGrp)
    mc.matchTransform(ctrlGrp, jnt)
    mc.orientConstraint(ctrlName, jnt)

    return ctrlName, ctrlGrp

def CreateIkBoxControllerForJnt(jnt, size=10):
    boxName = "ac_ik_" + jnt
    boxName = CreateBox(boxName, size)
    boxGrpName = boxName + "_grp"
    mc.group(boxName, n=boxGrpName)
    mc.matchTransform(boxGrpName, jnt)

    return boxName, boxGrpName


def CreateBox(name, size):
    mel.eval(f"curve -n {name} -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;")

    mc.setAttr(f"{name}.scale", size, size, size, type="double3")

    # this is freezed transformation
    mc.makeIdentity(name, apply=True)
    return name


def CreatePlus(name, size):
    mel.eval(f"curve -n {name} -d 1 -p -1 1 0 -p -1 3 0 -p 1 3 0 -p 1 1 0 -p 3 1 0 -p 3 -1 0 -p 1 -1 0 -p 1 -3 0 -p -1 -3 0 -p -1 -1 0 -p -3 -1 0 -p -3 1 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12;")

    mc.setAttr(f"{name}.scale", size, size, size, type="double3")

    # this is freezed transformation
    mc.makeIdentity(name, apply=True)
    return name


