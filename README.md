# DATA CHALLENGE

Giulia Verdi and Marco Bianchi are entrepreneurs who manage a chain of stores specializing in products for creative japanese hobbyists and collectors, called "IdeaStore." Thanks to innovative strategies like periodic promotions, IdeaStore quickly became a leading name in the industry, with locations in various Italian cities.

However, this growth has also brought challenges. With the increase in customers, there has been a rise in incidents of payment defaults and fraud. To address the issue, the owners decided to abolish the option of purchasing with deferred payment. While this decision reduced cases of default, it also led to a decline in satisfaction among some loyal customers, resulting in a significant drop in revenue.

A preliminary analysis showed that approximately 1 in 20 creditworthy customers, after being denied deferred payment, reduced their average spending by €30. To address this, the owners collected data on customers who had previously used deferred payment and documented any instances of default.

The goal is to develop a model capable of automating the decision-making process, helping the owners assess whether or not to grant credit to new customers based on the data collected.

# CODING CHALLENGE

Another ambitious project by the entrepreneurs Giulia Verdi and Marco Bianchi is the development of "MoverBot," a technological robot designed to automate and speed up the process of moving heavy stacks of collectible items within a store.

The entrepreneurs envision representing a store as an 8x8 matrix, where each cell's value indicates whether that specific area of the store is empty (" "), occupied by a wall ("W"), a stack of items ("S"), a display column for action figures ("D"), or a checkout counter ("C").

After learning the layout of the store, a starting cell, and a target cell, MoverBot should move—if possible—between the two cells using the fewest moves. Giulia and Marco consider it essential for MoverBot to move exactly like a knight in chess: two steps horizontally (or vertically), followed by one step vertically (or horizontally), forming an "L"-shaped path. This movement allows MoverBot to "jump" over occupied cells, provided it does not land on one.

As a preliminary test, the entrepreneurs want MoverBot to be programmed for a specific store layout and tasked with finding the shortest path between two cells in that layout. Later, they plan to require MoverBot to adapt to various arrangements of walls, stacks, display columns, and checkout counters.

It is specified that the positions of the cells in the matrix should be identified by integers ranging from 0 to 63, following this scheme:

lst_index = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]
The specific store configuration for the first test is given as follows:

lst_current_store = [
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    [" ", "S", " ", " ", "S", " ", " ", "S"],
    ["D", "S", " ", "D", "S", " ", "D", "S"],
    [" ", "S", " ", " ", "S", " ", " ", "S"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "S", " ", " ", "S", " ", " ", "S"],
    ["D", "S", " ", "D", "S", " ", "D", "S"],
    [" ", "S", "C", " ", "S", "C", " ", "S"]
]

# SOLUTIONS

In the repository, you will find the following files:

0. test.csv, train.csv and DataDictionary.xls

files for training and testing the classifiers plus the Data Dictionary for variables description.

1. Preprocessing_DataChallenge_Train_1stPart.ipynb
  
This notebook contains the first part of the preprocessing for the dataset, including:

- Data cleaning.
- Imputation of missing values.
- Evaluation of outliers.
- Encoding of variables.
  
2. Preprocessing_DataChallenge_Train_2ndPart.ipynb
   
This notebook includes the second part of the preprocessing for the dataset, focusing on:

- Deepening the descriptive analysis, partially introduced in the first part.
- Feature selection.
  
3. Processed CSV Files:

- processed_df_train_1stpart.csv: Output of the first part of the preprocessing for the training dataset.
- processed_df_train_2ndpart.csv: Output of the second part of the preprocessing for the training dataset.
- processed_df_test_1stpart.csv: Output of the first part of the preprocessing for the test dataset.
- processed_df_test_2ndpart.csv: Output of the second part of the preprocessing for the test dataset.
  
4. Classifiers_Data_Challenge.ipynb
   
This notebook contains the implementation of the classifiers and their application to the provided test dataset.

5. test_predicted.csv
   
A CSV file with the final predictions

6. solution_coding_challenge.py
   
A Python script containing the solution for the Coding Challenge.
