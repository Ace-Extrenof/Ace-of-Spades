ch_num = input("Enter chapter number > ")
ch_name = input("Enter chapter name > ")

file_name = f"chapter{ch_num}.md"

with open(file_name, "x") as file:
    file.write(f"# Chapter {ch_num}: {ch_name}")
