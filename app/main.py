from modules.knit_GUI import KnitGUI
from modules.reader import Reader
from modules.model import Model
from modules.components.button import Button


reader = Reader("KNIT\\workflows\\models\\model3\\model-three-workflow-three.json")
reader.readModel()
model = Model(reader)
model.loadZipFunctions()
gui = KnitGUI(model)
gui.run()



# print(model)
# model.loadZipFunctions()
# for name in model.getFunctions().keys():
#     function = model.getFunctions()[name]
#     function()

# for node in model.getNodes():
#     print(node.getFunction())

