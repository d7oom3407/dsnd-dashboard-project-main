from pathlib import Path
from sqlite3 import connect
import pandas as pd

pth = f"{__file__[:-7]}\\employee_events.db"



print(Path('employee_events.db').resolve())