from modules.Knit_HEADLESS import HeadlessHorseman
from modules.reader import Reader
from modules.model import Model
from modules.components.button import Button


reader = Reader("KNIT\\workflows\\models\\model3\\model-three-workflow-three.json")
reader.readModel()
model = Model(reader)
model.loadZipFunctions()
horseman = HeadlessHorseman(model)
horseman.run()
