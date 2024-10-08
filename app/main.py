from modules.knit_GUI import KnitGUI
from modules.reader import Reader
from modules.model import Model
from modules.components.button import Button

reader = Reader("model-three-workflow-three.json")
reader.readModel()
model = Model(reader)
model.loadZipFunctions()
gui = KnitGUI(model)
gui.run()


# root (dir)
#  |-> app (dir)
#  |    |-> main.py
#  |    |-> main_headless.py
#  |    |-> modules (dir)
#  |            |-> assets (dir)
#  |            |-> components (dir)
#  |-> workflows (dir)
#  |-> model1 (dir)
#  |-> model2 (dir)
#  |-> model3 (dir)
#         |-> model-three-workflow-three.json
#         |-> RAG_ToolKit.py
#         |-> RAG_Server.py
#         |-> RAG_Manager.py
#         |-> zipFunctions (dir)
#                  |-> func1.py
#                  |-> func2.py
#                  |-> func3.py
#                  |-> func4.py
 

