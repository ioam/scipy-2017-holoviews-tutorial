scipy-2017-holoviews-tutorial
===========================

HoloViews tutorial at SciPy 2017

Create a conda environment from ``environment.yml``
-----------------------------------------------------

The easiest way to get an environment set up for the tutorial is
installing it from the ``environment.yml`` we have provided. If you
don't already have it install `conda <
https://www.continuum.io/downloads>`_ and create the ``hvtutorial``
environment by executing::

   > conda env create -f environment.yml

when installation is complete you may activate the environment by writing::

   > activate hvtutorial

or using bash::

   $ source activate hvtutorial

next step is to start the jupyter notebook::

   (hvtutorial)> cd notebooks
   (hvtutorial)> jupyter notebook --NotebookApp.iopub_data_rate_limit=100000000

a browser window with a Jupyter Notebook instance will open letting
you select and execute the notebooks. (Increasing the rate limit in
this way is required for the current 5.0 Jupyter version, but should
not be needed in later Jupyter releases.)

To exit the environment you write::

   > deactivate

If you for some reason want to remove the environment you can do so by writing::

   > conda env remove --name hvtutorial


Downloading the sample data
---------------------------

In this tutorial we will be showing you how to work with some fairly
large datasets, unfortunately that also means that you have to
download this data. To make this as easy as possible we have provided
a script that will download the data for you, simply execute in the
root of the repository::

  > python download_sample_data.py


Preparing for the Tutorial
--------------------------

If you want to get familiar with HoloViews before the tutorial (which
is not a requirement), you can have a look at our new website at
`holoviews <http://holoviews.org/>`_ looking through the getting
started and user guides. If you want to run these examples yourself,
you can get a hold of them using this command inside your conda
environment::

    (hvtutorial)> holoviews --install-examples
	(hvtutorial)> cd holoviews-examples

This will create a holoviews-examples folder in your current directory.
Now launch a Jupyter notebook server and dive into the examples::

    (hvtutorial)> jupyter notebook --NotebookApp.iopub_data_rate_limit=100000000
