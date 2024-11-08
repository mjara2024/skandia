from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import jsonpickle
import json 
import requests


aplicacion = FastAPI()

#definimos la clase producto con los valores esperados por fake store api
class Producto(BaseModel):
  title: str
  price: int
  description: str
  image: str
  category: str



#GET para consultar productos se envia el ID del producto
@aplicacion.get("/GET/{id}")
async def consultar_producto(id: int):
    try:
        response = requests.get(f"https://fakestoreapi.com/products/{id}")

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code,detail="fallo el cosumo del api")    
    except Exception as e: 
            raise HTTPException(status_code=response.status_code, detail="fallo general consulta") 



#POST para crear un nuevo producto.   se convierte la clas Producto a JSON
@aplicacion.post("/POST")
async def insertar_producto(producto: Producto):
    try:
        productoJson = jsonpickle.encode(producto)
        response = requests.post(f"https://fakestoreapi.com/products/",{productoJson})

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code,detail="fallo el cosumo del api")    
    except Exception as e: 
            raise HTTPException(status_code=response.status_code, detail="fallo general ingreso") 
               

#PUT para actualizar un producto existente.   se convierte la clas Producto a JSON
@aplicacion.put("/PUT")
async def actualizar_producto(producto: Producto):
    try:
        productoJson = jsonpickle.encode(producto)
        response = requests.post(f"https://fakestoreapi.com/products/",{productoJson})

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code,detail="fallo el cosumo del api")    
    except Exception as e: 
            raise HTTPException(status_code=response.status_code, detail="fallo general Actualizaciòn") 


#DELETE para eliminar un producto específico.. se convierte la clas Producto a JSON
@aplicacion.delete("/DELETE")
async def borrar_producto(producto: Producto):
    try:
        productoJson = jsonpickle.encode(producto)
        response = requests.post(f"https://fakestoreapi.com/products/",{productoJson})

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code,detail="fallo el cosumo del api")    
    except Exception as e: 
            raise HTTPException(status_code=response.status_code, detail="fallo general borrado")            