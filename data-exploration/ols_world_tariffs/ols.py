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

model = sm.OLS(Y, sm.add_constant(X)).fit()

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

# Add the line of best fit
x_fit = data['l_lnsmfn']
y_fit = data['imf']
z_fit = data['polity']

predicted_dlnsmfn = model.params[0] + model.params[1] * x_fit + model.params[3] * y_fit + model.params[6] * z_fit

fig.add_trace(go.Scatter3d(x=x_fit, y=y_fit, z=z_fit, mode='markers', marker=dict(color=predicted_dlnsmfn, colorscale='Viridis', size=2)))

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

# Save the JSON object to a file
with open('plot_data.json', 'w') as file:
    file.write(plot_json)