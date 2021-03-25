import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64

# external CSS stylesheets
external_stylesheets = [
    'https://github.com/jgforeroneme/VisualizacionGr2/blob/main/Proyecto/styles.css',
        {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }

]

app = dash.Dash(__name__,                
                #external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

# ---------- Import and clean data (importing csv into pandas)

df = pd.read_excel("Df_Final.xlsx")

# ------------------------------------------------------------------------------

image_filename = 'imagen.jpg' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# App layout

colors = {
    #'background': '#140b34',
    'background': '#140B34',
    'text': '#E55C30',
    'text1': '#EAA928',#titulo
    'text2': '#F6D746' #explicacion
}
verticalcenter = {"display: table-cell", "height: 400px", "vertical-align: middle"}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='DATAFOLIO INDICADORES BANCO MUNDIAL',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.H2(children='Maestria en Analitica de Datos.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
########################
    html.Div(children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children='Regiones del mundo', style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'El banco Mundial es una organización multinacional especializada en finanzas y asistencia. Su propósito declarado es reducir la pobreza ' 
                            'mediante préstamos de bajo interés, créditos sin intereses a nivel bancario y apoyos económicos a las naciones en desarrollo.  '
                            'Con la intención de cumplir la misión de la entidad, el banco ha clasificado a los países en los cuales tiene presencia según las principales ' 
                            'características socioeconómicas con el fin de ofrecer servicios y soporte focalizado en las necesidades reales de cada área geográfica. ', 
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'De lo anterior podemos decir que el mundo esta dividido en las siguientes regiones que comparten entre si aspectos sociales, culturales y '
                            'económicos homogéneos entre sí, estas regiones son:',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Asia meridional,',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	África al sur del Sahara,',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Europa y Asia central,',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	América Latina y el Caribe,',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Asia oriental y el Pacífico,',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Oriente Medio y Norte de África.',
                            style={'textAlign': 'left', 'color': colors['text2']}),                        
                       
                    ])
    ),

########################
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    #height=500, width=300
    style={'height':'80%', 'text-align':'center', 'display':'inline-block'}
    ),
