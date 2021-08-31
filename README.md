The project uses three libraries: regex, time, and csv.

The project reads the sample data file line by line. It then loops through all the data while searching for specifc pieces of data from the dataset. This is done with the search attribute. Furthermore, the patterns are specific in which they only access the data intended. The loop then adds all the data to a list under the variable name named "row".

That data is then added line by line to the list under the variable name "data".

By using `with open("data.csv", mode="w") as file`, a file named data.csv is opened. If the csv file did not previously exist it will then create one. All the data is written row by row into that csv. 
