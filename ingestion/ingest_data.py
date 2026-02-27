import os
import pandas as pd
import logging

logging.basicConfig(
    filename="ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ingest_file(file_path, staging_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, on_bad_lines="skip")
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path, lines=True)
        else:
            raise ValueError("Unsupported file format")

        os.makedirs(staging_path, exist_ok=True)
        file_name = os.path.basename(file_path)
        df.to_csv(os.path.join(staging_path, file_name), index=False)

        logging.info(f"Successfully ingested {file_name}")

    except Exception as e:
        logging.error(f"Failed to ingest {file_path}: {str(e)}")

if __name__ == "__main__":
    ingest_file("data/raw/products.csv", "data/staging/products/")
    ingest_file("data/raw/sales.csv", "data/staging/sales/")
    ingest_file("data/raw/inventory.csv", "data/staging/inventory/")
