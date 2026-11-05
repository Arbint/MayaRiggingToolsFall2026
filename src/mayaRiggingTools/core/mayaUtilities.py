import maya.cmds as mc

def GetParent(objectToGetParent):
    parent = mc.listRelatives(objectToGetParent, p=True)
    if not parent or len(parent) == 0:
        return None

    return parent[0]