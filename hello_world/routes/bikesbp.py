from flask import Blueprint
from ..controllers.bikes_controller import BikesController
bikesbp = Blueprint('actor_bp',__name__)

bikesbp.route('/customers', methods = ['GET'])(BikesController.get_all)
bikesbp.route('/customers', methods = ['POST'])(BikesController.create_custom)
bikesbp.route('/customer/<int:customer_id>', methods = ['GET'])(BikesController.get_custom)
bikesbp.route('/customers/<int:customer_id>', methods = ['PUT'])(BikesController.update_custom)
bikesbp.route('/customers/<int:customer_id>', methods = ['DELETE'])(BikesController.delete_custom)


