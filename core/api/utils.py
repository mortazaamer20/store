import pandas as pd
from .models import Product  # Replace with your actual model

def process_excel_file(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Ensure required columns exist
        required_columns = {'name_EN', 'name_AR', 'description_EN', 'description_AR'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

        # Iterate over rows and create instances
        for index, row in df.iterrows():
            Product.objects.create(
                        name_EN=row['name_EN'],
                        name_AR=row['name_AR'],
                        description_EN=row['description_EN'],
                        description_AR=row['description_AR']
            )

    except Exception as e:
        print(f"Error processing Excel file: {e}")
        raise e
