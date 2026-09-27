import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download(
    "selonamaris/large-industrial-pump-maintenance-dataset"
)

print("Path to dataset files:", path)