import os

def merge_files_in_directory(directory):
    # Get list of files in directory
    files = os.listdir(directory)
    
    # Filter out directories
    files = [file for file in files if os.path.isfile(os.path.join(directory, file))]
    
    # Ensure there are at least two files to merge
    if len(files) < 2:
        print(f"Not enough files to merge in directory: {directory}")
        return
    
    # Merge the first two files
    file1 = files[0]
    file2 = files[1]
    merged_file_path = os.path.join(directory, f"{os.path.splitext(file1)[0]}_{os.path.splitext(file2)[0]}_merged.txt")
    
    with open(os.path.join(directory, file1), 'r') as f1, open(os.path.join(directory, file2), 'r') as f2, open(merged_file_path, 'w') as merged_file:
        merged_file.write(f1.read())
        merged_file.write(f2.read())
    
    # Delete the original files
    os.remove(os.path.join(directory, file1))
    os.remove(os.path.join(directory, file2))
    
    print(f"Files merged successfully and original files deleted: {file1}, {file2} => {merged_file_path}")

def merge_files_in_parent_directory(parent_directory):
    # Get list of subdirectories
    subdirectories = [os.path.join(parent_directory, directory) for directory in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, directory))]
    
    # Merge files in each subdirectory
    for directory in subdirectories:
        merge_files_in_directory(directory)

if __name__ == "__main__":
    parent_directory = input("Enter the parent directory path: ")
    merge_files_in_parent_directory(parent_directory)
