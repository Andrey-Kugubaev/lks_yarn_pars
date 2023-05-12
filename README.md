# Parser of link

---
![python](https://img.shields.io/badge/Python-3.10.4-green)
![Scrapy](https://img.shields.io/badge/Scrapy-2.9.0-green)
![flake8](https://img.shields.io/badge/flake8-6.0.0-green)
---
## Contents:
- [Introduction](#introduction)
- [Parsing links](#parsing-links)
- [Instruction to start](#instruction-to-start)

---
### <anchor>Introduction</anchor>
The project to write web page parser using Scrapy.
The project implements a parser for collecting links

----
### <anchor>Parsing links</anchor>
The parser collects information (Title, Link) from https://www.yarndatabase.com/
 and saves in _json_ file.
The format of file name: _knits_list.json_

----
### <anchor>Instruction to start</anchor>
<details>

1. Clone the repository to the local machine
`git clone git@github.com:Andrey-Kugubaev/lks_yarn_pars.git`
2. Install and activate the virtual environment
`python -m venv venv` or `python3 -m venv venv`,
then `source venv/Scripts/activate` or `source venv/bin/activate`
3. Install Dependencies `pip install -r requirements.txt`
4. Run parsers `scrapy crawl yarnd`

</details>