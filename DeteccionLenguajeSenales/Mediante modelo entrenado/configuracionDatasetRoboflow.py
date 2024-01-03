from roboflow import Roboflow

rf = Roboflow(api_key="xxxxxxxxxxxx")
project = rf.workspace("david-lee-d0rhs").project("american-sign-language-letters")
dataset = project.version(1).download("yolov8")