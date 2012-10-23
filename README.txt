Provides integration with Plone for the Clean Print product
(http://www.formatdynamics.com/diypub/).

To use clean print, you must agree to some terms and generate some
html/javascript:

  1. Enable the Wildcard.CleanPrint product
  2. Go to http://www.formatdynamics.com/diypub/
  3. Fill out the form and click the 'Generate CleanPrint Tag' button
  4. Copy the value of the SRC parameter of the <script> element and
     paste it into the Script URL configuration field in the CleanPrint
     settings (Site Setup -> CleanPrint Settings) and save the form
  5. Then there are 2 options for including buttons for clean print on
     your site:

     a. Make use of the defined portal_actions
     b. Use the generated Button HTML (or some derivation thereof) from
        step 2 in a custom template of some sort
