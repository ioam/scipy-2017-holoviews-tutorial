scipy-2017-holoviews-tutorial
===========================
HoloViews tutorial at SciPy 2017

Create a conda environment from ``environment.yml``
-----------------------------------------------------

The easiest way to get an environment set up for the tutorial is
installing it from the ``environment.yml`` we have provided. If you
don't already have it install `conda<
https://www.continuum.io/downloads>`_ and create the ``hvtutorial``
environment by executing::

   > conda env create -f environment.yml

when installation is complete you may acivate the environment by writing::

   > activate hvtutorial

or using bash::

   $ source activate hvtutorial

next step is to start the jupyter notebook::

   (hvtutorial)> cd notebooks
   (hvtutorial)> jupyter notebook

a browser window with a Jupyter Notebook instance will open letting
you select and execute the notebooks.

To exit the environment you write::

   > deactivate

If you for some reason want to remove the environment you can do so by writing::

   > conda env remove --name hvtutorial
