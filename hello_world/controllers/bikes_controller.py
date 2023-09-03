from ..models.Bikes_1 import Bikes
from flask import request
from flask import jsonify

class BikesController:
    @classmethod
    def get_all(cls):
        customers, total_customers = Bikes.get_customers()          # type: ignore
        
        
        if customers:
            data = []
            response_data = {}
            for customer in customers:
                customer_data = {
                    "nombre": customer.first_name,
                    "apellido": customer.last_name,
                    
                }
                data.append(customer_data)
                response_data = {"clientes":data,
                                 "total":total_customers}
            return jsonify(response_data), 200

        else:
            return {"msg": "No se encontraron clientes"}, 404
    
    @classmethod
    def get_custom(cls, customer_id):
        actor_instance = Bikes.get_customer(customer_id)         
             
        
        if actor_instance:
            response_data = {
                "id": actor_instance.customer_id,
                "nombre": actor_instance.first_name,
                "apellido": actor_instance.last_name,
                
                }
            
            return jsonify(response_data), 200
        
        else:
    
            return {"msg": "No se encontró el actor"}, 404
        
    @classmethod
    def create_custom(cls):
       
       if request.args.get('first_name') is not None:
        first_name = str(request.args.get('first_name', ''))
        last_name = str(request.args.get('last_name', ''))
        phone = str(request.args.get('phone', ''))
        email = str(request.args.get('email', ''))
        street = str(request.args.get('street', ''))
        city = str(request.args.get('city', ''))
        state = str(request.args.get('state', ''))
        zip_code = str(request.args.get('zip_code', ''))

 
        data = (first_name, last_name, phone, email, street, city, state, zip_code)       
        Bikes.create_customer(data)

        return {'message': 'Actor creado con éxito'}, 200
       else:
           return{'message': 'todos los campos son obligatorios'},400
    @classmethod
    def update_custom(cls, customer_id):
       
        existing_customer = Bikes.get_customer(customer_id)
        if not existing_customer:
            return {'message': 'El cliente no existe'}, 404

        updated_customer_data = {
            'first_name': request.args.get('first_name', existing_customer.first_name),
            'last_name': request.args.get('last_name', existing_customer.last_name),
            'phone': request.args.get('phone', existing_customer.phone),
            'email': request.args.get('email', existing_customer.email),
            'street': request.args.get('street', existing_customer.street),
            'city': request.args.get('city', existing_customer.city),
            'state': request.args.get('state', existing_customer.state),
            'zip_code': request.args.get('zip_code', existing_customer.zip_code)
        }

        Bikes.update_customer(customer_id, updated_customer_data)

        return {'message': 'Cliente actualizado con éxito'}, 200
   
    @classmethod
    def delete_custom(cls, customer_id):
        existing_customer = Bikes.get_customer(customer_id)
        if not existing_customer:
            return {'message': 'El cliente no existe'}, 404

        Bikes.delete_customer(customer_id)

        return {'message': 'Cliente eliminado con éxito'}, 200