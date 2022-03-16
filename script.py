import bpy
import sys
sys.path.append('/home/chuismi/Desktop/robotica/tercero/segundocuat/modelado/proyecto-modelado3d-chuismiguel')
from transformaciones import *

PI = 3.1416

def createWheel(x, y, z, name):
    Objeto.crearCilindro('centro_rueda')
    Seleccionado.rotarX(PI/2)
    Seleccionado.escalar((1, 0.2, 1))
    Especifico.posicionar('centro_rueda', (x, y, z))
    
    Objeto.crearCilindro('exterior_rueda_izq')
    Especifico.rotar('exterior_rueda_izq', (PI/2, 0, 0))
    Especifico.escalar('exterior_rueda_izq', (1, 1, 0.1))
    Especifico.posicionar('exterior_rueda_izq', (x, y - 0.3, z))
    Especifico.escalar('exterior_rueda_izq', (1.1, 1.1, 0.1))
    
    Objeto.crearCilindro('exterior_rueda_der')
    Especifico.rotar('exterior_rueda_der', (PI/2, 0, 0))
    Especifico.escalar('exterior_rueda_der', (1, 1, 0.1))
    Especifico.posicionar('exterior_rueda_der', (x, y + 0.3, z))
    Especifico.escalar('exterior_rueda_der', (1.1, 1.1, 0.1))
    
    juntarObjetos(['centro_rueda', 'exterior_rueda_izq', 'exterior_rueda_der'])
    
    for obj in bpy.context.selected_objects:
        obj.name = name

def createUltrasound(x, y, z):
    Objeto.crearCubo("base us")
    Especifico.posicionar("base us", (x, y, z))
    Especifico.escalar("base us", (1.2, 2.4, 1))
    
    Objeto.crearCilindro("us izq")
    Especifico.posicionar("us izq", (x - 0.3, y - 0.3, z))
    Especifico.rotar("us izq", (0, -PI/2, 0))
    Especifico.escalar("us izq", (0.15, 0.15, 0.1))
    
    Objeto.crearCilindro("us der")
    Especifico.posicionar("us der", (x - 0.3, y + 0.3, z))
    Especifico.rotar("us der", (0, -PI/2, 0))
    Especifico.escalar("us der", (0.15, 0.15, 0.1))
    
    juntarObjetos(["us der", "us izq"])
    for obj in bpy.context.selected_objects:
        obj.name = "us_cylinders"
    
    
def createChassis():
    createWheel(4, -2, 2, "LeftRearTyre")
    createWheel(4, 2, 2, "RightRearTyre")
    
    createWheel(0, -2, 2, "LeftFrontTyre")
    createWheel(0, 2, 2, "RightFrontTyre")
    
    seleccionarMultiples(["RightFrontTyre", "LeftFrontTyre"])
    Seleccionado.escalar([0.8, 1, 0.8])
    
    Objeto.crearCubo("chassis")
    Especifico.escalar("chassis", (10, 6.5, 3))
    Especifico.posicionar("chassis", (2, 0, 2))
    Especifico.posicionar("chassis", (2, 0, 2))
    
    juntarObjetos(["RightFrontTyre", "LeftFrontTyre", "RightRearTyre", "LeftRearTyre", "chassis"])
        
    for obj in bpy.context.selected_objects:
        obj.name = "full_chassis"
        
    createUltrasound(-0.3, 0 ,2)
    
def singleTrack(position, id):
    for o in bpy.context.scene.objects:
        if o.name == id:
            return
    Objeto.crearCubo(id)
    Especifico.escalar(id, (0.2, 1, 0.3))
    Especifico.posicionar(id, position)
    
