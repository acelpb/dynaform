import plotly.graph_objs as go
from django.utils.text import slugify
from plotly.offline import plot


def piechart(data, labels, title=None):
    layout = go.Layout(
        autosize=True,
        margin=dict(
            l=65,
            r=50,
            b=65
        ),
        title=title
    )
    fig = go.Figure(data=go.Pie(labels=labels, values=data),
                    layout=layout)
    return plot(fig, output_type='div', filename=slugify(title), include_plotlyjs=False)


def barchart(data, labels, title=None):
    layout = go.Layout(
        autosize=True,
        margin=dict(
            l=65,
            r=50,
            b=65,
        ),
        title=title
    )
    fig = go.Figure(data=go.Bar(x=labels, y=data), layout=layout)

    return plot(fig, output_type='div', filename=slugify(title), include_plotlyjs=False)


def horizontal_barchart(data, labels, title=None):
    layout = go.Layout(
        autosize=True,
        margin=dict(
            l=65,
            r=50,
            b=65,
        ),
        title=title
    )

    fig = go.Figure(
        data=[
            go.Bar(name=n, x=d, y=labels, orientation='h', )
            for n, d in data
        ],
        layout=layout,
    )
    return plot(fig, output_type='div', filename=slugify(title), include_plotlyjs=False)
