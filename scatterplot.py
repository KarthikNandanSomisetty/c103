import pandas as pd
import plotly.express as px
import plotly

df = pd.read_csv("c:/Users/Somisetty Karthik/Dropbox/My PC (LAPTOP-PJB0FTAK)/Downloads/data.csv")
fig = px.scatter(df, x="Population", y="Per capita",
	          size="Percentage",color="Country",
                   size_max=60)
plotly.offline.plot(fig)