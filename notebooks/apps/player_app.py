import dask.dataframe as dd
import holoviews as hv
import geoviews as gv

from bokeh.models import Slider, Button
from bokeh.layouts import layout
from bokeh.io import curdoc
from bokeh.models import WMTSTileSource

from holoviews.operation.datashader import datashade, aggregate, shade
from holoviews.plotting.util import fire
shade.cmap = fire

hv.extension('bokeh')
renderer = hv.renderer('bokeh').instance(mode='server')

# Load data
usecols = ['tpep_pickup_datetime', 'dropoff_x', 'dropoff_y']
ddf = dd.read_csv('../data/nyc_taxi.csv', parse_dates=['tpep_pickup_datetime'], usecols=usecols)
ddf['hour'] = ddf.tpep_pickup_datetime.dt.hour
ddf = ddf.persist()

### Define the HoloViews objects here ####


### Pass the HoloViews object to the renderer
plot = renderer.get_plot(hvobj, doc=curdoc())

# Define a slider and button
start, end = 0, 23

def slider_update(attrname, old, new):
    stream.event(hour=new)

slider = Slider(start=start, end=end, value=0, step=1, title="Hour")
slider.on_change('value', slider_update)

def animate_update():
    year = slider.value + 1
    if year > end:
        year = start
    slider.value = year

def animate():
    if button.label == '► Play':
        button.label = '❚❚ Pause'
        curdoc().add_periodic_callback(animate_update, 1000)
    else:
        button.label = '► Play'
        curdoc().remove_periodic_callback(animate_update)

button = Button(label='► Play', width=60)
button.on_click(animate)

# Combine the bokeh plot on plot.state with the widgets
layout = layout([
    [plot.state],
    [slider, button],
], sizing_mode='fixed')

curdoc().add_root(layout)
