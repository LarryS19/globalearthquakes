import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Analyze the structure of data for the following file
filename = 'eq_data_july5.json'  # JSON file path
with open(filename) as f:
    all_eq_data = json.load(f)

# Access the lists of earth quake data and metadata
all_eq_dicts = all_eq_data['features']
metadata = all_eq_data['metadata']

# Create lists and store magnitudes and coordinates
magnitudes = [each_dic['properties']['mag'] for each_dic in all_eq_dicts]
approx_loc = [each_dic['properties']['title'] for each_dic in all_eq_dicts]
longitudes = [each_dic['geometry']['coordinates'][0] for each_dic in all_eq_dicts]
latitudes = [each_dic['geometry']['coordinates'][1] for each_dic in all_eq_dicts]

# Prepare and format data for scatter plot
data = [{'type': 'scattergeo',
         'lon': longitudes,
         'lat': latitudes,
         'text': approx_loc,
         'marker': {
             'size': [5 * mag for mag in magnitudes],
             'color': magnitudes,
             'colorscale': 'portland',
             'colorbar':{'title': 'Magnitude'},
         },
         }]

# Plot Data
my_layout = Layout(title=f"{metadata['title']}"
                         f"\n (July 5th 2021)")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='index.html')