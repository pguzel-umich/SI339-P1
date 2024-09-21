# OVERVIEW

Our Python script processes data for male and female athletes from CSV files from the given drive folder. We did not upload the CSV files to GitHub because there were simply too many.
Our short program generates different HTML tables with the provided athlete data. For our index page, it creates a table inside a table to include both female and male athletes. Furthermore, we added a set of functions with loops to make individual HTML pages for each athlete.

The output includes an HTML page (index.html) with links to individual athlete profiles containing their personal records.

## How It Works

### Data Requirements
For phyton code to run, we require just the CSV files that include athlete and event data. Download the files from the drive provided by SI339 staff. We put all the files on the drive and called drive_download for easy access and navigation. The two below are the files we absolutely need. We find all the data names and tags in these two files. The rest of the data on GitHub is required for HTML5 documents to run correctly and include all the other data, the data that we do not need to create the HTML5 files themselves (images, favicon, logo, etc.).
> drive_download/athletes/mens_team    \
> drive_download/athletes/womens_team

## How To Use
Clone the project and navigate to the project directory. Download the data stated in **Data Requirements** and place the folders properly. Then to run, simply enter the provided line below to your terminal:
> python render_templates.py

The script will generate: \
A main HTML page (index.html) displaying tables of all athletes with links to their profile pages. \
Each athlete's Individual HTML profile pages contain their season and career records. To prevent overpopulation in the main working directory, these will be placed in the athlete_pages/directory.

## GitHub Data Structure
github                                                  \
&emsp;&emsp; athlete_pages                              \
&emsp;&emsp;&emsp;&emsp; [athlete_id].html              \
&emsp;&emsp; index.html                                 \
&emsp;&emsp; render_templates.py                        \
&emsp;&emsp; images                                     \
&emsp;&emsp;&emsp;&emsp; AthleteImages                  \
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [athlete_id].jpg   \
&emsp;&emsp;&emsp;&emsp; icon.png                       \
&emsp;&emsp;&emsp;&emsp; images.jpeg                    \
&emsp;&emsp;&emsp;&emsp; site_logo.png                           
