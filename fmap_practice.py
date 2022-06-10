import numpy as np
from PIL import Image, ImageDraw



w, h= 1000, 1000
fmap= Image.new("RGB", (w,h), ("Black"))
draw = ImageDraw.Draw(fmap)
npuntos = 0
while npuntos < 20000:
    lista_patron = [-1, 0, 1]
    seedx = (lista_patron[np.random.randint(0,3)])
    seedy = (lista_patron[np.random.randint(0,3)])
    coordinate_f = (500,500)
    seed = (seedx, seedy)
    difx = 0
    dify = 0
    if npuntos == 0:
        x = coordinate_f[0]+seedx
        y = coordinate_f[1]+seedy
        coordinate_n = (x,y)
        print('este es coordinate_n')
        print(coordinate_n)
        npuntos = npuntos + 1
    while npuntos != 300000:
        seedx_1 = (lista_patron[np.random.randint(0,3)])
        seedy_1 = (lista_patron[np.random.randint(0,3)])
        contador = npuntos 
        x1 = x + seedx_1 + difx
        y1 = y + seedy_1 + dify
        coordinate_n1 = (x1,y1)
        npuntos = npuntos + 1
        draw.point((coordinate_n1), "Green")
        difx = difx + lista_patron[np.random.randint(0,3)]
        dify = dify + lista_patron[np.random.randint(0,3)]
    if npuntos == 300000:
        fmap.show()

