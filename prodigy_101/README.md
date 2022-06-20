# Prodigy 101 for Digital Tolkien (and anyone else)

Prodigy is a data annotation tool built by Explosion, the creators of the NLP open-source library spaCy. A few things why you may find Prodigy appealing are:

- Modern web design focused on user experience
- Annotation can be aided by pattern matching and active learning
- Rapid, enjoyable iteration -> Better, faster, scalable annotations
- Helps inspect, clean data and do error analysis 
- The data lives in your computer and is private

Explosion is an open source company, but it does need to pay bills! The way they do it is though Prodigy, which is a paid tool. For more information, visit [https://prodi.gy/](https://prodi.gy/).


## Why use prodigy in Digital Tolkien?

- We have few annotators and want to maximize output
- We want our data to be machine-ready after annotation
- We want our annotations being informed by previous work
- We want to protect copyrighted text
- We want to enjoy our work!


## Walk-though

Follow these steps to install and set up Prodigy in your local machine. Notice that the standard license does not allow you to install this in a web server and make the tool available for other people. There are institutional licenses like the one used by [Purdue university](https://the-examples-book.com/prodigy/introduction) that allow them to have multiple users. If this is your case, you should contact Explosion for more information.

Pre-requisites:

1. A working version of Python 3.6 or above.
2. A valid license key which you can acquire at https://prodi.gy/buy
3. Basic know-how of your computer's [command line interface](https://www.freecodecamp.org/news/command-line-for-beginners/)

Note: It is recommended that you create [separate environments](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) for your Prodigy projects. Here I will assume you have created an environment with `Python 3.9.12`. If you use Conda, you can use the following commands:

```shell
# Create your new environment
conda create -n dt_prodigy101 python=3.9.12
# Activate it
conda activate dt_prodigy101
# Check your Python version
python -V
# The output should be: `>> Python 3.9.12`
```

### I. Installing prodigy

There are two ways:

1. Online using the `pip` command (you will need to use `pip` or `pip3` depending on how your version of Python 3.6+ has been installed). This method requires an internet connection.

```shell
pip install prodigy -f https://XXXX-XXXX-XXXX-XXXX@download.prodi.gy

```

2. Locally (also through the `pip` command). For this you will need to download Prodigy from the email you get after your purchase, unzip the compressed folder, get the path to the uncompressed folder, and use the following command:

```shell
pip install prodigy -f /path/to/unzipped/prodigy/wheels
```

3. Make sure the installation process was successful by running `prodigy stats`:

```shell
prodigy stats

# Output: 
# ============================== ✨  Prodigy Stats ==============================

# Version          1.11.7                        
# Location         /Users/[USRNAME]/opt/miniconda3/envs/dt_prodigy101/lib/python3.9/site-packages/prodigy
# Prodigy Home     /Users/[USRNAME]/.prodigy
# Platform         [YOUR COMPUTER]
# Python Version   3.9.12                        
# Database Name    SQLite                        
# Database Id      sqlite                        
# Total Datasets   0                             
# Total Sessions   0
```


### II. Learning about built-in annotation workflows

Prodigy allows you to use built-in annotation workflows called `recipies`. Some of these include [Named Entity Recognition
](https://prodi.gy/docs/recipes#ner), [Span categorization](https://prodi.gy/docs/recipes#spans), and [Part of speech tagging](https://prodi.gy/docs/recipes#pos). For a complete list visit: https://prodi.gy/docs/recipes

For this tutorial, we will be annotating spans using Prodigy.

There are several components a Prodigy recipe needs. Let's look at the ones for Span Categorization (spancat):

```shell
[1. python -m] [2. prodigy] [3. recipe] [4. name_your_dataset] [5. spacy_pipeline] [6. path_of_data_to_load] [7. optional loader] [8. label names] [9. optional  path to patterns file] [10. optional suggester] [11. optional list of IDs to exclude] [12. highlight characters or tokens]
```

These are the components:

1. python -m
2. prodigy
3. recipe, for example `spans.manual`
4. name of your dataset, for example `test_dataset`
5. spacy pipeline, for example `blank:en`
6. path of the data to load, for example: `./data/gospels.txt`
7. --loader, `str`
8. --label, `str`
9. --patterns, `str`
10. --suggester, `str`
11. --exclude, `str`
12. --highlight-chars, `bool`


### III. Start annotating spans using Prodigy

If you download this repository, you will find a directory structure similar to this:

```
.
├── LICENSE
├── README.md
└── prodigy_101
    ├── README.md
    ├── data
    │   ├── gospels.jsonl
    │   ├── gospels.txt
    │   └── oe_gospels_annotations.jsonl
    ├── prodigy.json
    └── sentence_gospels.py

```

To start annotating, go to the root of the `prodigy_101/` directory and try the Prodigy commands below:

1. Using the paragraphs file `./data/gospels.txt`:

```shell
python -m prodigy spans.manual oe_gospels blank:en ./data/gospels.txt --label ROOT,AFFIX,WORD,MULTI_WORD, --highlight-chars
````

1. Using the sentences file:

```shell
python -m prodigy spans.manual oe_gospels blank:en ./data/gospels.jsonl --label ROOT,AFFIX,WORD,MULTI_WORD, --highlight-chars
````


### IV. Look at the data

If you want to export your annotations to a file instead of having them in Prodigy's SQLite database, you can do:

```shell
prodigy db-out oe_gospels > ./oe_gospels_annotations.jsonl
````

Notice that the format might be odd if you're not using ASCII characters, in which case you can do two things: (a) you can read them into Python using the `json` library and export them again using [UTF8 encoding](https://stackoverflow.com/questions/18337407/saving-utf-8-texts-with-json-dumps-as-utf8-not-as-u-escape-sequence), or (b) leave them as-is. Next time you import them in Prodigy, you will see them normally. For more information, read this [support page](https://support.prodi.gy/t/db-out-utf-8-character-problem/3182/2).

One more thing, if you want to look at which datasets are stored in your database, you can open Python in your terminal and do:

```Python
>>> from prodigy.components.db import connect
>>> db = connect()
>>> all_dataset_names = db.datasets
>>> all_dataset_names
>>> db.close()
```

See [the Prodigy database documentation](https://prodi.gy/docs/api-database) for more information

## Resources

- Anaconda: https://docs.anaconda.com/
- Anaconda (managing environments): https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
- Old English Lemmas (wiktionary): https://en.wiktionary.org/wiki/Category:Old_English_lemmas
- Old English translations: https://www.oldenglishtranslator.co.uk/
- Other Old English resources: https://www.lexilogos.com/english/english_old.htm
- Morphology (Wikipedia): https://en.wikipedia.org/wiki/Morphology_(linguistics)
- Customize your Prodigy workspace: https://prodi.gy/docs/api-web-app
