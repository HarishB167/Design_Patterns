from .travel_mode_interface import TravelModeInterface

class DirectionService:
    __travel_mode: TravelModeInterface = None
    
    def getEta(self):
        self.__travel_mode.getEta()

    def getDirection(self):
        self.__travel_mode.getDirection()

    def getTravelMode(self):
        return self.__travel_mode

    def setTravelMode(self, travel_mode):
        self.__travel_mode = travel_mode

