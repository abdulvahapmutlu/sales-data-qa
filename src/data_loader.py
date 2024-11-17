import os
import pandas as pd

def load_excel_files(directory):
    """
    Load and preprocess all Excel files in the directory.
    """
    data_frames = []
    for filename in os.listdir(directory):
        if filename.endswith(('.xlsx', '.xls')):
            file_path = os.path.join(directory, filename)
            try:
                df = pd.read_excel(file_path)
                df['source_file'] = filename
                data_frames.append(df)
                print(f"Loaded '{filename}' successfully.")
            except Exception as e:
                print(f"Error reading '{file_path}': {e}")
    if data_frames:
        combined_df = pd.concat(data_frames, ignore_index=True)
        combined_df['combined_text'] = combined_df.astype(str).agg(' '.join, axis=1)
        return combined_df
    else:
        raise ValueError("No valid Excel files found.")
