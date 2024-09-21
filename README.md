## OVERVIEW

Our Python script processes data for male and female athletes from CSV files from the given drive folder. We did not include the csv files here as there were simply too many.
The short program generates different HTML tables with athlete data provided. For our index page it creates a table inside a table to include both female and male athletes. Furthermore we added a loop function to create individual HTML pages for each athlete.

The output includes an HTML page (index.html) with links to individual athlete profiles, which contains their personal records.

## HOW TO USE

# Running
To run simply download the code and enter the provided line below to your terminal:
> python main_script.py

# Data Requirements
For phyton code to run we actaully require just csv files that would include athlete and event data. Download the files from the drive provided by SI339 staff. For ease of access and navigation we put all the files on the drive and called drive_download. The two below are the files we absolutely need, we find all the data names and tags through there.
> drive_download/athletes/mens_team
> drive_download/athletes/womens_team



### GitHub Data Structure
github                                        \
&emsp;&emsp; athlete_pages                          \
&emsp;&emsp;&emsp;&emsp; [athlete_id].html                \
&emsp;&emsp; index.html                             \
&emsp;&emsp; render_templates.py                    \
&emsp;&emsp; images                                 \
&emsp;&emsp;&emsp;&emsp; AthleteImages                          \
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [athlete_id].jpg                 \
&emsp;&emsp;&emsp;&emsp; icon.png                               \
&emsp;&emsp;&emsp;&emsp; images.jpeg                            \
&emsp;&emsp;&emsp;&emsp; site_logo.png                           
