import plotly.graph_objects as go
import plotly.io as pio

pio.templates["ssb_plotly_template"] = go.layout.Template(
    layout={
        "title": {
            "font": {"family": "Roboto, Sans-serif", "size": 20, "color": "#162327"},
            "pad": {"b": 28},  # (linjeavstand)
        },
        # Fonts for other text and labels
        "font": {"family": "Open Sans, Sans-serif", "size": 16, "color": "#162327"},
        # SSB sorted priority colours
        "colorway": [
            "#1A9D49",
            "#075745",
            "#1D9DE2",
            "#0F2080",
            "#C78800",
            "#471F00",
            "#C775A7",
            "#A3136C",
            "#909090",
        ],
        # Framework lines and background colors
        "xaxis": {
            "showgrid": False,
            "linecolor": "#274247",
            "ticks": "outside",
            "zeroline": False,
            "showline": True,
            "tickmode": "linear",
            "automargin": True,
        },
        "yaxis": {
            "showgrid": True,
            "gridcolor": "#C3DCDC",
            "linecolor": "#274247",
            "ticks": "outside",
            "zeroline": False,
            "showline": True,
            "automargin": True,
        },
        "plot_bgcolor": "#FFFFFF",
    },
    data={
        # Scatter plot settings
        "scatter": [
            go.Scatter(
                mode="lines+markers",
                marker=dict(symbol="circle", size=8),
                line=dict(width=2),
            )
        ],
        # Table settings
        "table": [
            go.Table(
                header=dict(
                    fill_color="#FFFFFF",
                    font=dict(color="#162327", size=18),
                    align="left",
                    height=40,
                    line=dict(color="#C3DCDC", width=1),
                ),
                cells=dict(
                    fill_color=[["#ECFEED", "#FFFFFF"] * 100],
                    font=dict(color="#162327", size=16),
                    align="right",
                    height=40,
                    line=dict(color="#C3DCDC", width=1),
                ),
            )
        ],
    },
)

pio.templates.default = "ssb_plotly_template"
