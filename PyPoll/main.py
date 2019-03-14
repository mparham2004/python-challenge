import pandas as pd

# Reference the file where the CSV is located
election_csv_path = "../Resources/election_data.csv"

# Import the data into a Pandas DataFrame
election_df = pd.read_csv(election_csv_path)
election_df.head()


#calculate a values showing:
# Total number of votes cast
# List of candidates who got votes
# % of votes by  candidate
# Total votes by candidate
# Winner based on popular vote

Results = election_df["Candidate"].value_counts()
print ("")
print ("Election Results")
print ("-------------------------------")
print("Total Votes: ")
print(Results.sum())

Results = election_df["Candidate"].value_counts()
print(Results.head())

print ("-------------------------------")
print ("List by candidate: $")
print ("-------------------------------")
print ("Winner: ")
print ("-------------------------------")



with open("main_text_file.txt",'w',encoding = 'utf-8') as f:
   f.write("main_text_file\n")
   f.write("print path test")

   

