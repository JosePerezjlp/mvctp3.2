from ..database import DatabaseConnection


class Bikes:
    def __init__(self, customer_id = None, first_name = None, last_name = None, phone = None, email=None , street=None , city=None , state=None , zip_code=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city,
        self.state = state,
        self.zip_code = zip_code 
        

    @classmethod
    def get_customers(cls):
        query = "SELECT * FROM sales.customers" 
        result = DatabaseConnection.fetch_all(query)
        total_customers = len(result)
        if result is not None:
            customers = [Bikes(first_name=row[0], last_name=row[1]) for row in result]
            total_customers = len(customers)
            return customers, total_customers
        else:
            return None  
    @classmethod
    def get_customer(self,customer_id):
       query = 'SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM customers WHERE customer_id = %s;'
       params = (customer_id,)
       
       result = DatabaseConnection.fetch_one(query, params)
       print(type(result))
       if result is not None:
            return Bikes(
                customer_id = customer_id,
                first_name = result[0],
                last_name = result[1],           
        )
       else:
            return None    

    @classmethod
    def create_customer(cls, customer):
        query = "INSERT INTO sales.customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        params = customer
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update_customer(cls, customer_id, updated_customer_data):
        query = "UPDATE sales.customers SET first_name = %s, last_name = %s, phone = %s, email = %s, street = %s, city = %s, state = %s, zip_code = %s WHERE customer_id = %s;"
        
        params = (
            updated_customer_data['first_name'],
            updated_customer_data['last_name'],
            updated_customer_data['phone'],
            updated_customer_data['email'],
            updated_customer_data['street'],
            updated_customer_data['city'],
            updated_customer_data['state'],
            updated_customer_data['zip_code'],
            customer_id
        )
        
        DatabaseConnection.execute_update(query, params)

    @classmethod
    def delete_customer(cls, customer_id):
        query = "DELETE FROM sales.customers WHERE customer_id = %s;"
        params = (customer_id,)

        DatabaseConnection.execute_delete(query, params)        


