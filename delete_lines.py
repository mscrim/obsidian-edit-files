import glob
import emoji

# Use emoji.emojize if your path contains emojis
# List of emoji CLDR names is at https://unicode.org/emoji/charts/emoji-list.html
path = emoji.emojize("/Users/user/Documents/Obsidian/My Vault/:sun: Daily")
# Specify any files you want to exclude from editing
files_to_exclude = ['2021-04-26.md']

# Specify lines to delete - needs \n at the end
lines_to_delete = [
   '[[To-Do List]] | [[Reminders]]\n'
]


def del_lines(filename, lines_to_delete):
    with open(filename, "r") as f:
        lines = f.readlines()
        # lines: list of strings

    edit = False
    for line in lines_to_delete:
        if line in lines:
            lines.remove(line)
            edit = True

    if edit:
        print('Updating {}'.format(filename))
        with open(filename, "w") as f:
            for line in lines:
                f.write(line)
            f.truncate()


for filename in glob.glob(path + '/*.md'):
    if filename not in files_to_exclude:
        del_lines(filename, lines_to_delete)
