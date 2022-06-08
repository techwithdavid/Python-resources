from datetime import datetime
import re

#method 1
def transform_date_format(date):
   return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)


date_input = "2021-08-01"
print(transform_date_format(date_input))

#method 2
new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d:%m:%Y")
print(new_data)
