|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


SciApps Basics and Logging In
------------------------------

SciApps leverages CyVerse Agave API and Data Store for efficient data transfer, analysis, and management across heterogeneous systems. A CyVerse account is required to access these systems

**Some things to remember about the platform**

*Loading personal data to SciApps from CyVerse Data Store*

- SciApps access must be requested through the CyVerse user portal. You can check if you already have SciApps by logging into the portal and visiting the My Service page. If SciApps is not listed, click on Available services to request access
- Once requested, a ‘sci_data’ folder will be created in your Data Store root folder (/iplant/home/YOUR_USER_NAME). Any data you put in the folder will be available for using on SciApps (under the 'user' tab). For instructions on uploading data, check the `Data Store Guide <https://cyverse-data-store-guide.readthedocs-hosted.com/en/latest/index.html>`_

*Sample datasets*

- Sample datasets are available under the ‘public’ tab. These datasets are placed on the computing system for reducing data transfers and should be used whenever possible for building workflows
- More CyVerse sample datasets are available under the ‘shared’ tab. From there, sample datasets for most apps are available under ‘iplantcollaborative/example_data’

*Large datasets*

- SciApps is designed to process massive amount of data locally for minimizing cross-sites data transfer
- Existing workflows are built for execution on the CSHL computing system so it is not suitable to process large amount of data (>10GB) stored remotely (e.g. in the CyVerse Data Store)


----

*Logging into SciApps*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Access the SciApps website at https://www.SciApps.org/

  2. From the top navigation bar click on ‘Login’, you will be directed to the CyVerse Authentication Service page
  
  3. Enter your CyVerse username and CyVerse password, you will be redirected back to SciApps if successfully authenticated

     .. Note::
        To log out of SciApps and CyVerse, you need to click on 'Logout' from the top navigation bar. Additionally, your job histories in the right panel will be discarded after closing or refreshing the browser tab.
..
	#### Comment: Suggested style guide:
	1. Steps begin with a verb or preposition: Click on... OR Under the "Results Menu"
	2. Locations of files listed parenthetically, separated by carets, ultimate object in bold
	(Username > analyses > *output*)
	3. Buttons and/or keywords in bold: Click on **Apps** OR select **Arabidopsis**
	4. Primary menu titles in double quotes: Under "Input" choose...
	5. Secondary menu titles or headers in single quotes: For the 'Select Input' option choose...
	####


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
