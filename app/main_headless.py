from modules.Knit_HEADLESS import HeadlessHorseman # type: ignore
from modules.reader import Reader # type: ignore
from modules.model import Model # type: ignore
from modules.components.button import Button # type: ignore


reader = Reader("workflows\\models\\model3\\model-three-workflow-three.json")
reader.readModel()
model = Model(reader)
model.loadZipFunctions()
horseman = HeadlessHorseman(model)
horseman.run()


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
 
