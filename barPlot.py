import pandas as pd

import plotly.express as px
import plotly

df = pd.read_csv("c:/Users/Somisetty Karthik/Dropbox/My PC (LAPTOP-PJB0FTAK)/Downloads/data.csv")

fig = px.bar(df, x='Country', y='InternetUsers')
#fig.show()
plotly.offline.plot(fig)