def createLeftTrack():
    track_ids = []
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, -2, 2.9 + z), "left track top " + str(x))
        track_ids.append("left track top " + str(x))
    
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, -2, 1.1 - z), "left track bot " + str(x))
        track_ids.append("left track bot " + str(x))  
        
    for x in range(0, 10):
        z = x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, -2, 2 + z), "left curved top " + str(x))
        track_ids.append("left curved top " + str(x))  
        
    for x in range(0, 10):
        z = -x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, -2, 2 + z), "left curved bot " + str(x))
        track_ids.append("left curved bot " + str(x))
        
    singleTrack((-0.9, -2, 2), "middle left curved " + str(x))
    track_ids.append("middle left curved " + str(x))
    
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, -2, 2.9 + z), "left track top " + str(x))
        track_ids.append("left track top " + str(x))
    
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, -2, 1.1 - z), "left track bot " + str(x))
        track_ids.append("left track bot " + str(x))  
        
    for x in range(0, 10):
        z = x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, -2, 2 + z), "left curved top " + str(x))
        track_ids.append("left curved top " + str(x))  
        
    for x in range(0, 10):
        z = -x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, -2, 2 + z), "left curved bot " + str(x))
        track_ids.append("left curved bot " + str(x))
        
    singleTrack((-0.9, -2, 2), "middle left curved " + str(x))
    track_ids.append("middle left curved " + str(x))
    
    for x in range(0, 13):
        z = x/10.3
        x = ((x-1)*(x-1))/139.0
        singleTrack((5.1 - x, -2, 2 + z), "right curved top " + str(x))
        track_ids.append("right curved top " + str(x))  
        
    for x in range(0, 13):
        z = -x/10.3
        x = ((x-1)*(x-1))/139.0
        singleTrack((5.1 - x, -2, 2 + z), "right curved bot " + str(x))
        track_ids.append("right curved bot " + str(x))
        
    singleTrack((5.1, -2, 2), "middle right curved " + str(x))
    track_ids.append("middle right curved " + str(x))
        
    juntarObjetos(track_ids)
    for obj in bpy.context.selected_objects:
        obj.name = "oruga_izq"
        
    track_ids.clear()
def createRightTrack():
    
    track_ids = []
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, 2, 2.9 + z), "left track top " + str(x))
        track_ids.append("left track top " + str(x))
    
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, 2, 1.1 - z), "left track bot " + str(x))
        track_ids.append("left track bot " + str(x))  
        
    for x in range(0, 10):
        z = x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, 2, 2 + z), "left curved top " + str(x))
        track_ids.append("left curved top " + str(x))  
        
    for x in range(0, 10):
        z = -x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, 2, 2 + z), "left curved bot " + str(x))
        track_ids.append("left curved bot " + str(x))
        
    singleTrack((-0.9, 2, 2), "middle left curved " + str(x))
    track_ids.append("middle left curved " + str(x))
    
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, 2, 2.9 + z), "left track top " + str(x))
        track_ids.append("left track top " + str(x))
    
    for x in range(0, 38):
        z = x/140.0
        x = x/9.0
        singleTrack((0 + x, 2, 1.1 - z), "left track bot " + str(x))
        track_ids.append("left track bot " + str(x))  
        
    for x in range(0, 10):
        z = x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, 2, 2 + z), "left curved top " + str(x))
        track_ids.append("left curved top " + str(x))  
        
    for x in range(0, 10):
        z = -x/10.0
        x = -((x-1)*(x-1))/85.0
        singleTrack((-0.9 - x, 2, 2 + z), "left curved bot " + str(x))
        track_ids.append("left curved bot " + str(x))
        
    singleTrack((-0.9, 2, 2), "middle left curved " + str(x))
    track_ids.append("middle left curved " + str(x))
    
    for x in range(0, 13):
        z = x/10.3
        x = ((x-1)*(x-1))/139.0
        singleTrack((5.1 - x, 2, 2 + z), "right curved top " + str(x))
        track_ids.append("right curved top " + str(x))  
        
    for x in range(0, 13):
        z = -x/10.3
        x = ((x-1)*(x-1))/139.0
        singleTrack((5.1 - x, 2, 2 + z), "right curved bot " + str(x))
        track_ids.append("right curved bot " + str(x))
        
    singleTrack((5.1, 2, 2), "middle right curved " + str(x))
    track_ids.append("middle right curved " + str(x))
        
    juntarObjetos(track_ids)
    for obj in bpy.context.selected_objects:
        obj.name = "oruga_der"
        
        