########################


    html.Div(children=html.Div(className='control-tab', children=[
                        html.H3(className='what-is', children='Población Mundial', style={'textAlign': 'left', 'color': colors['text1']}),
                        html.P(
                            'Al hablar de población mundial nos referimos al total de personas que habitan el mundo en un periodo de tiempo determinado, '
                            'las Naciones unidas considera como principales factores que influyen en el crecimiento de la población los siguientes elementos:'                        
                            , 
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Tasas de Fecundidad: En demografía, la tasa de fecundidad refiere a la relación existente entre el número de nacimientos '
                            'ocurridos en un periodo de tiempo determinado y la cantidad de personas en edad fértil en dicho periodo, para este caso se '
                            'considera a la población femenina entre los 15 y 49 años como personas en edad fértil.',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Aumento de la longevidad: Este elemento tiene que ver con la expectativa de vida que tiene una persona según el país '
                            'donde habite entendiendo que existe una relación entre las personas y el entorno en el cual conviven.'
                            'Es de anotar que en la mayor parte de países del mundo la expectativa de vida ha ido aumentando, esto tiene que ver con el '
                            'mejoramiento en los sistemas de salud locales, el acceso a tecnologías y la implementación de políticas sociales tenientes a '
                            'proteger a los menores ya la población de la tercera edad.',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' •	Migración Internacional: Ocurre cuando las personas cruzan las fronteras estatales y permanecen en el país de acogida durante '
                            'un periodo mínimo de tiempo, la migración se da en muchos casos por movimientos políticos, sociales y económicos.',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            ' A continuación, va a encontrar un mapa que nos presenta la dinámica de la población mundial desde el año 1960 hasta 2019:',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                    ])
    ),

########################    
#app.layout = html.Div([
    html.Label('Seleccione un año:', style={'color': colors['text1']}),
    dcc.Dropdown(id="slct_year",
                 options=[
                    {"label": "1960", "value": 1960},
                    {"label": "1961", "value": 1961},
                    {"label": "1962", "value": 1962},
                    {"label": "1963", "value": 1963},
                    {"label": "1964", "value": 1964},
                    {"label": "1965", "value": 1965},
                    {"label": "1966", "value": 1966},
                    {"label": "1967", "value": 1967},
                    {"label": "1968", "value": 1968},
                    {"label": "1969", "value": 1969},
                    {"label": "1970", "value": 1970},
                    {"label": "1971", "value": 1971},
                    {"label": "1972", "value": 1972},
                    {"label": "1973", "value": 1973},
                    {"label": "1974", "value": 1974},
                    {"label": "1975", "value": 1975},
                    {"label": "1976", "value": 1976},
                    {"label": "1977", "value": 1977},
                    {"label": "1978", "value": 1978},
                    {"label": "1979", "value": 1979},
                    {"label": "1980", "value": 1980},
                    {"label": "1981", "value": 1981},
                    {"label": "1982", "value": 1982},
                    {"label": "1983", "value": 1983},
                    {"label": "1984", "value": 1984},
                    {"label": "1985", "value": 1985},
                    {"label": "1986", "value": 1986},
                    {"label": "1987", "value": 1987},
                    {"label": "1988", "value": 1988},
                    {"label": "1989", "value": 1989},
                    {"label": "1990", "value": 1990},
                    {"label": "1991", "value": 1991},
                    {"label": "1992", "value": 1992},
                    {"label": "1993", "value": 1993},
                    {"label": "1994", "value": 1994},
                    {"label": "1995", "value": 1995},
                    {"label": "1996", "value": 1996},
                    {"label": "1997", "value": 1997},
                    {"label": "1998", "value": 1998},
                    {"label": "1999", "value": 1999},
                    {"label": "2000", "value": 2000},
                    {"label": "2001", "value": 2001},
                    {"label": "2002", "value": 2002},
                    {"label": "2003", "value": 2003},
                    {"label": "2004", "value": 2004},
                    {"label": "2005", "value": 2005},
                    {"label": "2006", "value": 2006},
                    {"label": "2007", "value": 2007},
                    {"label": "2008", "value": 2008},
                    {"label": "2009", "value": 2009},
                    {"label": "2010", "value": 2010},
                    {"label": "2011", "value": 2011},
                    {"label": "2012", "value": 2012},
                    {"label": "2013", "value": 2013},
                    {"label": "2014", "value": 2014},
                    {"label": "2015", "value": 2015},
                    {"label": "2016", "value": 2016},
                    {"label": "2017", "value": 2017},
                    {"label": "2018", "value": 2018},
                    {"label": "2019", "value": 2019}
                     ],
                 multi=False,
                 value=2019,
                 style={'width': "100%", 'align-items': 'center', 'justify-content': 'center'}
                 
                 ),


    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={}),

########################
    html.Div(children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children='Población Rural vs Población Urbana', style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'No existe un criterio común para todos los países del mundo que permitan clasificar un espacio rural y un espacio urbano, '
                            'la distinción tradicional entre zonas urbanas y rurales dentro de un país se ha basado en el supuesto de que las áreas urbanas, '
                            'sin importar como se definan, proveen un estilo de vida distinto y usualmente un estándar de vida más alto que las áreas rurales.', 
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'Sin embargo, los países con mayor grado de industrialización han planteado la idea de clasificar la población urbana y rural por el grado '
                            'de concentración de la población en las ciudades, esta idea es debatida por regiones en las cuales se habla de población urbana con estilos '
                            'de vida rural, por esta ocasión se incluyen variables como actividad económica de la región, infraestructura energética y de saneamiento básico, '
                            'acceso a servicios de salud y recreación entre otros.',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'Para fines nacionales, al igual que para comparabilidad internacional, la unidad de clasificación más utilizada es el tamaño de la localidad o, '
                            'si esto no es posible, la división administrativa más pequeña del país. ',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'Se debe reconocer, sin embargo, que la distinción entre urbano y rural basada únicamente en el tamaño de la población de las localidades no siempre '
                            'ofrece una base satisfactoria para la clasificación, especialmente en países altamente industrializados',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'A continuación, va a encontrar la comparativa por región de la composición de la población Urbana y Rural por país para el año 2019:',
                            style={'textAlign': 'left', 'color': colors['text2']}),

                    ])
    ),
