import os
import requests
from tqdm import tqdm

# GGUF model URL (example — update with the correct one if different)
url = "https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q4_K_M.gguf"

# Target path
output_dir = "models"
output_file = os.path.join(output_dir, "deepseek-coder-6.7b-instruct.Q4_K_M.gguf")

# Make directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Download with progress bar
def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(dest_path, "wb") as f, tqdm(
        desc=dest_path,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

download_file(url, output_file)
print(f"✅ Downloaded to {output_file}")
