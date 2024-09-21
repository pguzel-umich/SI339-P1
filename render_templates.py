import csv
import os
import json

# Read from the csv files (all??) in directory
male_athelete_dir = "drive_download/athletes/mens_team"
female_athelete_dir = "drive_download/athletes/womens_team"

count = 0
male_athletes_table = ""
female_athletes_table = ""

# Data required to render templates
athlete_data_male = []
athlete_data_female = []


# load data requires a directory and an athlete list that will be modified to hold dictionaries where every dictionary is the data of a student in the directory
def load_data(directory, athlete_list):
    # Read csv files for files in directory
    for filename in os.listdir(directory):

        with open(directory + "/" + filename, 'r') as fh:
            
            table = csv.reader(fh)
            
            # Want reset for every new athlete
            athlete_dict = {}
            season_list = []
            career_list = []

            #Store the id and name
            athlete_dict['name'] = next(table)
            athlete_dict['id'] = next(table)

            for row in table:

                # grab data only if a row is not empty nor a header
                if len(row) != 0 and row != ['Name', 'Overall Place', 'Grade', 'Time', 'Date', 'Meet', 'Comments', 'Photo']:


                    # Check if the row is season record row (denoted by having a value in the grade column)
                    if row[2] != '':
                        season_list.append(row)
                    else: # Append all other races to their total career
                        career_list.append(row)
            
            athlete_dict["season_record"] = season_list
            athlete_dict["career"] = career_list

            # Append completed student dictionary into athlete_list
            athlete_list.append(athlete_dict)

            # pretty_print = json.dumps(athlete_dict, indent=2)
            # print(pretty_print)
    
#athlete list is data structure returned from load_data
def template_table(athlete_list):
    template_html = ""

    for athlete_dict in athlete_list:

        # pretty_print = json.dumps(athlete_dict, indent=2)
        # print(pretty_print)
        # For every athlete we want to add in a new row within our table


        template_html += f"""
        <tr>
            <td>
                <div>
                    <img src="drive_download/images/AthleteImages/{athlete_dict['id']}.jpg" alt="img of {athlete_dict['name'][0]}, id: {athlete_dict['id']}" width="50" height="50">

                    <!-- not all the images we require exists in the folders provided to us, but we have realized that there should exists profile pictures of athletes (there is a column in meet csv) that uses their id and .jpg extension to navigate and call them -->
                    
                    {athlete_dict['name'][0]}
                    {athlete_dict['id'][0]}
                </div>
            </td>
        </tr>
        """
    
    return template_html



load_data(male_athelete_dir,athlete_data_male)
load_data(female_athelete_dir,athlete_data_female)
male_athletes_table = template_table(athlete_data_male)
female_athletes_table = template_table(athlete_data_female)
# print(athlete_data_male)
# with open('output.txt', 'w') as file:
#     file.write(str(athlete_data_male))

index_html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title> <!--Title TK-->

</head>
<body>
    
    <!--nav bar-->
    <div id="tk1">
        <img src="/images/site_logo.png" alt="site logo"> <!-- IMG TK-->
        <nav>
            <ul>
                <li><a href="https://www.google.com/">login</a></li>
            </ul>
        </nav>
    </div>

    <!--Main box-->
    <div>
        <h1><a href="https://www.athletic.net">Athletic.net</a></h1>

        <!--Main box 1-->
            <!-- Logo?? of what school (make h1 tag)-->
            <!-- title?? of what schoo.?? -->

        <!--Main box 2 Comments-->
        <div id="box2">
            <!--Title tk-->
            <div>
                <!-- Templatize commemnts?? -->
                Comments: 
            </div>
        </div>

        <!--Main box 3-->
        <div id="athletes">
            <table>
                <tr>
                    <td>
                        <table>
                            <tr>
                                <th>Mens</th>
                            </tr>
                            <tbody>
                                {male_athletes_table}
                            </tbody>
                        </table>
                    </td>
                    <td>
                        <table>
                            <tr>
                                <th>Womens</th>
                            </tr>
                            <tbody>
                                {female_athletes_table}
                            </tbody>
                        </table>
                    </td>
                </tr>
            </table>

        </div>

        <!--Main box 4-->
        <footer id="footer">
            <nav>
                <ul>
                    <li><a href="">coaches</a></li> <!--Link tk-->
                    <li><a href="">contact</a></li>
                </ul> 
            </nav>
        </footer>
    </div>



</body>
</html>
"""
# print(index_html_template)

with open("index.html", 'w') as file:
    file.write(index_html_template)