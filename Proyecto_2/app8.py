import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from scipy import cluster
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from scipy.stats import kruskal
import prince
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import dataprep.eda as dp
#import matplotlib.pyplot as plt
#import seaborn as sns
#import scipy.stats as ss
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import interact, Layout
import ipywidgets as widgets

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D
import json

#from plotly.subplots import make_subplots

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
#-----------------------------------------------------------
#estilos

BODY_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "96rem",
    "padding": "4rem 19rem", #Organiza la letra
    "background-color": "#FDFEFE",  #"#1A5276",
    "text-color": "white"
}
CUERPO_STYLE = {
    "text-align": "center"
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "4rem 1rem",
    "background-color": '#72D9FB', #"#000000",  
    "text-color": "#EBF1F3",
    "text-align": "center"
}

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
#-----------------------------------------------------------
#Lectura de dataframe
df = pd.read_excel('dff2.xlsx')
df1 = pd.read_excel('BaseLoc.xlsx')
indic = pd.read_excel('indic.xlsx')
basec = pd.read_excel('basec.xlsx')
with open('ColombianRegionBA.geojson') as json_file:
    ColombiaRegion = json.load(json_file)
basec1 = pd.read_excel('basec.xlsx')
#-----------------------------------------------------------

#-----------------------------------------------------------
#COnstruccion de vistas

