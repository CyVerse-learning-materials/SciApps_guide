|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


Launching an Analysis Job
--------------------------

For analyzing data, you can select an app from the left panel of SciApps. In this example, to cover the minimum you need to launch an analysis, we will use the **SNAP** gene finding app to estimate Hidden Markov Model (HMM) parameters with a GFF file output from MAKER, an annotation app. 

----

.. #### Comment: short description

**Example Data**

.. list-table::
    :header-rows: 1
    
    * - Input
      - Description
      - Example
    * - Annotated gene models
      - MAKER output in GFF3 format
      - `maker_out.gff <https://data.sciapps.org/example_data/maker/maker_out.gff>`_

**SciApps App(s):**

.. list-table::
    :header-rows: 1
    
    * - App name
      - Version
      - Description
      - App link
      - Notes/other links
    * - SNAP
      - 0.0.1
      - Semi-HMM-based Nucleic Acid Parser
      - `App link <https://www.sciapps.org/app_id/SNAP-0.0.1>`_
      - `Source: <http://korflab.ucdavis.edu/software.html>`_


*Example SciApps Analysis: HMM parameters estimation with SNAP*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Login to `SciApps <https://www.SciApps.org/>`_

  2. Click **Prediciton** category from the left panel; search for SNAP or click this link to `SNAP 0.0.1 <https://www.sciapps.org/app_id/SNAP-0.0.1>`_
  
  3. Under “GFF file” click **or Browse DataStore**, then navigate to and select
   `maker_out.gff <https://data.sciapps.org/example_data/maker/maker_out.gff>`_; then click 'Select and Close'.

   (Location: *public > maker > maker_out.gff*)

  4. Leave others as defaults, and then click **Submit Job**. You will be asked to confirm and prompted to check the job status in the right panel.
  
----

..
	#### Comment: Suggested style guide:
	1. Steps begin with a verb or preposition: Click on... OR Under the "Results Menu"
	2. Locations of files listed parenthetically, separated by carets, ultimate object in bold
	(Username > analyses > *output*)
	3. Buttons and/or keywords in bold: Click on **Apps** OR select **Arabidopsis**
	4. Primary menu titles in double quotes: Under "Input" choose...
	5. Secondary menu titles or headers in single quotes: For the 'Select Input' option choose...
	####

**Fix or improve this documentation:**

- On Github: `Repo link <https://github.com/CyVerse-learning-materials/SciApps_guide>`_
- Send feedback: `Tutorials@CyVerse.org <Tutorials@CyVerse.org>`_

----

.. |CyVerse logo| image:: ./img/cyverse_rgb.png
    :width: 500
    :height: 100
.. _CyVerse logo: http://learning.cyverse.org/
.. |Home_Icon| image:: ./img/homeicon.png
    :width: 25
    :height: 25
.. _Home_Icon: http://learning.cyverse.org/
.. |snap_app| image:: ./img/sci_apps/snap.gff
    :width: 550
    :height: 428
