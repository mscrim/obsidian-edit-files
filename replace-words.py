""" Replace words in Markdown files.
    E.g. replace all tags #dailyjournal with a new tag #journal
"""
import os
import glob
import emoji

# Use emoji.emojize if your path contains emojis
# List of emoji CLDR names is at https://unicode.org/emoji/charts/emoji-list.html
path = emoji.emojize("/Users/user/Documents/Obsidian/My Vault/:sun: Daily")

# Define the text to replace, and new text
text_to_replace = "#dailyjournal"
new_text = "#journal"

def replace_text_in_file(filename, text_to_replace, new_text):
    with open(filename, 'r+') as f:
        
        #read file
        file_source = f.read()

        if text_to_replace in file_source:
        
            #replace old text with next text in the file
            replace_string = file_source.replace(text_to_replace, new_text)
            
            #save output
            f.write(replace_string)

            print('Replaced {} with {} in file {}'.format(text_to_replace, new_text, filename))


for filename in glob.glob(path + '/*.md'):
    replace_text_in_file(filename, text_to_replace, new_text)