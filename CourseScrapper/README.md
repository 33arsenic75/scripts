# Course Scrapper
Can be used to find which professor took which course in which semester.
## Run
```
python3 CourseScrapper.py
```
It generated a .csv file and a .db file by "Course_Scrapper.csv" and "Course_Scrapper.db" 
Note : Do not keep any other csv files in the folder other than the required
## Adding New Semester
Download the Courses Offered in csv format from eacads and save it in the folder, following a similar naming convention. ie 2023-24 Semester 2 would be 2302.csv
## Departments
Currently it works for Circuital and HUL courses, it can easily be extended by editing CourseScrapper.py line 5, add more departments to suit yourself.
```
Departments = ["COL", "ELL", "PYL", "MTL", "HUL","COP","ELP","PYP"]
```
## Results
The name of the professor in the files generated are approximately correct, ie extra spacing before and after the name might cause trouble. This is due to poorly formatted .csv by eacads. To properly use this follow the following commands.
Run the following command to open the database in your terminal.
```
sqlite3 Course_Scrapper.db
```
#### General Info
```
PRAGMA table_info('Course_Scrapper');
```
#### Course/Professor/Slot Specific
```
SELECT Professor FROM Course_Scrapper WHERE Course_Name LIKE '%COL100%';
```
Change the Course_Name to suit you.
Replace Course_Name by Professor, or Slot.

### Updates
Feel free to update it and add features.