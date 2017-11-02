|CyVerse logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_


Running a SciApps Workflow
---------------------------
Here we will run the workflow created in the 'Building a Workflow' section.

----

*Running the example Association Workflow*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. If necessary, login to `SciApps <https://www.SciApps.org/>`_

  2. Navigate to 'Workflow', then 'My workflows', to load the workflow you created and saved in the last section

     |my_workflow|

     .. Tip::
       From left to right, there are four icons next to the workflow name and description:

       - **Load**: Load the workflow with app forms in main panel and history in right panel
       - **Edit**: Modify the workflow name and/or description
       - **Download**: Download the workflow json
       - **Delete**: Delete the workflow from your account

  3. Alternatively, you can load the workflow by navigating to 'Workflow', 'Load a workflow', and then paste this URL: `https://data.sciapps.org/misc/my_pca_workflow.json<https://data.sciapps.org/misc/my_pca_workflow.json>`_

     |load_workflow|
 
     .. Tip::
       Before loading a workflow, you can refresh the browser window to clean out the History panel

  4. Optional: For **Step 1: MergeG2P**, under **Select marker file in Hapmap format**
     click the **or Browse DataStore** button, then navigate to and select
     `myStudy_filt.c9.hmp.v2.txt <https://data.sciapps.org/example_data/gwas_raw/myStudy_filt.c9.hmp.v2.txt>`_
     ; then click ‘Select and Close’. (Location: *example_data > gwas_raw > myStudy_filt.c9.hmp.v2.txt*)

     |run_workflow|

     .. Note::
       Marker file aligned to version 1 assembly of Sorghum is also available as myStudy_filt.c9.hmp.txt

  5. Leave others as defaults, scroll down the main panel, and then click
     **Submit Workflow**. You will be asked to confirm and prompted to check
     the job status in the right panel. Then a live workflow diagram will be
     displayed with real time analysis status updates.

     .. Note::

       |running_workflow|

       The color of the app node will change when the status of the analysis changes:

       - 'Yellow': Pending
       - 'Blue': Running
       - 'Green': Completed
       - 'Red': Failed

----

*Visualizing SciApps Workflow Result*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   1. Once the entire workflow is completed, click **4: EMMAX-0.0.2** in the
      History panel to expand its outputs.

      |workflow_results|

   2. Click **manhattan.plot** from the list of outputs, you will be directed
      to the Manhattan plot of the results. Check Q-Q plot and click the
      Manhattan plot to check nearby genes around the clicked position.

      |manhattan_plot|

      .. Note::
        The example here is using Chromosome 9 only. And the Manhattan plot is
        pre-configured to display the same Chromosome. For your own data, use
        the options on the left side to check a specific Chromosome, or all
        Chromosomes of your specific genome.

   3. Use the options on the left side for P-values adjustments, specifying
      species, chromosome, neighboring window size, and display Q-Q plot.

      .. Tip::
        Both Manhattan plot and Q-Q plot are interactive with all of the options.

   4. For visualizing **PCA** outputs, click the **(i)** icon for **5: PCA-0.0.1**,
      then click the output folder link, you will be directed to the data page of
      PCA outputs. There are two image outputs:  `pcplot <https://cran.r-project.org/web/packages/ggfortify/vignettes/plot_pca.html>`_
      and `scree plot <http://support.minitab.com/en-us/minitab/17/topic-library/modeling-statistics/multivariate/principal-components-and-factor-analysis/what-is-a-scree-plot/>`_

      |pca_output1| |pca_output2|
      
      .. Note::
        The output of PCA, **pca_output.txt**, can also be used with **MLM-TASSEL** for correcting population structure
----

*Summary*
~~~~~~~~~

Using the app SNAP and the Association workflow as examples, you have gotten an
overview of how SciApps workflows work - from accessing data in CyVerse Data
Store, to launching jobs, building workflows, importing workflows,
running workflows, and visualizing results.


More help and additional information
`````````````````````````````````````

..
    Short description and links to any reading materials

Search for an answer:
    `CyVerse Learning Center <http://learning.cyverse.org>`_ or
    `CyVerse Wiki <https://wiki.cyverse.org>`_

Post your question to the user forum:
    `Ask CyVerse <http://ask.iplantcollaborative.org/questions>`_

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
.. |my_workflow| image:: ./img/sci_apps/my_workflow.gif
    :width: 480
    :height: 208
.. |load_workflow| image:: ./img/sci_apps/load_workflow.gif
    :width: 480
    :height: 172
.. |run_workflow| image:: ./img/sci_apps/run_workflow.gif
    :width: 660
    :height: 318
.. |running_workflow| image:: ./img/sci_apps/running_workflow.gif
    :width: 660
    :height: 299
.. |workflow_results| image:: ./img/sci_apps/workflow_results.gif
    :width: 660
    :height: 319
.. |manhattan_plot| image:: ./img/sci_apps/manhattan_plot.gif
    :width: 660
    :height: 355
.. |pca_output1| image:: ./img/sci_apps/pca_output1.gif
    :width: 300
    :height: 297
.. |pca_output2| image:: ./img/sci_apps/pca_output2.gif
    :width: 300
    :height: 284