#################################################################
    html.Label('Seleccione una Región:', style={'color': colors['text1']}),
    dcc.Dropdown(id="slct_region",
                 options=[
                    {"label": "South Asia", "value": "South Asia"},
                    {"label": "Europe & Central Asia", "value": "Europe & Central Asia"},
                    {"label": "Middle East & North Africa", "value": "Middle East & North Africa"},
                    {"label": "Sub-Saharan Africa", "value": "Sub-Saharan Africa"},
                    {"label": "Latin America & Caribbean", "value": "Latin America & Caribbean"},
                    {"label": "East Asia & Pacific", "value": "East Asia & Pacific"},
                    {"label": "North America", "value": "North America"}
                     ],
                 multi=False,
                 value="Latin America & Caribbean",
                 style={'width': "40%"}
                 ),
    html.Br(),

    dcc.Graph(id='graph1', figure={}),

########################
    html.Div(children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children='Población Rural vs Población Urbana en el tiempo', style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'La revolución Industrial trajo consigo como principal consecuencia la ruptura del modelo económico agrario pasando a constituir '
                            'un modelo económico industrializado, la nobleza pierde su antiguo rol de dominio político y social creándose entonces la burguesía '
                            'que es quien reclama el poder político y social en el siglo XVIII.', 
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'Al aparecer nuevas industrias, se produce un fenómeno de desplazamiento de personas de las zonas rurales buscando emplearse en las nuevas '
                            'industrias, esta situación conllevó a la creación de nuevos asentamientos Urbanos que son en muchos casos el origen de las ciudades modernas '
                            'que conocemos hoy en día.',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'El crecimiento de la población urbana en detrimento de la población rural tiene que ver mucho con el mejoramiento de las condiciones de vida que '
                            'encuentran as personas que deciden migrar del campo a la urbe, en la medida que los países del mundo logran crecer económicamente se observa un '
                            'aumento en el crecimiento de la población urbana.',
                            style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'A continuación, va a encontrar la evolución de la población rural vs población urbana por país, la gráfica se construye en términos porcentuales '
                            'comparando la cantidad de población urbana / total de población y población rural / total de población:',
                            style={'textAlign': 'left', 'color': colors['text2']}),

                    ])
    ),
