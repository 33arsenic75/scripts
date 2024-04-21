# Moodle Course Material Downloader

This script allows you to download course materials from Moodle, a popular online learning platform. You can specify various options such as downloading all documents, a specific number of documents, documents from the beginning or end of the list, listing all available documents, and specifying a folder to save the downloads.

## Usage

```bash
python moodle_downloader.py [-h] [-a ALLDOCUMENT] [-n NUMBEROFDOCUMENTS] [-b] [-e] [-show] [-f FOLDER]
```

#### How to add a course ?

Open course_id.json and add the key-value pair for the new course. If you dont want to use Course Name, you can always use Course Id without adding anything to course_id.json.

## Installation

```bash
pip install -r requirements
```

## Example

#### Download all documents from a course:

```bash
python moodle_downloader.py -a all
```

#### Download the first 5 documents from a course:

```bash
python moodle_downloader.py -n 5 -b
```

#### Download the last 5 documents from a course:

```bash
python moodle_downloader.py -n 5 -l
```

#### List all available documents without downloading:

```bash
python moodle_downloader.py -show
```

#### Download documents and save them to a specific folder:

```bash
python moodle_downloader.py -f "Course Materials"
```

## Trust?

_can you be trusted? What if you are stealing my passwords?_

Read the source code. If you still dont trust, dont use it. Simple.

## Copyleft

_can I copy this?_

This is my intellectual property, original creation, and is copylefted. Use it for anything, but be warned that I am not liable, in any way, for any misuse, real or perceived, of this code.

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).
