import pandas as pd
import plotly.graph_objects as go
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/time_series/time-series-data.csv')


X = df[['IMPGS', 'INTDSRUSM193N', 'New House Sale', 'S&P Returns', 'UNRATE', 'WM2NS', 'GDPC1','T10Y2Y']]
corr_matrix = X.corr()

# Create a mask to color only the upper triangular cells
mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=0)

# Create a heatmap using Plotly
fig = go.Figure(data=go.Heatmap(
    z=corr_matrix.mask(~mask).values,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    colorscale='Viridis',
    zmin=-1,
    zmax=1
))

# Customize the layout
fig.update_layout(
    title='Correlation Matrix Heatmap (Upper Triangular)',
    xaxis_title='Features',
    yaxis_title='Features',
    width=800,
    height=800,
    autosize=False
)

# Display the plot
fig.show()