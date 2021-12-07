# Stepic: Automated testing using Selenium and Python

This repo contains the source code for [Unit 3.6 step 9](https://stepik.org/lesson/237240/step/9?unit=209628) of the course.

To run this repo, please use following instructions:

1. Install virtual environmemt:
```
python -m venv venv
```

2. Activate environment:
```shell
source venv/bin/activate
```

3. Install requirements:
```shell
pip install -r requirements.txt
```

4. Download chromedriver to the root folder of the repo

5. Run the programm using the following command:
```shell
python --language=[YOUR LANGUAGE] test_items.py
```

The script will open the [link](http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/), on specified language and check wether add to basket button is present.
