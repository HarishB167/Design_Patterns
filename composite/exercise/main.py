from .team import Team
from .truck import Truck
from .human_resource import HumanResource

if __name__ == "__main__":
    subteam1 = Team()
    subteam1.add(Truck())
    subteam1.add(HumanResource())
    subteam1.add(HumanResource())

    subteam2 = Team()
    subteam2.add(Truck())
    subteam2.add(HumanResource())
    subteam2.add(HumanResource())

    team = Team()
    team.add(subteam1)
    team.add(subteam2)
    
    team.deploy()
