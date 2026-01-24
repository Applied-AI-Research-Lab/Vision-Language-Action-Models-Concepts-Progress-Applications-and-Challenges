import bibtexparser
import os

# Read the bib file from parent directory
# Disable string interpolation to avoid errors with unquoted abbreviations like ICCV
parser = bibtexparser.bparser.BibTexParser(interpolate_strings=False)

with open('paper/example.bib', 'r') as f:
    bib_database = bibtexparser.load(f, parser=parser)

# Group entries by year
years = {}
for entry in bib_database.entries:
    year = entry.get('year', 'Unknown')
    if year not in years:
        years[year] = []
    years[year].append(entry)

# For each year, create a markdown file in current directory
for year, entries in sorted(years.items(), reverse=True):
    filename = f'paper_list_{year}.md'
    with open(filename, 'w') as f:
        f.write(f'# Paper List {year}\n\n')
        f.write('### Follow-up Papers\n\n')
        for entry in entries:
            title = entry.get('title', 'Unknown Title').strip('{}')
            authors = entry.get('author', 'Unknown Authors').replace(' and ', ', ')
            journal = entry.get('journal', entry.get('booktitle', 'Unknown Venue'))
            year_pub = entry.get('year', 'Unknown Year')
            entry_id = entry.get('ID', 'unknown')
            
            # Format similar to the example
            f.write(f'- **{entry_id}:** {authors}.<br />\n')
            f.write(f'  "{title}." {journal} ({year_pub}).\n\n')
            # Add [year] at the end
            f.write(f'  [{year_pub}]\n\n')

print("Markdown files generated.")