#################################################################
    html.Label('Seleccione un Pais:', style={'color': colors['text1']}),
    dcc.Dropdown(id="slct_country",
                 options=[
                    {"label": "Australia", "value": "AUS"},
                    {"label": "Brunei Darussalam", "value": "BRN"},
                    {"label": "China", "value": "CHN"},
                    {"label": "Fiji", "value": "FJI"},
                    {"label": "Indonesia", "value": "IDN"},
                    {"label": "Japan", "value": "JPN"},
                    {"label": "Cambodia", "value": "KHM"},
                    {"label": "Korea, Rep.", "value": "KOR"},
                    {"label": "Lao PDR", "value": "LAO"},
                    {"label": "Myanmar", "value": "MMR"},
                    {"label": "Mongolia", "value": "MNG"},
                    {"label": "Malaysia", "value": "MYS"},
                    {"label": "New Caledonia", "value": "NCL"},
                    {"label": "New Zealand", "value": "NZL"},
                    {"label": "Philippines", "value": "PHL"},
                    {"label": "Papua New Guinea", "value": "PNG"},
                    {"label": "Korea, Dem. People’s Rep.", "value": "PRK"},
                    {"label": "Solomon Islands", "value": "SLB"},
                    {"label": "Thailand", "value": "THA"},
                    {"label": "Timor-Leste", "value": "TLS"},
                    {"label": "Vietnam", "value": "VNM"},
                    {"label": "Vanuatu", "value": "VUT"},
                    {"label": "Albania", "value": "ALB"},
                    {"label": "Armenia", "value": "ARM"},
                    {"label": "Austria", "value": "AUT"},
                    {"label": "Azerbaijan", "value": "AZE"},
                    {"label": "Belgium", "value": "BEL"},
                    {"label": "Bulgaria", "value": "BGR"},
                    {"label": "Bosnia and Herzegovina", "value": "BIH"},
                    {"label": "Belarus", "value": "BLR"},
                    {"label": "Switzerland", "value": "CHE"},
                    {"label": "Cyprus", "value": "CYP"},
                    {"label": "Czech Republic", "value": "CZE"},
                    {"label": "Germany", "value": "DEU"},
                    {"label": "Denmark", "value": "DNK"},
                    {"label": "Spain", "value": "ESP"},
                    {"label": "Estonia", "value": "EST"},
                    {"label": "Finland", "value": "FIN"},
                    {"label": "France", "value": "FRA"},
                    {"label": "United Kingdom", "value": "GBR"},
                    {"label": "Georgia", "value": "GEO"},
                    {"label": "Greece", "value": "GRC"},
                    {"label": "Greenland", "value": "GRL"},
                    {"label": "Croatia", "value": "HRV"},
                    {"label": "Hungary", "value": "HUN"},
                    {"label": "Ireland", "value": "IRL"},
                    {"label": "Iceland", "value": "ISL"},
                    {"label": "Italy", "value": "ITA"},
                    {"label": "Kazakhstan", "value": "KAZ"},
                    {"label": "Kyrgyz Republic", "value": "KGZ"},
                    {"label": "Lithuania", "value": "LTU"},
                    {"label": "Luxembourg", "value": "LUX"},
                    {"label": "Latvia", "value": "LVA"},
                    {"label": "Moldova", "value": "MDA"},
                    {"label": "North Macedonia", "value": "MKD"},
                    {"label": "Montenegro", "value": "MNE"},
                    {"label": "Netherlands", "value": "NLD"},
                    {"label": "Norway", "value": "NOR"},
                    {"label": "Poland", "value": "POL"},
                    {"label": "Portugal", "value": "PRT"},
                    {"label": "Romania", "value": "ROU"},
                    {"label": "Russian Federation", "value": "RUS"},
                    {"label": "Serbia", "value": "SRB"},
                    {"label": "Slovak Republic", "value": "SVK"},
                    {"label": "Slovenia", "value": "SVN"},
                    {"label": "Sweden", "value": "SWE"},
                    {"label": "Tajikistan", "value": "TJK"},
                    {"label": "Turkmenistan", "value": "TKM"},
                    {"label": "Turkey", "value": "TUR"},
                    {"label": "Ukraine", "value": "UKR"},
                    {"label": "Uzbekistan", "value": "UZB"},
                    {"label": "Argentina", "value": "ARG"},
                    {"label": "Bahamas, The", "value": "BHS"},
                    {"label": "Belize", "value": "BLZ"},
                    {"label": "Bolivia", "value": "BOL"},
                    {"label": "Brazil", "value": "BRA"},
                    {"label": "Chile", "value": "CHL"},
                    {"label": "Colombia", "value": "COL"},
                    {"label": "Costa Rica", "value": "CRI"},
                    {"label": "Cuba", "value": "CUB"},
                    {"label": "Dominican Republic", "value": "DOM"},
                    {"label": "Ecuador", "value": "ECU"},
                    {"label": "Guatemala", "value": "GTM"},
                    {"label": "Guyana", "value": "GUY"},
                    {"label": "Honduras", "value": "HND"},
                    {"label": "Haiti", "value": "HTI"},
                    {"label": "Jamaica", "value": "JAM"},
                    {"label": "Mexico", "value": "MEX"},
                    {"label": "Nicaragua", "value": "NIC"},
                    {"label": "Panama", "value": "PAN"},
                    {"label": "Peru", "value": "PER"},
                    {"label": "Puerto Rico", "value": "PRI"},
                    {"label": "Paraguay", "value": "PRY"},
                    {"label": "El Salvador", "value": "SLV"},
                    {"label": "Suriname", "value": "SUR"},
                    {"label": "Trinidad and Tobago", "value": "TTO"},
                    {"label": "Uruguay", "value": "URY"},
                    {"label": "Venezuela, RB", "value": "VEN"},
                    {"label": "United Arab Emirates", "value": "ARE"},
                    {"label": "Djibouti", "value": "DJI"},
                    {"label": "Algeria", "value": "DZA"},
                    {"label": "Egypt, Arab Rep.", "value": "EGY"},
                    {"label": "Iran, Islamic Rep.", "value": "IRN"},
                    {"label": "Iraq", "value": "IRQ"},
                    {"label": "Israel", "value": "ISR"},
                    {"label": "Jordan", "value": "JOR"},
                    {"label": "Kuwait", "value": "KWT"},
                    {"label": "Lebanon", "value": "LBN"},
                    {"label": "Libya", "value": "LBY"},
                    {"label": "Morocco", "value": "MAR"},
                    {"label": "Oman", "value": "OMN"},
                    {"label": "Qatar", "value": "QAT"},
                    {"label": "Saudi Arabia", "value": "SAU"},
                    {"label": "Syrian Arab Republic", "value": "SYR"},
                    {"label": "Tunisia", "value": "TUN"},
                    {"label": "Yemen, Rep.", "value": "YEM"},
                    {"label": "Canada", "value": "CAN"},
                    {"label": "United States", "value": "USA"},
                    {"label": "Afghanistan", "value": "AFG"},
                    {"label": "Bangladesh", "value": "BGD"},
                    {"label": "Bhutan", "value": "BTN"},
                    {"label": "India", "value": "IND"},
                    {"label": "Sri Lanka", "value": "LKA"},
                    {"label": "Nepal", "value": "NPL"},
                    {"label": "Pakistan", "value": "PAK"},
                    {"label": "Angola", "value": "AGO"},
                    {"label": "Burundi", "value": "BDI"},
                    {"label": "Benin", "value": "BEN"},
                    {"label": "Burkina Faso", "value": "BFA"},
                    {"label": "Botswana", "value": "BWA"},
                    {"label": "Central African Republic", "value": "CAF"},
                    {"label": "Cote d'Ivoire", "value": "CIV"},
                    {"label": "Cameroon", "value": "CMR"},
                    {"label": "Congo, Dem. Rep.", "value": "COD"},
                    {"label": "Congo, Rep.", "value": "COG"},
                    {"label": "Eritrea", "value": "ERI"},
                    {"label": "Ethiopia", "value": "ETH"},
                    {"label": "Gabon", "value": "GAB"},
                    {"label": "Ghana", "value": "GHA"},
                    {"label": "Guinea", "value": "GIN"},
                    {"label": "Gambia, The", "value": "GMB"},
                    {"label": "Guinea-Bissau", "value": "GNB"},
                    {"label": "Equatorial Guinea", "value": "GNQ"},
                    {"label": "Kenya", "value": "KEN"},
                    {"label": "Liberia", "value": "LBR"},
                    {"label": "Lesotho", "value": "LSO"},
                    {"label": "Madagascar", "value": "MDG"},
                    {"label": "Mali", "value": "MLI"},
                    {"label": "Mozambique", "value": "MOZ"},
                    {"label": "Mauritania", "value": "MRT"},
                    {"label": "Malawi", "value": "MWI"},
                    {"label": "Namibia", "value": "NAM"},
                    {"label": "Niger", "value": "NER"},
                    {"label": "Nigeria", "value": "NGA"},
                    {"label": "Rwanda", "value": "RWA"},
                    {"label": "Sudan", "value": "SDN"},
                    {"label": "Senegal", "value": "SEN"},
                    {"label": "Sierra Leone", "value": "SLE"},
                    {"label": "Somalia", "value": "SOM"},
                    {"label": "Eswatini", "value": "SWZ"},
                    {"label": "Chad", "value": "TCD"},
                    {"label": "Togo", "value": "TGO"},
                    {"label": "Tanzania", "value": "TZA"},
                    {"label": "Uganda", "value": "UGA"},
                    {"label": "South Africa", "value": "ZAF"},
                    {"label": "Zambia", "value": "ZMB"},
                    {"label": "Zimbabwe", "value": "ZWE"},
                     ],
                 multi=False,
                 value="COL",
                 style={'width': "40%"}
                 ),
    html.Br(),

    dcc.Graph(id='graph2', figure={}),

