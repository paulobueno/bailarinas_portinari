# Bailarinas
## Portinari's tale design  
An application destinated to help design walls covered by Portinari's tales called 'Bailarinas'  
It is a regular triangular tile, available in 8 different colors, suit to decorate internal and external areas  
<img src="https://drive.google.com/uc?export=view&id=1CKdgfwH62n0RRELX84s7uDj3vRtfqD7e" alt="Portinari's Bailarinas" width="400"/>

Application's output example:  
![alt text](https://drive.google.com/uc?export=view&id=1JJEjaQX80Fc3axN_8wcnDg-hV7Zsk-mR "Output example")

### requirements
Must install tkinter to visualize the output when executing matplot_test.py

Code to generate the image above:  
```python
bailarinas = to.TileClass('Bailarina')
parede = to.Wall(246, 96)
pedido = to.Order(parede, bailarinas)
wall_preview(pedido)
```  

The result at my place:  
<img src="https://drive.google.com/uc?export=view&id=1zXG2vB29U_kHR5hiv6GU1TSmbg_iNmTk" alt="Result" width="400"/>
