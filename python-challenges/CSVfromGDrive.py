from io import StringIO
import pandas
csv_link = "https://docs.google.com/spreadsheets/d/..."
data_source = StringIO.StringIO(requests.get(csv_link).content))
    dataframe=pd.read_csv(data_source)
    print(dataframe.head())
