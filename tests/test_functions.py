# test_plotly_template.py
import plotly.io as pio


def test_ssb_plotly_template():

    # Check if the template is correctly applied
    template = pio.templates["ssb_plotly_design_template"]

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

    # Check that the colorway is correctly applied
    expected_colorway = [
        "#1A9D49",
        "#075745",
        "#1D9DE2",
        "#0F2080",
        "#C78800",
        "#471F00",
        "#C775A7",
        "#A3136C",
        "#909090",
    ]
    assert (
        template.layout.colorway == expected_colorway
    ), "Colorway should match the expected colors"

    # Check that the table's header background color is correct
    assert (
        template.data["table"][0].header.fill.color == "#66FCF1"
    ), "Table header background color should be '#66FCF1'"

    # Check that the table's alternating cell fill colors are correct
    assert template.data["table"][0].cells.fill.color == [
        ["#F2F2F2", "#ECFEED"] * 5
    ], "Table cell fill color should alternate '#F2F2F2' and '#ECFEED'"
