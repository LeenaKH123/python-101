# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"
file1_resu1t = file_1.split(".")[-1]
file2_result = file_2.split(".")[-1]
file3_result = file_3.split(".")[-1]
file4_result = file_4.split(".").[-1]
files = [file1_result, file2_result, file3_result, file4_result]
