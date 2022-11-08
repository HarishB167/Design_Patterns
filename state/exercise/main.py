from .direction_service import DirectionService
from .travel_modes import DrivingMode, BicyclingMode, TransitMode, WalkingMode

if __name__ == "__main__":
    service = DirectionService()
    service.setTravelMode(WalkingMode())
    service.getEta()
    service.getDirection()