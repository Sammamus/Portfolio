import json

large_file_path = "/Users/darianraffle/Downloads/eff_large_wordlist.txt"
general_short_file_path = "/Users/darianraffle/Downloads/eff_short_wordlist_1.txt"
short_file_path = "/Users/darianraffle/Downloads/eff_short_wordlist_2_0.txt"

short_names = {
    "/Users/darianraffle/Downloads/eff_large_wordlist.txt": "large",
    "/Users/darianraffle/Downloads/eff_short_wordlist_1.txt": "general_short",
    "/Users/darianraffle/Downloads/eff_short_wordlist_2_0.txt": "short"
}

# - Pull list
compiled_output = {}

files = [
    large_file_path,
    general_short_file_path,
    short_file_path
]

for file_path in files:
    designator = short_names[file_path]
    compiled_output[designator] = {}
    with open(file_path) as f:
        for line in f:
            words = line.split()
            compiled_output[designator][words[0]] = words[-1]
    f.close()

with open("word_dictionaries.json", "w") as outfile:
    json.dump(compiled_output, outfile)

outfile.close()
# - Read line by line
# - Break each line and take index 0 as key and index -1 as value
# - assign key and value to dictionary
# - save dictionary to a json file.