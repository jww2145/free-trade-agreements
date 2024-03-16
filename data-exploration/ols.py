import pandas as pd
import statsmodels.api as sm
import plotly.graph_objects as go


import json


df = pd.read_csv('/Users/joshiebestie/Downloads/linear regression project/trade blocs tariffs.csv')

data = df.dropna()
cluster_var = data['isocode']
Y = data['dlnsmfn']
X = data[['l_lnsmfn', 'dxr', 'imf', 'fsharec', 'wlrcac', 'polity']]

X = sm.add_constant(X)

model = sm.OLS(Y, sm.add_constant(X)).fit('pinv','cluster',{'groups': cluster_var})

print(model.summary())

model_summary = model.summary().as_csv()
with open('model_summary.csv', 'w') as file:
    file.write(model_summary)



# Create the 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=data['l_lnsmfn'],
    y=data['imf'],
    z=data['polity'],
    mode='markers',
    marker=dict(
        size=5,
        color=data['dlnsmfn'],
        colorscale='Viridis',
        opacity=0.8
    )
)])

# Add layout and title
fig.update_layout(
    scene=dict(
        xaxis_title='Initial MFN',
        yaxis_title='IMF',
        zaxis_title='Polity'
    ),
    width=800,
    height=600,
    margin=dict(r=20, b=10, l=10, t=10)
)

# Export the plot as a JSON object
plot_json = fig.to_json()

with open('plot_data.json', 'w') as file:
    file.write(plot_json)