import os
import shutil

def delete_folder(folder_path):
    # Safety check
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    confirm = input(f"Are you sure you want to delete '{folder_path}'? (yes/no): ")
    if confirm.lower() == 'yes':
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
    else:
        print("Operation cancelled.")

# Example usage
delete_folder("/home/ec2-user/old_project")

print("no errorr")
