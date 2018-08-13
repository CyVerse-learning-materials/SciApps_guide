|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


Viewing and Accessing Data
----------------------------

SciApps uses `CyVerse Data Store <https://cyverse-data-store-guide.readthedocs-hosted.com/en/latest/>`_
for user data management. Besides public and shared data, SciApps can only access data placed in your **sci_data** folder. Following steps show how this folder can be created.

----

*Browsing/Navigating CyVerse Data Store on SciApps*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Log into CyVerse User portal at https://user.cyverse.org.

  2. By default, you will see 'My SERVICES'. If SciApps is not listed, click 'AVAILABLE', then 'REQUEST ACCESS'.

     |cyverse_user|

     .. Note::

       Once requested, SciApps will create the **sci_data** folder in your Data Store home folder. Any data you put in this folder can be used to build workflows. The REQUEST step is one-time operation, and after this, you can log into SciApps directly at https://www.SciApps.org.

  3. If SciApps is listed, click 'LAUNCH'.

     |sciapps_launch|

  4. Load any App form by clicking on an App name in the left panel. For any steps that require an input, click '**or Browse DataStore**' to open the browsing window.

     .. tip::

       Click **example** to browse example data sets used by public workflows (e.g. example data for MAKER below):

       |data_window|

       Other tabs include:

       - **home**: Your CyVerse Data Store (**sci_data** folder only)
       - **shared**: Community data shared with everybody
       - **Go up**: Move up one level
       - **Refresh**: Reload current folder

  5. Check the checkbox in front the file or folder to use it as input, then close the browsing window.

----

*Accessing Data on SciApps*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to organize your data, including CyVerse DE, CyberDuck, and iCommands. 

----

  1. Access CyVerse DE at https://de.cyverse.org if you want to use a GUI to `upload or download small data <https://pods.iplantcollaborative.org/wiki/display/DEmanual/Uploading+and+Importing+Data+Items+Within+the+DE>`_. You could also use it to organize or share your data

  2. For bulk data transfer with CyberDuck, here is the `information <https://pods.iplantcollaborative.org/wiki/display/DS/Using+Cyberduck+for+Uploading+and+Downloading+to+the+Data+Store>`_ to get started

  3. For command line users, here is the `documentation <https://pods.iplantcollaborative.org/wiki/display/DS/Using+iCommands>`_ for using iCommands

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
    :width: 500
    :height: 266
.. |cyverse_user| image:: ./img/sci_apps/cyverse_user.gif
    :width: 660
    :height: 362
.. |sciapps_launch| image:: ./img/sci_apps/sciapps_launch.gif
    :width: 550
    :height: 172
