|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


Building a Workflow
--------------------
A workflow is a series of apps chained together to run in sequence as a batch operation. On SciApps, workflows are generated from the analysis already completed in a history. Workflows can be viewed, shared, imported, and executed. Additionally, SciApps workflows capture inputs, intermediate outputs, and final results along with the analysis history. Importing a workflow will import the analysis history used to build the workflow.

----

*Step 1: Importing a Workflow History*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This step will show you how to import a history/workflow from a remote source into your own workspace. We will be using this history to build a new workflow. The example used here is the public association workflow.

  1. Login to `SciApps <https://www.SciApps.org/>`_

  2. Click 'Workflow' (from the top navigation bar), then 'Public workflows' to load the public workflow page in the main panel
     
     .. Tip::
       When the right panel (History) is empty, Click the 'public workflow' link (on the top of the History panel) to load the public workflow page
       
  3. Click the 'Association' link to load the Association Workflow. The app forms are loaded in the main panel, and analysis history is loaded in the right panel.
  
     |association_workflow|
      
     .. Tip::
       To view the workflow diagram, scroll down the main panel and click the 'Show Diagram' button

----

*Step 2: Creating a Workflow*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This step will demo how to build a workflow from the loaded history. Assume we just want to use EMMAX for association analysis.

   1. Check the checkbox for step 1, 2, 3, and 6 in the History panel, then click the 'build a workflow' link (on the top of the History panel) to load the Workflow building page. Alternatively, Click 'Workflow' (from the top navigation bar), then 'Build a workflow' to load the workflow building page
      
      |build_workflow|
      
      .. Tip::
        History panel Checkboxes and the workflow building page are interactive. Use the 'Select All' or 'Reset' button to simplify the selection step

   2. Modify **Workflow Name** and **Workflow Description**, then click the 'Build Workflow' button to visualize the workflow
   
      .. Tip::
        All nodes of the diagram are interactive
        |emmax_workflow|
	
   3. On the 'Workflow Diagram', you can choose to download or save the workflow. For downloading, you will get a JSON file, which can be passed to others for sharing the entire analysis. 
   
	
----

*Step 3: Adding additional analyses to a Workflow*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This step will show you how to add new analysis to the workflow built above. We will perform PCA on the imputed marker data (imputed.txt), which is the output of the NPUTE step.

  1. Click 'Workflow' (from the top navigation bar), then 'Load a workflow' to loaded the downloaded JSON file. Alternatively, click 'My Workflow' to load the workflow if you have saved the workflow in your workspace.
  
  2. Click **Clustering** category from the left panel or search for PCA, then click **PCA** to load PCA 0.0.1
     
  3. Click **2: NPUTE-0.0.1** in the History panel to expand its outputs, then drag and drop **imputed.txt** into the **Marker file** field
  
     |pca_workflow|
       
  4. Leave others as defaults, then click the "Submit Job" button
  
  5. Once completed, select all analyses to build a new workflow
  
     .. Note::
       The connection between **imputed.txt** and **PCA-0.0.1** is recorded through analysis, which is exactly how the Association workflow is built
       |emmax_pca_workflow|
     
----

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
.. |association_workflow| image:: ./img/sci_apps/association_workflow.gif
    :width: 660
    :height: 394
.. |build_workflow| image:: ./img/sci_apps/build_workflow.gif
    :width: 660
    :height: 359
.. |emmax_workflow| image:: ./img/sci_apps/emmax_workflow.gif
    :width: 660
    :height: 325
.. |pca_workflow| image:: ./img/sci_apps/pca_workflow.gif
    :width: 660
    :height: 409
.. |emmax_pca_workflow| image:: ./img/sci_apps/emmax_pca_workflow.gif
    :width: 660
    :height: 295
