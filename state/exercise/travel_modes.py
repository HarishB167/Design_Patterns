from .travel_mode_interface import TravelModeInterface


class DrivingMode(TravelModeInterface):
    def getEta(self):
        print("Calculating ETA (driving)")

    def getDirection(self):
        print("Calculating Direction (driving)")


class BicyclingMode(TravelModeInterface):
    def getEta(self):
        print("Calculating ETA (bicycling)")

    def getDirection(self):
        print("Calculating Direction (bicycling)")


class TransitMode(TravelModeInterface):
    def getEta(self):
        print("Calculating ETA (transit)")

    def getDirection(self):
        print("Calculating Direction (transit)")


class WalkingMode(TravelModeInterface):
    def getEta(self):
        print("Calculating ETA (walking)")

    def getDirection(self):
        print("Calculating Direction (walking)")