def createHead():
    Objeto.crearCilindro("cabeza")
    Especifico.posicionar("cabeza", (0.5,0,4.5))
    Especifico.rotar("cabeza", (PI/2, 0, 0))
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0), scale=(1, 1, 1))
    Activo.renombrar("face")
    Especifico.rotar("face", (0, PI/2, 0))
    Especifico.posicionar("face", (-0.5,0,4.6))
    Especifico.escalar("face", (0.3,0.4,1))
    
def createBody():
    Objeto.crearCubo("head rest")
    Especifico.posicionar("head rest", (0, 0, 3))
    Especifico.rotar("head rest", (0, PI/6, 0))
    Especifico.escalar("head rest", (1, 6.5, 2))
    
    Objeto.crearCubo("left side")
    Especifico.posicionar("left side", (1, -1.39, 4.2))
    Especifico.escalar("left side", (4, 1, 5.7))
    
    Objeto.crearCubo("right side")
    Especifico.posicionar("right side", (1, 1.39, 4.2))
    Especifico.escalar("right side", (4, 1, 5.7))
    
    Objeto.crearCubo("left end")
    Especifico.posicionar("left end", (3.25, -1.39, 3.5))
    Especifico.escalar("left end", (5, 1, 3))
    
    Objeto.crearCubo("right end")
    Especifico.posicionar("right end", (3.25, 1.39, 3.5))
    Especifico.escalar("right end", (5, 1, 3))
    
    Objeto.crearCilindro("back end")
    Especifico.rotar("back end", (PI/2, 0, 0))
    Especifico.posicionar("back end", (3.8, 0, 3.2))
    Especifico.escalar("back end", (0.7, 1, 1.4))
    
    Objeto.crearCubo("back cover")
    Especifico.posicionar("back cover", (3.25, 0, 4.3))
    Especifico.escalar("back cover", (5, 6.67, 0.7))
    
    Objeto.crearCubo("top cover")
    Especifico.posicionar("top cover", (1, 0, 5.7))
    Especifico.escalar("top cover", (4, 6.67, 0.7))
    
    juntarObjetos(["head rest", "left side", "right side", "left end", "right end", "back end", "back cover", "top cover"])
    for obj in bpy.context.selected_objects:
        obj.name = "bodywork"

def createArmJoint(position, n):
    Objeto.crearCilindro("arm joint " + n)
    Especifico.posicionar("arm joint " + n, position )
    Especifico.rotar("arm joint " + n, (PI/2, 0, 0))
    Especifico.escalar("arm joint " + n, (0.2, 0.2, 0.2))
    
def createArm(jointX, jointY, jointZ, n):
    createArmJoint((jointX, jointY, jointZ), n)
    Objeto.crearCubo("top arm " + n)
    Especifico.posicionar("top arm " + n, (jointX - 1.4, jointY, jointZ + 0.2))
    Especifico.rotar("top arm " + n, (0, PI/20, 0))
    Especifico.escalar("top arm " + n, (6, 0.5, 0.5))
    
    Objeto.crearCubo("bot arm " + n)
    Especifico.posicionar("bot arm " + n, (jointX - 3.3, jointY, jointZ - 0.3))
    Especifico.rotar("bot arm " + n, (0, -PI/3, 0))
    Especifico.escalar("bot arm " + n, (4, 0.5, 0.5))
    
    juntarObjetos(["bot arm " + n, "top arm " + n, "arm joint " + n])
    for obj in bpy.context.selected_objects:
        obj.name = "arm " + n

    
