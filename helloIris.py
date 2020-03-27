import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
app = dash.Dash()

header_names = [
    'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
]

df = pd.read_csv('data/iris.data', names=header_names)
g = dcc.Graph(id='Iris Viz',
              figure={
                  'data': [
                      go.Scatter(x=df[df['class'] == i]['petal_length'],
                                 y=df[df['class'] == i]['sepal_length'],
                                 mode='markers',
                                 opacity=0.7,
                                 marker={
                                     'size': 15,
                                     'line': {
                                         'width': 0.5,
                                         'color': 'white'
                                     }
                                 },
                                 name=i) for i in df['class'].unique()
                  ],
                  'layout':
                  go.Layout(xaxis={'title': 'Petal Length'},
                            yaxis={'title': 'Sepal Length'},
                            margin={
                                'l': 200,
                                'b': 40,
                                't': 100,
                                'r': 200
                            },
                            legend={
                                'x': 0,
                                'y': 1
                            },
                            hovermode='closest')
              })

app.layout = html.Div(children=[
    html.H1(children='Iris visualization'),
    html.Div(
        '''        This was Built with Dash: A web application framework for Python.    '''
    ), g
])

if __name__ == '__main__':
    app.run_server(debug=True)
