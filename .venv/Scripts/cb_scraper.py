import re
from win32 import win32clipboard as clip



chunk_compile = re.compile(r"Detailed Forecast\n.*\n+?(?=Additional Forecasts and Information)",re.DOTALL)
chunk_list = re.findall(chunk_compile,clip)
for template in chunk_list:
    template_rows = template.split('\n')
    for row in template_rows:
        print(row)

