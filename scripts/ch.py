file_name = input("Enter chapter name > ")
ch_num = input("Enter chapter number > ")

if file_name[:3] != ".md":
    file_name += ".md"

with open(file_name, "x") as file:
    ch_name = file_name.replace('.md', '')
    file.write(f"# Chapter {ch_num}: {ch_name}")
