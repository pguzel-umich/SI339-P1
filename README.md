# OVERVIEW

Our Python script processes data for male and female athletes from CSV files from the given drive folder. We did not upload the CSV files to GitHub because there were simply too many of them.
Our short program generates different HTML tables with the provided athlete data. For our index page, it creates a table inside a table to include both female and male athletes. Furthermore we added a loop function to create individual HTML pages for each athlete.

The output includes an HTML page (index.html) with links to individual athlete profiles, which contains their personal records.

## How It Works

## How To Use

## Running
To run, simply download the code and enter the provided line below to your terminal:
> python render_templates.py

## Data Requirements
For phyton code to run, we require just the CSV files that include athlete and event data. Download the files from the drive provided by SI339 staff. We put all the files on the drive and called drive_download for ease of access and navigation. The two below are the files we absolutely need. We find all the data names and tags there.
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
