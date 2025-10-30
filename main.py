import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

points = [
    {"x": 1, "y": 10, "z": 4.8},  # Top-left corner
    {"x": 10, "y": 1, "z": 4.2},  # Bottom-right corner
    {"x": 10, "y": 10, "z": 5}, # Top-right corner
    {"x": 1, "y": 1, "z": 4}, # Bottom-left corner
    {"x": 5, "y": 5, "z": 4.5}, # Center point
]

df = pd.DataFrame(points)

grid_x, grid_y = np.meshgrid(
    np.linspace(df.x.min(), df.x.max(), 50), np.linspace(df.y.min(), df.y.max(), 50)
)

# Interpolate Z values to create surface (using linear for stability with few points)
z = griddata((df.x, df.y), df.z, (grid_x, grid_y), method="linear")

sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(
    title=dict(text="CNC Bed Surface"),
    autosize=False,
    width=500,
    height=500,
    margin=dict(l=65, r=50, b=65, t=90),
)
fig.show()
