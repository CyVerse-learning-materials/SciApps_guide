|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


SciApps Basics and Logging In
------------------------------

SciApps leverages CyVerse Agave API and Data Store for efficient data transfer, analysis, and management across heterogeneous systems. A CyVerse account is required to access these systems

**Some things to remember about the platform**

*Sample datasets*

- Sample datasets are available under the ‘public’ tab. These datasets are placed on the computing system for reducing data transfers and should be used whenever possible for building workflows
- More CyVerse sample datasets are available under the ‘shared’ tab (CyVerse credentials required). From there, sample datasets for most apps are available under ‘iplantcollaborative/example_data’

*Large datasets*

- SciApps is designed to process massive amount of data locally for minimizing cross-sites data transfer
- Existing workflows are built for execution on the CSHL computing system so it is not suitable to process large amount of data (>10GB) stored remotely (e.g. in the CyVerse Data Store)


----

*Logging into SciApps*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Access the SciApps website at https://www.SciApps.org/

  2. Click on ‘Login’ (from the top navigation bar), you will be directed to the CyVerse Authentication Service page
  
  3. Enter your CyVerse username and CyVerse password, you will be redirected back to SciApps if successfully authenticated

     .. Tip::
        To log out of SciApps and CyVerse, you need to click on 'Logout' from the top navigation bar. Additionally, your job histories in the right panel will be discarded after closing or refreshing the browser tab.
..

*Access Without Logging In*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   1. Access the SciApps website at https://www.SciApps.org/ 
   
   2. Navigate public data
   
   3. Load app form by clicking on the app name in left panel
   
   4. Load public workflows (or workflow templates) from right panel or click on 'Workflow' then 'Public Workflows' from top navigation bar
   
   5. Build new workflows from the workflow templates, visualize workflow diagram, and download workflow in JSON format
   
      .. Note::
        Without logging in, you can not view data in CyVerse Data Store, submit analysis job, or save worlflows.
..


----

**Fix or improve this documentation:**

- On Github: `Repo link <https://github.com/CyVerse-learning-materials/sciapps_guide>`_
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
