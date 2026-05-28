import os
import pandas as pd
import subprocess

# ============================================================
# LOCAL PATH
# ============================================================

LOCAL_FOLDER = "/home/hdoop/big-data-learning-environment-linux-hadoop/projects/Prediccion-Estancia-Hospitalaria-LOS-Python/Data"

# ============================================================
# HDFS PATH
# ============================================================

HDFS_PATH = "/user/hdoop/hospital/input"

# ============================================================
# GET XLSX FILES
# ============================================================

xlsx_files = [
    f for f in os.listdir(LOCAL_FOLDER)
    if f.endswith(".xlsx")
]

print(f"Found {len(xlsx_files)} Excel files")

# ============================================================
# PROCESS EACH FILE
# ============================================================

for file_name in xlsx_files:

    print("=" * 50)
    print(f"Processing: {file_name}")

    # Full XLSX path
    xlsx_path = os.path.join(LOCAL_FOLDER, file_name)

    # CSV filename
    csv_name = file_name.replace(".xlsx", ".csv")

    # Full CSV path
    csv_path = os.path.join(LOCAL_FOLDER, csv_name)

    # ========================================================
    # READ EXCEL
    # ========================================================

    df = pd.read_excel(xlsx_path)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    # ========================================================
    # SAVE CSV
    # ========================================================

    df.to_csv(csv_path, index=False)

    print(f"CSV created: {csv_path}")

    # ========================================================
    # REMOVE OLD FILE FROM HDFS
    # ========================================================

    subprocess.run(
        f"hdfs dfs -rm -f {HDFS_PATH}/{csv_name}",
        shell=True
    )

    # ========================================================
    # UPLOAD TO HDFS
    # ========================================================

    upload_command = f"hdfs dfs -put {csv_path} {HDFS_PATH}/"

    result = subprocess.run(
        upload_command,
        shell=True
    )

    if result.returncode == 0:
        print(f"Uploaded to HDFS: {csv_name}")
    else:
        print(f"Failed upload: {csv_name}")

print("=" * 50)
print("Pipeline Completed Successfully")
