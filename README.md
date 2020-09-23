# Bailarinas
## Portinari's tale design  
An application destinated to help design walls covered by Portinari's tales called 'Bailarinas'  
It is a regular triangular tile, available in 8 different colors, suit to decorate internal and external areas  
<img src="https://tanto.com.br/wp-content/uploads/2018/04/Bailarinas-Portinari.jpg" alt="Portinari's Bailarinas" width="400"/>

Application's output example:  
![alt text](https://s3-sa-east-1.amazonaws.com/pythonprojects.fun/static/img/myplot_sample.png "Output example")

Code to generate the image above:  
```python
bailarinas = to.TileClass('Bailarina')
parede = to.Wall(246, 96)
pedido = to.Order(parede, bailarinas)
wall_preview(pedido)
```  

The result at my place:  
<img src="https://s3-sa-east-1.amazonaws.com/pythonprojects.fun/static/img/triangle_5.jpg" alt="Result" width="400"/>