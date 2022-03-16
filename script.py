import bpy
import sys
sys.path.append('/home/chuismi/Desktop/robotica/tercero/segundocuat/modelado')
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
    
    juntarObjetos(["us der", "us izq", "base us"])
    for obj in bpy.context.selected_objects:
        obj.name = "ultrasound"
    
    
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
    
    createUltrasound(-0.3, 0 ,2)
    
    juntarObjetos(["RightFrontTyre", "LeftFrontTyre", "RightRearTyre", "LeftRearTyre", "chassis", "ultrasound"])
        
    for obj in bpy.context.selected_objects:
        obj.name = "full_chassis"
        

def singleTrack(position, id):
    Objeto.crearCubo(id)
    Especifico.escalar(id, (0.2, 1.8, 0.2))
    Especifico.posicionar( id, position)
    
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
    
def main():
    borrarObjetos()
    createChassis()
    createLeftTrack()
    createRightTrack()
    
if __name__ == "__main__":
    main()