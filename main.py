import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

points = [
    # Center Section
    {"x": 5, "y": 5, "z": 0},
    # Top-Left to Center
    {"x": 1, "y": 10, "z": 0},
    # Top-Right to Center
    {"x": 10, "y": 10, "z": 0},
    # Bottom-Left to Center
    {"x": 1, "y": 1, "z": 0},
    # Bottom-Right to Center
    {"x": 10, "y": 1, "z": 0},
]

df = pd.DataFrame(points)

grid_resolution = 50
grid_x, grid_y = np.meshgrid(
    np.linspace(df.x.min(), df.x.max(), grid_resolution),
    np.linspace(df.y.min(), df.y.max(), grid_resolution),
)

# Interpolate Z values to create surface (using linear for stability with few points)
z = griddata((df.x, df.y), df.z, (grid_x, grid_y), method="linear")

sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title=dict(text="CNC Bed Surface"), autosize=True)
fig.show()
