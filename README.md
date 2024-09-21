
Our Python script processes data for male and female athletes from CSV files from the given drive folder. We did not include the csv files here as there were simply too many.
The short program generates different HTML tables with athlete data provided. For our index page it creates a table inside a table to include both female and male athletes. Furthermore we added a loop function to create individual HTML pages for each athlete.

The output includes an HTML page (index.html) with links to individual athlete profiles, which contains their personal records.

Our basic data structure is given below       \
github                                        \
&emsp; athlete_pages                          \
&emsp;&emsp; [athlete_id].html                \
&emsp; index.html                             \
&emsp; render_templates.py                    \
&emsp; images                                 \
&emsp; AthleteImages                          \
&emsp;&emsp; [athlete_id].jpg                 \
&emsp; icon.png                               \
&emsp; images.jpeg                            \
&emsp; site_logo.png                           