sidebar = html.Div(
    [
        html.H2("Universidad Central", className="display-8"),
        html.Hr(),
        html.P(
            "Maestria de Analitica de Datos", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Exploración", href="/", active="exact"),
                dbc.NavLink("Indicadores", href="/page-1", active="exact"),
                dbc.NavLink("Agrupación", href="/page-2", active="exact"),
                dbc.NavLink("k-means", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        
        html.Footer(
            "Miryam Leguizamón López"),
        html.Footer(
            "Juan Guillermo Forero Neme"
        ),
    ],
    style=SIDEBAR_STYLE,
)

#-----------------------------------------------------------
navbar = dbc.NavbarSimple(
    children=[
            dbc.Row(
                [
                dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                dbc.Col(dbc.NavbarBrand("Power by Plotly", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            #href="https://plot.ly",
        #),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)
# -----------------------------------------------------------

content = html.Div(id="page-content", children=[], style=BODY_STYLE)

#-----------------------------------------------------------
#Construccion de la vista web
app.layout = html.Div([
    dcc.Location(id="url"),
    content,
    sidebar,
    navbar
])

# -----------------------------------------------------------
#Procedimientos interactivos

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H4("Indicadores SECOP", className="display-10"),
                html.H2("                                        "),
                dbc.Row([
                    dbc.Col(dbc.Card(card1, color='white')),
                ]),
                html.H2("                                        "),
                dbc.Row(
                [
                    dbc.Col(dbc.Card(graph_card1)),
                    dbc.Col(dbc.Card(graph_card)),
                ],
                className="mb-4",
                ),
                                
        ]
    elif pathname == "/page-1":
        return [
            html.H2("Indicadores SECOP", className="display-10"),
                dbc.Row(
                    [
                    dbc.Col(dbc.CardDeck([card2] , style={"height": "330px"})),
                    dbc.Col(dbc.CardDeck([card3] , style={"height": "330px"})),                   
                    dbc.Col(dbc.CardDeck([card4] , style={"height": "330px"})),        
                        ]),
                html.H2("                                        "),
                dbc.Row([
                    dbc.Col(dbc.CardDeck([graph_Mapa], style={"height": "550px"})),
                    #dbc.Col(dbc.CardDeck([card2] , style={"height": "550px"})),
                    ]),
        ]
    # If the user tries to reach a different page, return a 404 message
    elif pathname == "/page-2":
        return [
        html.H4("Indicadores SECOP", className="display-10"),
        dbc.Row(
        [
            dbc.Col(dbc.CardDeck([card5] , style={"height": "350px"})),
            dbc.Col(dbc.CardDeck([graph_card_heatmap] , style={"height": "350px"})),
            
                    
                ],
               #width=5,
                #className="mb-4",
            ),          
        html.H2("                                        "),
        dbc.Row([
            dbc.Col([dbc.CardDeck([graph_card_agrup], style={"height": "200px"})]),
            #dbc.Col(dbc.CardDeck([graph_card_heatmap] , style={"height": "550px"})),
            ]),

            
        ]
    elif pathname == "/page-3":
        return [
        html.H4("Indicadores SECOP", className="display-10"),
        dbc.Row([
            dbc.Col([dbc.CardDeck([graph_card_kmeans], style={"height": "300px"})]),
            dbc.Col(dbc.CardDeck([graph_card_kmeans2] , style={"height": "100px"})),
            ]),

            
        ]
 #---------------------------------------------------------
@app.callback(  
    Output(component_id='exploratorio', component_property='figure'),
    Input(component_id='slct_depto', component_property='value'),
    Input(component_id='slct_option', component_property='value')
)
def distrib(slct_depto, slct_option):
    dfs = df.copy()
    dfs = dfs.fillna(0)
    dfs1 = dfs[dfs['Departamento'] == slct_depto]
    Freq=dfs1[slct_option].value_counts()
    if len(dfs1[slct_option].unique())<10:
        fig1 = go.Figure(data=[go.Pie(labels=list(Freq.index), values=Freq.values,hole=0.3,title=slct_option)])
        return fig1
    else:
        fig1 = go.Figure(data=[go.Table(
            columnwidth = [500,100,100],
            header=dict(values=['Categoría','Cantidad','Porcentaje'],
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[Freq.index, Freq.values,["{:.2%}".format(i) for i in Freq.values/len(dfs)]],
                       fill_color='lavender',
                       align='left'))
                             ])
        return fig1

@app.callback(  
    Output(component_id='boxplot', component_property='figure'),
    Input(component_id='slct_valor', component_property='value')
)
def boxplot1(slct_valor):
    ncontracts=df[df['Valor del Contrato']<slct_valor]
    fig4 = px.box(ncontracts, x = 'Departamento', y = 'Valor del Contrato')
    fig4.show()
    return fig4



@app.callback(  
    Output(component_id='scatterfig', component_property='figure'),
    Input(component_id='slct_axisX', component_property='value'),
    Input(component_id='slct_axisY', component_property='value')
)
def scatterfig(slct_axisX, slct_axisY):
    labels = kmeans.predict(X)
    C = kmeans.cluster_centers_
    colores=['red','green','blue']
    asignar=[]
    for row in labels:
        asignar.append(colores[row])
    f1 = basec[slct_axisX].values
    f2 = basec[slct_axisY].values 
    fig40 = go.Figure(data=go.Scattergl(
        x = f1,
        y = f2,
        mode='markers',
        marker=dict(
            color=asignar,
            colorscale='Viridis',
            line_width=1
        )
    ))
    return fig40


# -----------------------------------------------------------
card1 = dbc.Card([dbc.CardHeader("¿Que es el Secop"), 
dbc.CardBody(
    "El (SECOP) también denominado Servicio Electrónico de Contratación Pública por sus siglas en español, es un sistema que permite "
    "a las entidades estatales cumplir con las obligaciones de publicidad de los diferentes actos expedidos en los procesos contractuales "
    "y permite a los interesados en participar en los procesos de contratación, proponentes, veedurías y a la ciudadanía en general, consultar "
    "el estado de los mismos."
)])
#Page-1
card2 = dbc.Card([dbc.CardHeader("Total de inversión por mil personas"), 
dbc.CardBody("Este indicador permite conocer la inversión territorial de cada departamento por cada mil personas. Permite estandarizar la inversión de acuerdo con "
"la población de cada departemento, lo que hace que la inversión sea analizada de manera objetiva")])
card3 = dbc.Card([dbc.CardHeader("Inversión de la rama ejecutiva por cada mil personas"), 
dbc.CardBody("Este indicador permite conocer la inversión territorial de cada departamento por cada mil personas de la rama ejecutiva. Permite estandarizar la inversión "
"de acuerdo con la población de cada departemento, lo que hace que la inversión sea analizada de manera objetiva.")])
card4 = dbc.Card([dbc.CardHeader("Duración promedio de los contratos"), 
dbc.CardBody("Este es una característica de los contratos, que permite identificar el tiempo medio en días de los contratos terminados y analizar con más detalle las "
"inversiones y las diferencias de los mismos por cada departamento")])
card5 = dbc.Card([dbc.CardHeader("Costo mínimo de contratos día"), dbc.CardBody("Esta caracacterística de los contratos permite conocer el costo mínimo por dia que tienen "
"los contratos de cada departamento. Este indicador analizado y comparado en cada departamento puede dar idea de valore atipicos o raros en cada departamento.")])
#Page-2
card6 = dbc.Card([dbc.CardHeader("Prueba6"), dbc.CardBody("esto es un cajon")])
card7 = dbc.Card([dbc.CardHeader("Prueba7"), dbc.CardBody("esto es un cajon")])
card8 = dbc.Card([dbc.CardHeader("Prueba8"), dbc.CardBody("esto es un cajon")])
card9 = dbc.Card([dbc.CardHeader("Prueba9"), dbc.CardBody("esto es un cajon")])

#-----------------------------------------------------------
card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]


graph_card1 = dbc.Card(
    [dbc.CardHeader("Descriptivo"), 
    html.Div([
                    html.Label('Seleccione una columna:'),                     
                    dcc.Dropdown(
                        id='slct_option',
                        options=[
                            {'label':'Anno BPIN','value':'Anno BPIN'},
                            {'label':'Ciudad','value':'Ciudad'},
                            {'label':'Código BPIN','value':'Código BPIN'},
                            {'label':'Codigo de Categoria Principal','value':'Codigo de Categoria Principal'},
                            {'label':'Codigo Entidad','value':'Codigo Entidad'},
                            {'label':'Condiciones de Entrega','value':'Condiciones de Entrega'},
                            #{'label':'Departamento','value':'Departamento'},
                            {'label':'Descripcion del Proceso','value':'Descripcion del Proceso'},
                            {'label':'Destino Gasto','value':'Destino Gasto'},
                            {'label':'Dias Adicionados','value':'Dias Adicionados'},
                            {'label':'Documento Proveedor','value':'Documento Proveedor'},
                            {'label':'Entidad Centralizada','value':'Entidad Centralizada'},
                            {'label':'Es Grupo','value':'Es Grupo'},
                            {'label':'Es Pyme','value':'Es Pyme'},
                            {'label':'EsPostConflicto','value':'EsPostConflicto'},
                            {'label':'Estado BPIN','value':'Estado BPIN'},
                            {'label':'Estado Contrato','value':'Estado Contrato'},
                            {'label':'Fecha de Fin de Ejecucion','value':'Fecha de Fin de Ejecucion'},
                            {'label':'Fecha de Fin del Contrato','value':'Fecha de Fin del Contrato'},
                            {'label':'Fecha de Firma','value':'Fecha de Firma'},
                            {'label':'Fecha de Inicio de Ejecucion','value':'Fecha de Inicio de Ejecucion'},
                            {'label':'Fecha de Inicio del Contrato','value':'Fecha de Inicio del Contrato'},
                            {'label':'Género Representante Legal','value':'Género Representante Legal'},
                            {'label':'Gobernaciones y Resguardos Indígenas)','value':'Gobernaciones y Resguardos Indígenas)'},
                            {'label':'Habilita Pago Adelantado','value':'Habilita Pago Adelantado'},
                            {'label':'ID Contrato','value':'ID Contrato'},
                            {'label':'Identificación Representante Legal','value':'Identificación Representante Legal'},
                            {'label':'Justificacion Modalidad de Contratacion','value':'Justificacion Modalidad de Contratacion'},
                            {'label':'Localización','value':'Localización'},
                            {'label':'Modalidad de Contratacion','value':'Modalidad de Contratacion'},
                            {'label':'Nacionalidad Representante Legal','value':'Nacionalidad Representante Legal'},
                            {'label':'Nit Entidad','value':'Nit Entidad'},
                            {'label':'Nombre Entidad','value':'Nombre Entidad'},
                            {'label':'Nombre Representante Legal','value':'Nombre Representante Legal'},
                            {'label':'Obligación Ambiental','value':'Obligación Ambiental'},
                            {'label':'Obligaciones Postconsumo','value':'Obligaciones Postconsumo'},
                            {'label':'Orden','value':'Orden'},
                            {'label':'Origen de los Recursos','value':'Origen de los Recursos'},
                            {'label':'Pilares del Acuerdo','value':'Pilares del Acuerdo'},
                            {'label':'Presupuesto General de la Nacion – PGN','value':'Presupuesto General de la Nacion – PGN'},
                            {'label':'Proceso de Compra','value':'Proceso de Compra'},
                            {'label':'Proveedor Adjudicado','value':'Proveedor Adjudicado'},
                            {'label':'Puntos del Acuerdo','value':'Puntos del Acuerdo'},
                            {'label':'Rama','value':'Rama'},
                            {'label':'Recursos de Credito','value':'Recursos de Credito'},
                            {'label':'Recursos Propios','value':'Recursos Propios'},
                            {'label':'Recursos Propios (Alcaldías','value':'Recursos Propios (Alcaldías'},
                            {'label':'Referencia del Contrato','value':'Referencia del Contrato'},
                            {'label':'Reversion','value':'Reversion'},
                            {'label':'Saldo CDP','value':'Saldo CDP'},
                            {'label':'Saldo Vigencia','value':'Saldo Vigencia'},
                            {'label':'Sector','value':'Sector'},
                            {'label':'Sistema General de Participaciones','value':'Sistema General de Participaciones'},
                            {'label':'Sistema General de Regalías','value':'Sistema General de Regalías'},
                            {'label':'Tipo de Contrato','value':'Tipo de Contrato'},
                            {'label':'Tipo de Identificación Representante Legal','value':'Tipo de Identificación Representante Legal'},
                            {'label':'TipoDocProveedor','value':'TipoDocProveedor'},
                            {'label':'URLProceso','value':'URLProceso'},
                            {'label':'Valor Amortizado','value':'Valor Amortizado'},
                            {'label':'Valor de pago adelantado','value':'Valor de pago adelantado'},
                            {'label':'Valor del Contrato','value':'Valor del Contrato'},
                            {'label':'Valor Facturado','value':'Valor Facturado'},
                            {'label':'Valor Pagado','value':'Valor Pagado'},
                            {'label':'Valor Pendiente de Amortizacion','value':'Valor Pendiente de Amortizacion'},
                            {'label':'Valor Pendiente de Ejecucion','value':'Valor Pendiente de Ejecucion'},
                            {'label':'Valor Pendiente de Pago','value':'Valor Pendiente de Pago'}
                            ],
                        value='Rama',
                        #style={'width': '80%', 'float': 'right', 'display': 'inline-block'}
                        ),
                ]),    
                html.Div([
                    html.Br(),
                    html.Label('Seleccione un Departamento:'),   
                    dcc.Dropdown(
                        id='slct_depto',
                        options=[
                            {'label':'Amazonas','value':'Amazonas'},
                            {'label':'Antioquia','value':'Antioquia'},
                            {'label':'Arauca','value':'Arauca'},
                            {'label':'Atlántico','value':'Atlántico'},
                            {'label':'Bolívar','value':'Bolívar'},
                            {'label':'Boyacá','value':'Boyacá'},
                            {'label':'Caldas','value':'Caldas'},
                            {'label':'Caquetá','value':'Caquetá'},
                            {'label':'Casanare','value':'Casanare'},
                            {'label':'Cauca','value':'Cauca'},
                            {'label':'Cesar','value':'Cesar'},
                            {'label':'Chocó','value':'Chocó'},
                            {'label':'Córdoba','value':'Córdoba'},
                            {'label':'Cundinamarca','value':'Cundinamarca'},
                            {'label':'Distrito Capital de Bogotá','value':'Distrito Capital de Bogotá'},
                            {'label':'Guainía','value':'Guainía'},
                            {'label':'Guaviare','value':'Guaviare'},
                            {'label':'Huila','value':'Huila'},
                            {'label':'Magdalena','value':'Magdalena'},
                            {'label':'Meta','value':'Meta'},
                            {'label':'Nariño','value':'Nariño'},
                            {'label':'Norte de Santander','value':'Norte de Santander'},
                            {'label':'Putumayo','value':'Putumayo'},
                            {'label':'Santander','value':'Santander'},
                            {'label':'Sucre','value':'Sucre'},
                            {'label':'Tolima','value':'Tolima'},
                            {'label':'Valle del Cauca','value':'Valle del Cauca'},
                            {'label':'Vaupés','value':'Vaupés'},
                            {'label':'Vichada','value':'Vichada'}
                            ],
                            value='Distrito Capital de Bogotá',
                            #style={'width': '80%', 'float': 'right', 'display': 'inline-block'}
                        ),
                ]),    
                    dcc.Graph(id='exploratorio', figure={}),
        
        
    ]
)

ncontracts=df[df['Valor del Contrato']<215000000]
graph_card = dbc.Card(
    [dbc.CardHeader("Atipicos"), 
    html.Label('Seleccione un monto de contrato:'),                     
                    dcc.Dropdown(
                        id='slct_valor',
                        options=[
                            {'label':'215000000','value':215000000}
                            ],
                        value=215000000
                    ),
    dbc.CardBody([
        dcc.Graph(id='boxplot', figure={}),
        
        ])
    ]
)
# -----------------------------------------------------------
basec=df1[['Departamento','ind1', 'ind2', 'duracion', 'ind4_x', 'ind4_y', 'ind4']]
basec
indic= basec.select_dtypes(exclude=['object'])
escala=StandardScaler(with_mean=True, with_std=True)
escala.fit(indic)
datosestan=escala.transform(indic)
pca=PCA(0.99)
pca.fit(datosestan)  ## Ajusto el PCA (valores, vectpores, varianza)
nuevosACP=pca.transform(datosestan)
pca.explained_variance_ratio_  ## Como el ACP es tan malo, se podria trabajar con los estandarizados
pca=PCA(0.99)
pca.fit(datosestan)  ## Ajusto el PCA (valores, vectpores, varianza)
nuevosACP=pca.transform(datosestan)
pca.explained_variance_ratio_  ## Como el ACP es tan malo, se podria trabajar con los estandarizados
def agnes_coef(bas,metodo,metrica):
    '''
    Función que permite determinar el coeficiente de aglomeración entre varias métricas y métodos
    Datos de entrada:
        Obligatorios:
            base: se recomienda la base ya normalizada y que solo contenga variables cuantitativas.
            método: contiene la lista de métodos que se usara a comparar.
            métrica: contiene la lista de las métricas que se usara para comparar
    Datos de salida:
        devolverá un Dataframe que contendrá el cálculo de cada coeficiente de aglomeración, donde los métodos son 
        las columnas y las métricas los índices. Dado el caso que el resultado sea -1 es que la combinación entre 
        métrica y método genera error.
    '''
    bas=pd.DataFrame(bas)
    bas_resul=pd.DataFrame(columns=metrica,index=metodo)
    for i in range(len(metodo)):
        for j in range(len(metrica)):
            try:
                enla=sch.linkage(bas, method=metodo[i], metric=metrica[j])
                enlas=pd.DataFrame(enla)
                a1=enlas[enlas[0].isin(bas.index)]
                b1=enlas[enlas[1].isin(bas.index)]
                resul=sum(max(enlas[2])-pd.concat([a1,b1],axis=0)[2])/(max(enlas[2])*bas.shape[0])
                bas_resul.iloc[i,j]=resul
            except ValueError:
                bas_resul.iloc[i,j]=-1
            
    return bas_resul
agnes_coef(nuevosACP,["ward","complete","single", "average","centroid", "median"],
           ["braycurtis", "canberra", "chebyshev", 
          "cityblock", "correlation", "cosine", "euclidean", "jensenshannon", "mahalanobis"])
#plt.rcParams["figure.figsize"] = (20,10)
fig10 = ff.create_dendrogram(nuevosACP)
fig10.show()
dendograma = dcc.Graph(id='dend_1', figure = fig10, style={
            'border': 'thin lightgrey solid', 
            'overflowY': 'scroll',
            'height': '275px'})
graph_card_agrup = dbc.Card(
    [dbc.CardHeader("Dendograma"), 

    dbc.CardBody([
        dcc.Graph(id='dend_1', figure = fig10, style={"height": "550px"}),
        
        ])
    ]
)
# -----------------------------------------------------------
dff = df1.copy()
fig50 = px.scatter_mapbox(dff, lat="Latitud", lon="Longitud", color= 'Departamento', hover_name='Departamento', hover_data=['Departamento', 'Valor del Contrato_x', 'ind1', 'ind2', 'duracion'],
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=4, height=700, size= 'Poblacion 2020')
fig50.update_layout(mapbox_style="open-street-map", showlegend=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig50.show()
graph_Mapa = dbc.Card(
    [dbc.CardHeader("Indicadores"), 

    dbc.CardBody([
        dcc.Graph(id='mapa', figure = fig50),
        
        ])
    ]
)
# -----------------------------------------------------------
X = np.array(basec[["ind1","duracion","ind4_x","ind4_y","ind4"]])
y = np.array(basec['Departamento'])
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score
fig30 = px.line(score)

kmeans = KMeans(n_clusters=3).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

labels = kmeans.predict(X)
C = kmeans.cluster_centers_
# -----------------------------------------------------------

fig60 = px.choropleth_mapbox(basec1, geojson=ColombiaRegion, color="Grupo",
                            opacity=1,
                            locations="Departamento", featureidkey="properties.NOMBRE_DPT",
                            center={"lat": 4.089722, "lon":  -72.961944},
                            mapbox_style="carto-darkmatter",  zoom=3.5,
                            width=400,
                            height=600
                            )
fig60.update_xaxes(fixedrange=True)
#fig60.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, showlegend=False)
fig60.update_layout(mapbox_style="open-street-map", showlegend=False)
graph_card_kmeans = dbc.Card(
    [dbc.CardHeader("k-means"), 

    dbc.CardBody([
        dcc.Graph(id='kmeans_1', figure = fig60, style={"height":600}),
        
        ])
    ]
)
# -----------------------------------------------------------
graph_card_kmeans2 = dbc.Card(
    [dbc.CardHeader("k-means"), 

    dbc.CardBody([
        html.Label('Seleccione en eje X:'),   
                    dcc.Dropdown(
                        id='slct_axisX',
                        options=[
                            {'label':'Indicador 1','value':'ind1'},
                            {'label':'Indicador 2','value':'ind2'},
                            {'label':'Indicador 3','value':'ind4_y'},
                            {'label':'Duracion','value':'duracion'}
                            ],
                            value='ind1',
                            #style={'width': '80%', 'float': 'right', 'display': 'inline-block'}
                        ),
        html.Label('Seleccione en eje Y:'),   
                    dcc.Dropdown(
                        id='slct_axisY',
                        options=[
                            {'label':'Indicador 1','value':'ind1'},
                            {'label':'Indicador 2','value':'ind2'},
                            {'label':'Indicador 3','value':'ind4_y'},
                            {'label':'Duracion','value':'duracion'}
                            ],
                            value='ind2',
                            #style={'width': '80%', 'float': 'right', 'display': 'inline-block'}
                        ),
        dcc.Graph(id='scatterfig', figure = {}),
        
        ])
    ]
)

heat = basec.corr()
fig70 = px.imshow(heat, width=600, height=250)
fig70.update_layout(xaxis={"tickangle": 45}, )
fig70.show() 
graph_card_heatmap = dbc.Card(
    [dbc.CardHeader("heatmap"), 

    dbc.CardBody([
        dcc.Graph(id='heatmap_1', figure = fig70, style={"width":600, "height": 350}),
        
        ])
    ]
)
# -----------------------------------------------------------

if __name__=='__main__':
    app.run_server(debug=True, port=8000)