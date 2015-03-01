STEP 1 : Run preprocessing_train.py and preprocessing_test.py

STEP 2 : Create .arff files with the newly created .csv files but simply change the extension of the file and adding this following header to the top of the file.

Header to put at the top of .arff file for Weka : 

------------------------------------
@relation titanic

@attribute Survived {0,1}
@attribute Pclass {1,2,3}
@attribute Sex {male,female}
@attribute Age numeric
@attribute SibSp numeric
@attribute Parch numeric
@attribute Fare numeric
@attribute Embarked {S,C,Q}
@attribute Deck {A,B,C,D,E,F,T,G}
@attribute Title {Mr,Mrs,Miss,Master}
@attribute Familysize numeric
@attribute Age*Class numeric
@attribute FarePerPerson numeric

@data
-------------------------------------

STEP 3 : Open WEKA on the train_preprocessed.arff file.

STEP 4 : Go to "Classify" tab

STEP 5 : Set the class to "Survived" (above the start button)

STEP 6 : Select the algorithm for the classifier : Choose -> meta -> Bagging

STEP 7 : Select the good options for the algorithm by double clicking on the algorithm

STEP 8 : Provide the test set : test_preprocessed.arff file.

STEP 9 : Run the algorithm

STEP 10 : right click on the newly created model in the "Result list" and select "Visualize classifiers error"

STEP 11 : Save in the folder : for instance "bagging_model.arff"

STEP 12 : Run make_kaggle_format.py in order to create a file with the good format for the kaggle submissions.

STEP 13 : Make the submission on the Kaggle platform.

