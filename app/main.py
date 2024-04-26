from modules.knit_GUI import KnitGUI

from modules.reader import Reader
from modules.model import Model


reader = Reader("C:/Users/Ethan/Documents/KNIT/workflows/models/model1/model-one-workflow-one.json")
reader.readModel()
model = Model(reader)
gui = KnitGUI(model)
gui.run()



# print(model)
# model.loadZipFunctions()
# for name in model.getFunctions().keys():
#     function = model.getFunctions()[name]
#     function()

# for node in model.getNodes():
#     print(node.getFunction())

