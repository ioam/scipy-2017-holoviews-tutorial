import dask.dataframe as dd
from holoviews.operation.datashader import datashade
import holoviews as hv

renderer = hv.renderer('bokeh')

# Load data
ddf = dd.read_csv('../data/nyc_taxi.csv', usecols=['dropoff_x', 'dropoff_y']).persist()

# Declare points and datashade them
points = hv.Points(ddf, kdims=['dropoff_x', 'dropoff_y'])
shaded = datashade(points).opts(plot=dict(width=800, height=600))

doc = renderer.server_doc(shaded)
doc.title = 'HoloViews Bokeh App'