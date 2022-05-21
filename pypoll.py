# file_to_load = os.path.join("resources", "election_results.csv")
# with open(file_to_load) as election_data:
#    print(election_data)
    
#     file_to_save = os.path.join("Analysis", "election_analysis.txt")
#     outfile = open(file_to_save, "w")
#     outfile.write("Hello World")
#     outfile.close()
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Hello Squirrel, ")
#     txt_file.write("\nArapahoe, ")
#     txt_file.write("Denver, ")
#     txt_file.write("Jefferson.")
# import csv
# import os
# file_to_load = os.path.join("Resources", "election_results.csv")
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
# for row in file_reader:
#     print(row)
    
                            
                                
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    print(headers)
          
        