#################################################################
########################
    html.Div(children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children=' ', style={'textAlign': 'left', 'color': colors['text2']}),
                        html.P(
                            'Universidad Central', 
                            style={'textAlign': 'right', 'color': colors['text2']}),
                        html.P(
                            'Maestría en Analítica de Datos', 
                            style={'textAlign': 'right', 'color': colors['text2']}),
                        html.P(
                            'Curso Visualización de Datos', 
                            style={'textAlign': 'right', 'color': colors['text2']}),
                        html.P(
                            'Juan Guillermo Forero Neme', 
                            style={'textAlign': 'right', 'color': colors['text2']}),
                        html.P(
                            '2021', 
                            style={'textAlign': 'right', 'color': colors['text2']}),

                    ])

    ),   
    
]) 
#-------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [
     Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure'),
     #Output(component_id='graph1', component_property='figure'),
     ],
    [
     Input(component_id='slct_year', component_property='value'),
     #Input(component_id='slct_region', component_property='value')
     ]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))
    
    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    
    # Plotly Express
    fig = px.scatter_mapbox(dff, lat="latitude", lon="longitude", color= 'Region', hover_name="Country Name", hover_data=['Urban population', 'Rural polulation', 'Year'],
                            #color_discrete_sequence=["fuchsia"], 
                            zoom=1, height=700, size= 'Total Population')
    fig.update_layout(mapbox_style="open-street-map", plot_bgcolor='#F6D746', paper_bgcolor='#F6D746')
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

    return container, fig

