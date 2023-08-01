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
