from .customer_service import CustomerService
from .fx.command_interface import CommandInterface

class AddCustomerCommand(CommandInterface):
    __service: CustomerService = None

    def __init__(self, service: CustomerService):
        self.__service = service

    def execute(self):
        self.__service.add_customer()