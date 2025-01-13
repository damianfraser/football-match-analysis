import kagglehub

# Download latest version of the dataset
path = kagglehub.dataset_download("hugomathien/soccer")

print("Path to dataset files:", path)
