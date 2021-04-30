#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:39:04 2021

@author: kevin
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:24:44 2021

@author: kevin
"""


import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go



# Set templates
# fig.update_layout(template="plotly_white")

# fig.show()


df1 = pd.read_csv('menu.csv')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app: Dash = dash.Dash(__name__)
server = app.server

fig2 = px.bar(df1, x = "Calories" , y="Item",color_discrete_sequence =['red']*len(df1))
fig2.update_xaxes( showticklabels=False, color = "Yellow", tickangle = 180)


             
app.layout = html.Div([
    dcc.Markdown("Individual Project : Data Science | Kevin Puthota",style ={"text-align": "left",'fontSize': 15 ,'color': 'blue'}),
       html.H2("McDonald's' Nutritional Analysis:  ", style={'text-align': 'center','color': 'Gold', 'fontSize': 44,"font-family" :" Mclawsuit","text-shadow" : "2px 2px red" }),
        html.H2("Why this dashboard?:  ", style={'text-align': 'left', 'fontSize': 23,'color': 'rgb(0,59,115' }),
         html.H4("The dashboard shows the different nutritional values for all the items available at the popular food chain : ", style ={'fontSize': 20,'color': 'rgb(199,80,82'}),
    dcc.Markdown("""
                     - An average person would not go to a Mcdonalds if he/she plans to diet.
                     - During emergencies or unforeseeable situatons, one may be forced to buy here.
                     - This dashboard will help you choose the best option of all the items available and also recommend you to choose the best one!
                     - Choose the Category and the nutritional value you would love to see.
                     We hope you are lovin 'it'!"""
                
                 ),
    
        
        html.H3("Select a Category : ",style ={'fontSize': 21,'color':'rgb(199,80,82'}),
        dcc.Dropdown(
        id="select_category",
        options=[
            {'label': 'Breakfast', 'value': 'Breakfast'},
            {'label': 'Salads', 'value': 'Salads'},
            {'label': 'Snack & Sides', 'value': 'Snacks & Sides'},
            {'label': 'Beef & Pork', 'value': 'Beef & Pork'},
            {'label': 'Fish', 'value': 'Fish'}
        ],
        value='Breakfast',
        multi=False,
        placeholder="Select a Category",
        style={'width': "50%"}
    ),
         html.H3("Select a Nutritional Value : ",style ={'fontSize': 21,'color':'rgb(199,80,82'}),
        dcc.RadioItems(
        id="new_id",    
        options=[
         {'label': 'Fat ', 'value': 'Total Fat'},
        {'label':  'Sugars ', 'value': 'Sugars'},
        {'label': ' Calories ', 'value': 'Calories'},
        {'label': ' Protein ', 'value': 'Protein'},
        {'label': ' Carbs ', 'value': 'Carbohydrates'},
        {'label': ' Cholestrol ', 'value': 'Cholestrol'},
        ],
        value='Calories',
        labelStyle={'display': 'inline-block'},
        style={'display': 'inline-block',"background-color" : "Gold"}),
    # html
    html.Br(),
    html.Br(),
    html.Div(id='bar-container'),
    html.Div(id='choromap-container'),

    html.Div(id='output', children=[]),
    #html.Br(),
    dcc.Graph(id='kcrp', figure=fig2),
  
  
    
    
     
     
     # dcc.Graph(figure=fig2),
     html.H1("Selection Results",style ={'fontSize': 30,'color': 'black'}),
     # html.A("Any comparisons of crime among different locales should take into consideration relevant factors in addition to the area’s crime statistics. UCR Statistics: Their Proper Use provides more details concerning the proper use of UCR statistics."),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in df1[df1["Category"]=="Breakfast"].columns],
        data=df1[df1["Category"]=="Breakfast"].to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender"),
        filter_action="native",
        sort_action="native",
        sort_mode="single",
    )
                 
   ])
@app.callback(
    [Output(component_id='output', component_property='children'),
     Output(component_id='kcrp', component_property='figure'),
     Output('table','data')],
    [Input(component_id="select_category", component_property='value'),
     Input(component_id='new_id', component_property='value')]
)
def update_page(option_slctd,new_id):
    print(option_slctd)
    print(type(option_slctd))

    container = "The Category chosen by user was: {}".format(option_slctd)
    dff = df1.copy()
    dff = dff[dff["Category"] == option_slctd]
    fig2 = px.bar(dff, x = "Item" , y=new_id)
    #fig2.update_xaxes( showticklabels=False)
    data=dff[dff["Category"]==option_slctd].to_dict('records')
    
    
    return container, fig2, data


    

if __name__ == '__main__':
    app.run_server(debug=False)
        
    
    
