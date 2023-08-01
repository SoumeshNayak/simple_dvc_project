git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"

dvc repro

dvc metrics diff

dvc metrics show

NOTE:
in dvc.yaml:
in test_and_evaluate for windows 
metrics:
    - report\params.json:
        cache: false
    - report\scores.json:
        cache: false

pip install -e . After making setup.py to install dependency        

tox command:
tox
tox for rebuilding:
tox -r

pytest command:
pytest -v

flake8 for cleaner code and check error
     stop the build if there are Python syntax errors or undefined names
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
     flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