@app.callback(
    [
     Output(component_id='graph1', component_property='figure'),
     ],
    [
     Input(component_id='slct_region', component_property='value')
     ]
)
def update_graph(option_slctd1):
    print(option_slctd1)
    print(type(option_slctd1))
    
    dff = df.copy()
    dff = dff[dff["Year"] == 2019]
    dff = dff[dff["Region"] == option_slctd1]

    # Plotly Express
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=dff['Country Name'],
        y=dff['% Rural'],
        name='Porcentaje Poblacion Rural',
        marker_color='#e55c30'
    ))
    fig1.add_trace(go.Scatter(
        x=dff['Country Name'],
        y=dff['%Urbano'],
        name='Porcentaje Poblacion Urbana',
        marker_color='#84206b',
        mode='lines+markers'
    ))

    fig1.update_layout(barmode='group', xaxis_tickangle=-45, plot_bgcolor='#F6D746', paper_bgcolor='#F6D746')
    #fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig1.show()

    return fig1, 

@app.callback(
    [
     Output(component_id='graph2', component_property='figure'),
     ],
    [
     Input(component_id='slct_country', component_property='value')
     ]
)
def update_graph(option_slctd2):
    print(option_slctd2)
    print(type(option_slctd2))

    dff = df.copy()
    dff = dff[dff["Country Code"] == option_slctd2]

    # Plotly Express
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=dff['Year'],
        y=dff['% Rural'],
        name='Porcentaje Poblacion Rural',
        marker_color='#e55c30'
    ))
    fig2.add_trace(go.Scatter(
        x=dff['Year'],
        y=dff['%Urbano'],
        name='Porcentaje Poblacion Urbana',
        marker_color='#84206b',
        mode='lines+markers'
    ))

    fig2.update_layout(barmode='group', xaxis_tickangle=-45, plot_bgcolor='#F6D746', paper_bgcolor='#F6D746')
    #fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig2.show()

    return fig2, 
   

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)