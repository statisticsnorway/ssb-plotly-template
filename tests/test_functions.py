# test_plotly_template.py
import plotly.io as pio
import ssb_plotly_template.ssb_plotly_template  # noqa: F401


def test_ssb_plotly_template() -> None:

    # Check if the template is correctly applied
    template = pio.templates["ssb_plotly_template"]

    # Check that the font family in the layout is set correctly
    assert (
        template.layout.font.family == "Open Sans, Sans-serif"
    ), "Font family should be 'Open Sans, Sans-serif'"

    # Check that the title font color is correct
    assert (
        template.layout.title.font.color == "#162327"
    ), "Title font color should be '#162327'"

    # Check that the x-axis line color is correct
    assert (
        template.layout.xaxis.linecolor == "#274247"
    ), "x-axis line color should be '#274247'"
