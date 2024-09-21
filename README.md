
Our Python script processes data for male and female athletes from CSV files from the given drive folder. We did not include the csv files here as there were simply too many.
The short program generates different HTML tables with athlete data provided. For our index page it creates a table inside a table to include both female and male athletes. Furthermore we added a loop function to create individual HTML pages for each athlete.

The output includes an HTML page (index.html) with links to individual athlete profiles, which contains their personal records.

Our basic data structure is given below
github
    athlete_pages
        [athlete_id].html
    index.html
    render_templates.py
    images
      AthleteImages
        [athlete_id].jpg
      icon.png
      images.jpeg
      site_logo.png
