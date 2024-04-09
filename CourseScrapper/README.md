# Course Scrapper

## Run

```bash
python3 CourseScrapper.py
```

It generates a .csv file and a .db file named "Course_Scrapper.csv" and "Course_Scrapper.db", respectively. Note: Ensure no other CSV files exist in the folder except the required ones.

## Adding New Semester

Download the "Courses Offered" file in CSV format from eacads and save it in the folder data. Follow a similar naming convention, e.g., for the 2023-24 Semester 2, name the file `2302.csv`.

## Departments

Currently, it works for Circuital and HUL courses. You can extend it by editing `CourseScrapper.py`. Add more departments as needed:

```python
Departments = ["COL", "ELL", "PYL", "MTL", "HUL", "COP", "ELP", "PYP"]
```

## Results

The tool extracts professor names from poorly formatted CSV files by eacads, which may include extra spacing around the names. To use the generated files effectively, follow these commands:

### Accessing the SQLite Database

Run the following command to open the database in your terminal:

```bash
sqlite3 Course_Scrapper.db
```

### General Information

To view the table structure, execute:

```sql
PRAGMA table_info('Course_Scrapper');
```

### Course/Professor/Slot Specific Queries

To query specific information about a course, professor, or slot, use the following syntax:

```sql
SELECT Professor FROM Course_Scrapper WHERE Course_Name LIKE '%COL100%';
```

Replace `Course_Name` with the desired course code. You can also query by `Professor` or `Slot`.

## Updates

Feel free to contribute to this tool by adding features or improving the README.md file.
