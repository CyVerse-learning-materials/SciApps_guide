|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


Building a Workflow
--------------------
A workflow is a series of apps chained together to run in sequence as a batch operation. On SciApps, workflows are generated from the analysis already completed in a history. Workflows can be viewed, shared, imported, and executed. Additionally, SciApps workflows capture inputs, intermediate outputs, and final results along with the analysis history. Importing a workflow will import the analysis history used to build the workflow.

----


**Example Data**

.. list-table::
    :header-rows: 1
    
    * - Input
      - Description
      - Example
    * - Marker file
      - Marker data in TASSEL Hapmap format
      - `myStudy_filt.c9.hmp.txt <https://data.sciapps.org/example_data/gwas_raw/myStudy_filt.c9.hmp.txt>`_
    * - Trait file
      - Trait data in TASSEL triat format
      - `trait.txt <https://data.sciapps.org/example_data/gwas_raw/trait.txt>`_

**SciApps App(s):**

.. list-table::
    :header-rows: 1
    
    * - App name
      - Version
      - Description
      - App link
      - Notes/other links
    * - MergeG2P
      - 0.0.2
      - Intersect marker data with trait data
      - `App link <https://www.sciapps.org/app_id/MergeG2P-0.0.2>`_
      - 
    * - NPUTE
      - 0.0.1
      - Imputes missing markers via voting from K-nearest-neighbors (KNN)
      - `App link <https://www.sciapps.org/app_id/NPUTE-0.0.1>`_
      - `Source <http://compgen.unc.edu/NPUTE_README.html>`_
    * - NumericalTransform-TASSEL
      - 4.3.15
      - Numerical Transform of marker data using TASSEL and PLINK
      - `App link <https://www.sciapps.org/app_id/NumericalTransform-TASSEL-4.3.15>`_
      - 
    * - CloudSTRUCTURE
      - 2.3.4
      - Parallelized STRUCTURE software for estimating population structures
      - `App link <https://www.sciapps.org/app_id/CloudSTRUCTURE-2.3.4>`_
      - `Source <http://pritch.bsd.uchicago.edu/structure.html>`_
    * - MLM-TASSEL
      - 5.1.23
      - Mixed Linear Model analysis using TASSEL
      - `App link <https://www.sciapps.org/app_id/MLM-TASSEL-5.1.23>`_
      - `Source <http://www.maizegenetics.net/>`_
    * - EMMAX
      - 0.0.2
      - Association mapping with consideration of sample structure
      - `App link <https://www.sciapps.org/app_id/EMMAX-0.0.2>`_
      - `Source <http://genetics.cs.ucla.edu/emmax/>`_
    * - MLMM
      - 0.0.2
      - An efficient multi-locus mixed-model approach for GWAS
      - `App link <https://www.sciapps.org/app_id/MLMM-0.0.2>`_
      - `Source <https://cynin.gmi.oeaw.ac.at/home/resources/mlmm>`_
    * - PCA
      - 0.0.1
      - Principal Component Analysis
      - `App link <https://www.sciapps.org/app_id/PCA-0.0.1>`_
      - `Source <https://stat.ethz.ch/R-manual/R-patched/library/stats/html/prcomp.html>`_

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
	
   3. On the 'Workflow Diagram', you can choose to download or save the workflow. 
   
      .. Tip::
        For downloading, you will get a JSON file, which can be passed to others for **sharing** the entire analysis. 
   
	
----

*Step 3: Adding New Analysis to the Workflow*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This step will show you how to add new analysis to the workflow built above. We will perform PCA on the imputed marker data (imputed.txt), which is the output of the NPUTE step.

  1. Click 'Workflow' (from the top navigation bar), then 'Load a workflow' to loaded the downloaded JSON file. Alternatively, click 'My Workflow' to load the workflow if you have saved the workflow in your workspace.
  
  2. Click **Clustering** category from the left panel or search for **PCA**, then click **PCA** to load **PCA 0.0.1**
     
  3. Click **2: NPUTE-0.0.1** in the History panel to expand its outputs, then drag and drop **imputed.txt** into the **Marker file** field
  
     |pca_workflow|
       
  4. Leave others as defaults, then click the "Submit Job" button
  
  5. Once completed, select all analyses to build a new workflow. Save or download the workflow for running it in the next section
  
     .. Note::
       The connection between **imputed.txt** and **PCA-0.0.1** is recorded through **dragging and dropping**, which is how SciApps workflows are built from scratch
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
    :height: 361
.. |emmax_pca_workflow| image:: ./img/sci_apps/emmax_pca_workflow.gif
    :width: 660
    :height: 295
