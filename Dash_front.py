import matplotlib
import dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from shift_reduce import *
from dash.dependencies import Input, Output,State,ALL

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#00022e',
    'text': '#7FDBFF'
}

grammar = []
string =""

app.layout = html.Div(style={'backgroundColor': colors['background'], 'height':'725px',},  children=[
    html.Br(),
    html.Br(),
    html.H1(children='Shift Reduce Parser',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),
    html.Div([

        html.Div(style= {'backgroundColor': '#82EEFD',
                             'height':'500px',
                             'margin-left': '2vw',
                             #'vertical-align':'centre',
                              'margin-top':'4vw',
                             #'textAlign': 'center',
                             'display': 'inline-block'
                             #'justifyContent':'center'
                             },
                 children = [
                     html.H4(children='',
                             style={
                                 'textAlign': 'center', 'color': '#00022e',
                             }
                             ),

                html.Div( children = [
                    html.P("Enter the grammar of the parser.",style={'color':'#0A1172'}),
                    html.Button("Add", id="add",n_clicks = 0,style={'colors':'#ffffff','BackgroundColor':'black','display':'block'}),
                    html.Div(id='dropdown-container', children=[]),
                    html.Br(),
                    html.Div(id='dropdown-container-output', children=['Enter a value and press submit'],style={'color':'#0A1172'}),

                    ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '8vw', 'margin-top': '5vw'},className='three columns'),


                    #string input
                    html.Div(children=[
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.P(id='text-2',
                               children='Enter the input string '),
                        html.Div([dcc.Input(id='input', type='text',placeholder='Enter your String'),
                                  html.Button(id='submit-button',n_clicks=0,children='Submit'),
                                  html.Div(id='output'),
                                  html.Br()
                                  ])



                    ], style={'backgroundColor': '#82EEFD','display': 'inline-block', 'vertical-align': 'top', 'margin-left': '10vw', 'margin-top': '3vw'},className='three columns'),
                    html.Div(html.Br())
                    ],className='row'),



        # TABLE display (third column )
        html.Div([
            html.Br(),
            html.H4(children='Working of the Parser',
                    style={
                        'textAlign': 'center', 'color': '#FFFFFF',
                    }
                    ),
                html.Div(id="output_div", children=[
                ]),
        html.Div(html.Br())
        ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '10vw', 'margin-top': '1vw'}),

    ], className="row"),

])


@app.callback(
    Output('dropdown-container', 'children'),
    Input('add', 'n_clicks'),
    State('dropdown-container', 'children'))
def display_dropdowns(n_clicks, children):
    new_dropdown = html.Div([dcc.Input(id={'type':'text','index': n_clicks}, placeholder='initial value',  type='text', debounce = True),
                             html.Br()])
    children.append(new_dropdown)
    return children


@app.callback(
    Output('dropdown-container-output', 'children'),
    Input({'type': 'text', 'index': ALL}, 'value')
)
def display_output(values):
    if values:
        grammar.append(values)
    return html.Div([
        html.Div('{} ) {}'.format(i + 1, value))
        for (i, value) in enumerate(values)
    ])


@app.callback(Output('output_div', 'children'),
              Input('submit-button', 'n_clicks'),
              State('input', 'value'))
def update_output(n_clicks, input):
    input_string = input
    newlist = [x for x in grammar if x not in [[],[None]]]
    temp_grammar=newlist[-1]
    formatted_grammar=[]
    for i in temp_grammar:
        i1, i2= i.split("->")
        formatted_grammar.append([i1,i2])
    output_string, output_dictionary=parse(formatted_grammar,input_string)
    output_table=dash_table.DataTable(
                 id='table',
                 columns=[{"name": i, "id": i}
                          for i in output_dictionary.columns],
                 data=output_dictionary.to_dict('records'),
                 style_cell=dict(textAlign='center'),
                 style_header=dict(border='2px black solid', backgroundColor="paleturquoise", align="center", height=50),
                 style_data=dict(backgroundColor="white", align="center", border='2px black solid'),
            )
    return output_table, html.H3(children=output_string, style={ 'textAlign': 'center', 'color': '#FFFFFF',})


if __name__ == '__main__':
    app.run_server(debug=False)