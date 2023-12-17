first load the dataset into the `data/` folder.

then go to the root of project and run the following commands

```bash
pypy3 -m pip install termcolor
cd src/
pypy3 wordlist_generator.py
pypy3 tfidf_per_doc.py
pypy3 main.py "{location of data.json}"
```


do not remember to set the test limit in file `main.py`.
now continue to work on the project.