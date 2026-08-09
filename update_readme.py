import datetime
import re

# Your birthdate
birth_date = datetime.date(2007, 4, 13)
today = datetime.date.today()

# Calculate exact age
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
current_year = today.year

# Read the current README.md
with open('README.md', 'r', encoding='utf-8') as file:
    content = file.read()

# 1. Update the hidden HTML tags in the "About Me" and "Footer" sections
content = re.sub(r'<!-- AGE -->\d+<!-- /AGE -->', f'<!-- AGE -->{age}<!-- /AGE -->', content)
content = re.sub(r'<!-- YEAR -->\d+<!-- /YEAR -->', f'<!-- YEAR -->{current_year}<!-- /YEAR -->', content)

# 2. Update the Animated Typing SVG URL
# This finds "lines=19+year+old" and updates the number automatically
content = re.sub(r'lines=\d+\+year\+old', f'lines={age}+year+old', content)

# Write the updated text back to the file
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(content)

print(f"Updated README with Age: {age} and Year: {current_year}")