def createArms():
    createArm(2.4, -1.8, 4.2, "1")
    createArm(2.4, -1.8, 3.4, "2")
    
    createArm(2.4, 1.8, 4.2, "3")
    createArm(2.4, 1.8, 3.4, "4")
    
    juntarObjetos(["arm 1", "arm 2", "arm 3", "arm 4"])
    for obj in bpy.context.selected_objects:
        obj.name = "arms"
    

def createGripper():
    Objeto.crearCubo("left side")
    Especifico.posicionar("left side", (-1.4, -1.8,  2.5))
    Especifico.escalar("left side", (0.9, 0.9, 5))
    
    Objeto.crearCubo("right side")
    Especifico.posicionar("right side", (-1.4, 1.8,  2.5))
    Especifico.escalar("right side", (0.9, 0.9, 5))
    
    Objeto.crearCubo("bottom")
    Especifico.posicionar("bottom", (-1.4, 0, 1.48))
    Especifico.escalar("bottom", (0.9, 7, 0.9))
    
    Objeto.crearCubo("left clamp")
    Especifico.rotar("left clamp",(0, -PI/7, 0) )
    Especifico.posicionar("left clamp", (-1.7, -1.57, 2.8))
    Especifico.escalar("left clamp", (0.2, 0.2, 1.5))
    
    Objeto.crearCubo("right clamp")
    Especifico.rotar("right clamp",(0, -PI/7, 0) )
    Especifico.posicionar("right clamp", (-1.7, 1.57, 2.8))
    Especifico.escalar("right clamp", (0.2, 0.2, 1.5))
    
    juntarObjetos(["right clamp", "left clamp", "bottom", "right side", "left side"])
    for obj in bpy.context.selected_objects:
        obj.name = "gripper"
    
def createHook():
    Objeto.crearCubo("top")
    Especifico.posicionar("top", (5.5, 0, 5))
    Especifico.escalar("top", (0.2, 0.2, 0.5))
    
    Objeto.crearCubo("right")
    Especifico.posicionar("right", (5.57, 0, 4.85))
    Especifico.escalar("right", (0.5, 0.2, 0.2))
    
    Objeto.crearCubo("middle")
    Especifico.posicionar("middle", (5.7, 0, 4.64))
    Especifico.escalar("middle", (0.2, 0.2, 1))
    
    Objeto.crearCubo("bottom")
    Especifico.rotar("bottom",(0, -PI/4, 0))
    Especifico.posicionar("bottom", (5.6, 0, 4.35))
    Especifico.escalar("bottom", (0.5, 0.2, 0.2))
    
    juntarObjetos(["top", "right", "middle", "bottom"])
    for obj in bpy.context.selected_objects:
        obj.name = "hook"
    
def createCrane():
    Objeto.crearCubo("left guide")
    Especifico.rotar("left guide",(0, PI/3, PI/10))
    Especifico.posicionar("left guide", (4, -0.5, 5))
    Especifico.escalar("left guide", (0.5, 0.5, 7))
    
    Objeto.crearCubo("right guide")
    Especifico.rotar("right guide",(0, PI/3, -PI/10))
    Especifico.posicionar("right guide", (4, 0.5, 5))
    Especifico.escalar("right guide", (0.5, 0.5, 7))
    
    Objeto.crearCubo("rope 1")
    Especifico.rotar("rope 1" ,(0, PI/3, 0))
    Especifico.posicionar("rope 1" , (4, 0, 5))
    Especifico.escalar("rope 1", (0.05, 0.05, 7))
    
    Objeto.crearCubo("rope 2")
    Especifico.posicionar("rope 2" , (5.5, 0, 5.5))
    Especifico.escalar("rope 2", (0.05, 0.05, 2))
    
    createHook()
    
    juntarObjetos(["left guide", "right guide", "rope 1", "rope 2", "hook"])
    for obj in bpy.context.selected_objects:
        obj.name = "crane"
    
def main():
    borrarObjetos()
    createChassis()
    createLeftTrack()
    createRightTrack()
    createHead()
    createBody()
    createArms()
    createGripper()
    createCrane()
    
if __name__ == "__main__":
    main()