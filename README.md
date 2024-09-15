# PA3 🦖
## Problem 1
#### Initalization
1. Import pandas first as pd (or not if you don't want to code).
2. Make sure that the file "cars.csv" is within the same folder as "PA3", or it won't work.
#### a.) Load the corresponding .csv file into a data frame named cars using pandas
1. Declared a variable "cars" as pd.read_csv('cars.csv') which uses the panda function "read" and reads the csv 'cars.csv'.
2. Call 'cars'.
#### b.) Display the first five and last five rows of the resulting cars.
1. Value of the variable 'cars' was already declared at a.).
2. Input cars.head(5), and cars.tail(5) which reads the first, and last five rows of cars.csv, respectively.
   
## Problem 2
#### Initialization
1. Just copied and pasted what I did in the initialization and a.) for Problem 1. We'll do that anyway for the code to begin.
#### a.) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
1. Coded cars[1:11:2] and slice the portions like butter.
2. First input indicates what column it starts in this case, 1; second input (either 10 or 11, just don't make it 9 or 12 or it won't/will include column 9/11) means it stops at column 9; third input sets the gap per shing shing.
#### b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
1. cars.head(1) does that easily since it's the first column of the whole csv.
2. Another input to do this is cars.loc[0]/cars.iloc[0], but why would you do that?
#### c.) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
1. For this one, let's use "cars.iloc[[23],[0,2]]". The input "cars.iloc[23,2]" would suffice for this question, but "cars.iloc[[23],[0,2]]" includes the names "Model", and "cyl" making it look more refined.
2. The panda function ".iloc" locates the row number(s) in the first input, and the second input(s) correspond to what column(s) it would refer to.
#### d.) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
1. Let's use cars.loc[[1,18,28],['Model','cyl','gear']] for this one as .iloc no longer matters to me.
2. The panda function ".iloc" also locates the row number(s) in the first input, but the second input(s) uses names as reference making it easier than .iloc.

## Learnings
1. Panda function is very useful in locating values, though a bit tricky to master at first.
2. Some brackets also change how the output is shown, for example: .iloc / .loc with one less square bracket will not show the names of the columns or not work at all.
3. As learned in the last module: slicing, subsetting and indexing (which i didn't use in my solutions) are all very useful and satisfying to do in my opinion.
4. Dinosaur emoji 🦖

