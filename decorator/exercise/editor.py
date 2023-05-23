from .artifact import Artifact
from .main_marker import MainMarker
from .error_marker import ErrorMarker

class Editor:
    def open_project(self, path:str):
        artifacts = [
            Artifact("Main"),
            Artifact("Demo"),
            Artifact("EmailClient"),
            Artifact("EmailProvider"),
        ]

        artifacts[0] = MainMarker(artifacts[0])
        artifacts[2] = ErrorMarker(artifacts[2])

        for artifact in artifacts:
            print(artifact.render())

