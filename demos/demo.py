# %% [markdown]
# # Demo
#
# Creating some Plotly figures and a table with the ssb_plotly_template

# %%
# import

import os
import pandas as pd

# %%
# Change directory until find project root
notebook_path = os.getcwd()
for folder_level in range(50):
    if "pyproject.toml" in os.listdir():
        break
    os.chdir("../")

# %%
# import plotly template
# ruff: noqa: F401
import ssb_plotly_template.ssb_plotly_template

# %%
import plotly.graph_objects as go

data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 23, 15, 7],
    "Values2": [13, 22, 25, 17],
    "Values3": [23, 23, 28, 27],
    "Dates": ["2024-10-01", "2024-10-05", "2024-10-10", "2024-10-15"],
}

df = pd.DataFrame(data)
df["Dates"] = pd.to_datetime(df["Dates"])


bar_chart = go.Figure(
    data=[go.Bar(x=df["Category"], y=df["Values"])],
    layout_title_text="Bar Chart",
    layout_template="ssb_plotly_template",
)


bar_chart.show()

# %%
# Create a timeline (scatter plot) with multiple lines
timeline_chart = go.Figure(
    data=[
        go.Scatter(x=df["Dates"], y=df["Values"], mode="lines+markers", name="Line 1"),
        go.Scatter(x=df["Dates"], y=df["Values2"], mode="lines+markers", name="Line 2"),
        go.Scatter(x=df["Dates"], y=df["Values3"], mode="lines+markers", name="Line 2"),
    ],
    layout_title_text="Timeline",
    layout_template="ssb_plotly_template",
)

timeline_chart.show()

# %%
# Create Plotly Table
fig_table = go.Figure(
    data=[
        go.Table(
            header=dict(values=list(df.columns)),
            cells=dict(values=[df[col].tolist() for col in df.columns]),
        )
    ]
)

fig_table.update_layout(template="ssb_plotly_template", title="Table")

fig_table.show()

# %%
