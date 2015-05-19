#SPOJ Scrapper

[![Join the chat at https://gitter.im/shreyans800755/SPOJ-Scrapper](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/shreyans800755/SPOJ-Scrapper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
To get URL and SPOJ problem number from its name.

[![Build Status](https://travis-ci.org/girishramnani/SPOJ-Scrapper.svg?branch=master)](https://travis-ci.org/girishramnani/SPOJ-Scrapper)

##The feature list:

+ A neat Command line interface. ( #1 )

+ Use of `html Snippets` to find content using contentFinder ( # 1)

+ Persistant storage as a cache for opptimized lookup ( # 1 )

+ `Content finder` is decoupled from the `Snippets` logic so can be used in other websites as well ( #1 )

+ Use of Jinja2 to create a `template` which would be used to store the final output of the question as a text or stripped down HTML (optional).

##Results:

the first iteration of the project is complete

just clone the project ,install the dependencies using `pip3 install -r requirements.txt` and then <br>

`python3 main.py "Aliens"`  and you will get the specific index









<hr>

###GOALS

####Iteration ID:

1) the actual requirement of the project is to create a lookup table to Question_name -> ID the first iteration would contain that much with a neat commandline tool.
<br>
2) i know this application isnt big or does something magical but i have tried to make this project with TDD(also used travis CI) and also i like to make small things big ;->

NOTE: here (#d) means features required to be implemented in the Iteration ID = d.


