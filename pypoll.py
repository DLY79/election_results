# # # file_to_load = os.path.join("resources", "election_results.csv")
# # # with open(file_to_load) as election_data:
# # #    print(election_data)
    
# # #     file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # #     outfile = open(file_to_save, "w")
# # #     outfile.write("Hello World")
# # #     outfile.close()
# # # file_to_save = os.path.join("analysis", "election_analysis.txt")
# # # with open(file_to_save, "w") as txt_file:
# # #     txt_file.write("Hello Squirrel, ")
# # #     txt_file.write("\nArapahoe, ")
# # #     txt_file.write("Denver, ")
# # #     txt_file.write("Jefferson.")
# # # import csv
# # # import os
# # # file_to_load = os.path.join("Resources", "election_results.csv")
# # # file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # # with open(file_to_load) as election_data:
# # #     file_reader = csv.reader(election_data)
# # # for row in file_reader:
# # #     print(row)
    
                            
                                
# # import csv
# # import os

# # file_to_load = os.path.join("Resources", "election_results.csv")
# # file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # total_votes = 0
# # candidate_options = []

# # candidate_votes = {}
# # winning_candidate = ""
# # winning_count = 0
# # winning_percentage = 0
# # with open(file_to_load) as election_data:
# #     file_reader = csv.reader(election_data)
    
# #     headers =next(file_reader)
    
# #     for row in file_reader:
# #         total_votes += 1
        
# #         candidate_name = row[2]
        
# #         if candidate_name not in candidate_options:
# #             candidate_options.append(candidate_name)
            
# #             candidate_votes[candidate_name] = 0
            
# #         candidate_votes[candidate_name] += 1
# #     with open(file_to_save, "w") as txt_file:
# #         election_results = (
# #         f"\nElection Results\n"
# #         f"-------------------------\n"
# #         f"Total Votes: {total_votes:,}\n"
# #         f"-------------------------\n")
# #     print(election_results, end="")
# #     # Save the final vote count to the text file.
# #     txt_file.write(election_results)
        
# #     for candidate_name in candidate_votes:
# #         votes = candidate_votes[candidate_name]
# #         vote_percentage = float(votes) / float(total_votes) * 100
# #         # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# #         if (votes > winning_count) and (vote_percentage > winning_percentage):
        
                    
# #             winning_count = votes
# #             winning_percentage = vote_percentage
# #             winning_candidate = candidate_name
# #             #  print(f"{candidate_name}: received {vote_percentage:.1f}%  of the vote.")
# #         winning_candidate_summary = (
# #         f"-------------------------\n"
# #         f"Winner: {winning_candidate}\n"
# #         f"Winning Vote Count: {winning_count:,}\n"
# #         f"Winning Percentage: {winning_percentage:.1f}%\n"
# #         f"-------------------------\n")
# #     # print(winning_candidate_summary)
                            
# #     # print(candidate_options)
            
# #     # print(total_votes)

# #     # print(candidate_votes)
        
# #         # headers = next(file_reader)
# #         # print(headers)
            
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Initialize a total vote counter.
# total_votes = 0
# # Candidate options and candidate votes
# candidate_options = []
# candidate_votes = {}
# # Track the winning candidate, vote count, and percentage.
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read the header row.
#     headers = next(file_reader)
#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1
#         # Get the candidate name from each row.
#         candidate_name = row[2]
#         # If the candidate does not match any existing candidate add it the
#         # the candidate list.
#         if candidate_name not in candidate_options:
#             # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)
#             # And begin tracking that candidate's voter count.
#             candidate_votes[candidate_name] = 0
#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1
#         # Save the results to our text file.
#     with open(file_to_save, "w") as txt_file:
#             # Print the final vote count to the terminal.
#         election_results = (
#             f"\nElection Results\n"
#             f"-------------------------\n"
#             f"Total Votes: {total_votes:,}\n"
#             f"-------------------------\n")
#         print(election_results, end="")
#     # Save the final vote count to the text file.
#         txt_file.write(election_results)

#     for candidate_name in candidate_votes:
#         # Retrieve vote count and percentage.
#         votes = candidate_votes[candidate_name]
#         vote_percentage = float(votes) / float(total_votes) * 100
#         # Print each candidate, their voter count, and percentage to the
#         # terminal.
#         candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
#         # Determine winning vote count, winning percentage, and candidate.
#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             winning_count = votes
#             winning_candidate = candidate_name
#             winning_percentage = vote_percentage
#     # Print the winning candidates' results to the terminal.
#     winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")

#     #print(winning_candidate_summary)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)