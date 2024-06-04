from typing import Any

import pandas as pd
import seaborn as sns
from IPython.display import HTML


def display_process(outputs: list[str]) -> HTML:
    """Display process as html."""
    html_content = """
        <style>
            .output-box {{
                padding: 10px;
                margin: 5px;
                border: 1px solid black;
                display: inline-block;
                background-color: #f9f9f9;
            }}
            .arrow {{
                display: inline-block;
                margin: 0 20px;
                width: 40px;
                height: 20px;
                background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="40" height="20"><path d="M 0,10 L 30,10 M 30,10 L 20,0 M 30,10 L 20,20" fill="none" stroke="black"/></svg>');
                background-repeat: no-repeat;
                background-position: center;
            }}
        </style>
        """

    output_boxes = [f"""<div class="output-box">{output}</div>""" for output in outputs]
    return HTML(html_content + '<div class="arrow"></div>'.join(output_boxes))


def multi_boxplot(df: pd.DataFrame, var_name: str, cols: list[str] | str = None, ax=None, **kwargs):
    """Create a multi boxplot."""
    if cols is not None and not isinstance(cols, list):
        cols = [cols]

    if cols is None:
        cols = df.columns

    return sns.boxplot(data=_prep_df(df, cols, var_name), ax=ax, y="value", hue=var_name, **kwargs)


def multi_histplot(
    df: pd.DataFrame, var_name: str, cols: list[str] | str = None, ax: Any = None, **kwargs
):
    """Create a multi histplot."""
    if cols is not None and not isinstance(cols, list):
        cols = [cols]

    if cols is None:
        cols = df.columns

    return sns.histplot(data=_prep_df(df, cols, var_name), ax=ax, x="value", hue=var_name, **kwargs)


def pareto_plot(
    df: pd.DataFrame, cat_column: str, value_column: str, topk=20, ax=None, palette="viridis"
):
    """Create a pareto plot."""
    df = df.copy()
    # Sort the DataFrame by Value in descending order
    df = df.sort_values(value_column, ascending=False)

    # Calculate the cumulative percentage
    df["cumulative_percent"] = df[value_column].cumsum() / df[value_column].sum() * 100

    df = df.iloc[:topk]

    # Create the bar plot
    bar_plot = sns.barplot(x=cat_column, y=value_column, data=df, alpha=0.8, ax=ax, palette=palette)

    # Get the axis of the bar plot
    ax = bar_plot.axes

    # Plot the cumulative percentage as a line plot on the secondary y-axis
    ax2 = ax.twinx()
    sns.lineplot(
        x=cat_column,
        y="cumulative_percent",
        data=df,
        sort=False,
        marker="o",
        color="grey",
        alpha=0.4,
        ax=ax2,
    )

    # Labeling the axis
    ax.set_ylabel("Value")
    ax2.set_ylabel("Cumulative Percentage")

    return ax


def _prep_df(df: pd.DataFrame, cols: list, var_name) -> pd.DataFrame:
    return pd.melt(df[cols], var_name=var_name, value_name="value")
