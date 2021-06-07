import pandas as pd

import plotly.express as px
import plotly

df = pd.read_csv("c:/Users/Somisetty Karthik/Dropbox/My PC (LAPTOP-PJB0FTAK)/Downloads/line_chart.csv")

fig = px.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

#fig.show()
plotly.offline.plot(fig)