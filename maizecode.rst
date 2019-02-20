|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


Accessing MaizeCODE Data
----------------------------

Customized apps (e.g. `MCRNAseq-0.0.1 <https://www.sciapps.org/app_id/MCRNAseq-0.0.1/>`_) are built to perform QC and preliminary quantifications on the MaizeCODE raw data. For each MaizeCODE experiment, the analysis of all replicates are saved as a SciApps workflow (with a unique ID), which records the relationship between raw reads and their derived results. Following sections illustrate how users can check the QC results of any MaizeCODE experiments, as well as using the preliminary results for performing various downstream analysis.

----

*Check QC Results of an Experiment*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Open https://www.SciApps.org, click *Data* (top menu) then *MaizeCODE*. Alternatively, you can access MaizeCODE experiments directly at https://www.SciApps.org/data/MaizeCODE 

     |MaizeCODE|

  2. Locate an experiment by searching with keyword ''

    .. note::
       
       Experiments can also be located by searching with  workflow id. For each experiment, the workflow id is stored as metadata of the first read of the first replicate (e.g. https://).

  3. Check the experiment, then click *load* to load derived results into the History panel.

     .. note::

       |data_window|

       Results are:

       - **home**: Your CyVerse Data Store (**sci_data** folder only)
       - **shared**: Community data shared with everybody
       - **Go up**: Move up one level
       - **Refresh**: Reload current folder

  4. Click the Visualization icon to display the list of outputs. SelectC

----

*Find differentially expressed genes*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to organize your data, including CyVerse DE, CyberDuck, and iCommands. 

----

  1. Access CyVerse DE at https://de.cyverse.org if you want to use a GUI to `upload or download small data <https://pods.iplantcollaborative.org/wiki/display/DEmanual/Uploading+and+Importing+Data+Items+Within+the+DE>`_. You could also use it to organize or share your data

  2. For bulk data transfer with CyberDuck, here is the `information <https://pods.iplantcollaborative.org/wiki/display/DS/Using+Cyberduck+for+Uploading+and+Downloading+to+the+Data+Store>`_ to get started

  3. For command line users, here is the `documentation <https://pods.iplantcollaborative.org/wiki/display/DS/Using+iCommands>`_ for using iCommands

----

*Find differentially expressed isoforms*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to organize your data, including CyVerse DE, CyberDuck, and iCommands.

----

  1. Access CyVerse DE at https://de.cyverse.org if you want to use a GUI to `upload or download small data <https://pods.iplantcollaborative.org/wiki/display/DEmanual/Uploading+and+Importing+Data+Items+Within+the+DE>`_. You could also use it to organize or share your data

----

**Fix or improve this documentation:**

- On Github: `Repo link <https://github.com/CyVerse-learning-materials/SciApps_guide/blob/master/step2.rst>`_
- Send feedback: `Tutorials@CyVerse.org <Tutorials@CyVerse.org>`_

----

  |Home_Icon|_
  `Learning Center Home <http://learning.cyverse.org/>`_

.. |CyVerse logo| image:: ./img/cyverse_rgb.png
    :width: 500
    :height: 100
.. _CyVerse logo: http://learning.cyverse.org/
.. |Home_Icon| image:: ./img/homeicon.png
    :width: 25
    :height: 25
.. _Home_Icon: http://learning.cyverse.org/
.. |data_window| image:: ./img/sci_apps/data_window.gif
    :width: 582
    :height: 264
.. |cyverse_user| image:: ./img/sci_apps/cyverse_user.gif
    :width: 660
    :height: 362
.. |sciapps_launch| image:: ./img/sci_apps/sciapps_launch.gif
    :width: 550
    :height: 172
