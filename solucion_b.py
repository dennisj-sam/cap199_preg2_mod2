# Solución
import pandas as pd
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"
df = pd.read_csv(url, compression='zip')
df.info()
