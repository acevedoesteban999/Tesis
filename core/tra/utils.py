from core.as7265x import AS7265X
from .models import Training
#from core.meas.models import Measuring,MeasuringData
from core.meas.utils import MeasuringI2C
import time
def TrainingI2C(name,count):
    tr=Training.objects.create(
        name=name,
        count=count,
    )
    for count in range(int(count)):
        MeasuringI2C(f"TR~{tr.name}~{count}",tr)
        