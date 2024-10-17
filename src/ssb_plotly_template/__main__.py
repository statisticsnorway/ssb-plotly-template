"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Plotly template SSB design."""


if __name__ == "__main__":
    main(prog_name="ssb-plotly-template")  # pragma: no cover
