# Plotly template SSB design

[![PyPI](https://img.shields.io/pypi/v/ssb-plotly-template.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/ssb-plotly-template.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/ssb-plotly-template)][pypi status]
[![License](https://img.shields.io/pypi/l/ssb-plotly-template)][license]

[![Documentation](https://github.com/statisticsnorway/ssb-plotly-template/actions/workflows/docs.yml/badge.svg)][documentation]
[![Tests](https://github.com/statisticsnorway/ssb-plotly-template/actions/workflows/tests.yml/badge.svg)][tests]
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=statisticsnorway_ssb-plotly-template&metric=coverage)][sonarcov]
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=statisticsnorway_ssb-plotly-template&metric=alert_status)][sonarquality]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)][poetry]

[pypi status]: https://pypi.org/project/ssb-plotly-template/
[documentation]: https://statisticsnorway.github.io/ssb-plotly-template
[tests]: https://github.com/statisticsnorway/ssb-plotly-template/actions?workflow=Tests

[sonarcov]: https://sonarcloud.io/summary/overall?id=statisticsnorway_ssb-plotly-template
[sonarquality]: https://sonarcloud.io/summary/overall?id=statisticsnorway_ssb-plotly-template
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black
[poetry]: https://python-poetry.org/

A Python library that provides a custom Plotly template for visualising data with consistent styling and layout. The font and colours follow the SSB Design-system https://design.ssb.no

This is not an official template. The template is still under development.

## Features

- Custom Plotly layout that can be easily applied to any figure.
- Includes predefined color schemes, fonts, and other styling options.
- Compatible with Plotly go chart types, including bar, line, scatter, and Plotly tables.


## Requirements

- Python 3.x
- Plotly 5.x or higher

## Installation

You can install _Plotly template SSB design_ via [pip] from [PyPI]:

```console
pip install ssb-plotly-template
```

## Usage

After installing the library, you can easily apply the custom Plotly template to your figures. Here’s how to use it:

1. Import both Plotly and ssb-plotly-template
2. Create a Plotly figure.  with the ssb-plotly-template template.

### Example
Import libraries and create data:
```
import ssb_plotly_template
import plotly.graph_objects as go
import pandas as pd


data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 23, 15, 7],
    "Values2": [13, 22, 25, 17],
    "Values3": [23, 23, 28, 27],
    "Dates": ["2024-10-01", "2024-10-05", "2024-10-10", "2024-10-15"],
}

df = pd.DataFrame(data)
df["Dates"] = pd.to_datetime(df["Dates"])
```

Create Plotly Go bar chart with ssb-plotly-template.
```
bar_chart = go.Figure(
    data=[go.Bar(x=df["Category"], y=df["Values"])],
    layout_title_text="Bar Chart",
    layout_template="ssb_plotly_template",
)

bar_chart.show()
```

Create timeline (scatter plot) with multiple lines with ssb-plotly-template.

```
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
```

Create Plotly Table with ssb-plotly-template.

```
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
```


## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Plotly template SSB design_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [Statistics Norway]'s [SSB PyPI Template].

[statistics norway]: https://www.ssb.no/en
[pypi]: https://pypi.org/
[ssb pypi template]: https://github.com/statisticsnorway/ssb-pypitemplate
[file an issue]: https://github.com/statisticsnorway/ssb-plotly-template/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/statisticsnorway/ssb-plotly-template/blob/main/LICENSE
[contributor guide]: https://github.com/statisticsnorway/ssb-plotly-template/blob/main/CONTRIBUTING.md
[reference guide]: https://statisticsnorway.github.io/ssb-plotly-template/reference.html
