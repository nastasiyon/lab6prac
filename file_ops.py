import os
import shutil
from utils import validate_path, get_absolute_path

class FileOperations:
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def list_directory(self, current_dir):
        try:
            entries = os.listdir(current_dir)
            for entry in entries:
                full_path = os.path.join(current_dir, entry)
                if os.path.isdir(full_path):
                    print(f"[DIR] {entry}")
                else:
                    print(f"[FILE] {entry}")
        except Exception as e:
            print(f"Error listing directory: {e}")

    def create_directory(self, current_dir, args):
        if len(args) != 1:
            print("Usage: mkdir <name>")
            return
        dir_path = get_absolute_path(current_dir, args[0])
        if validate_path(dir_path, self.working_dir):
            try:
                os.makedirs(dir_path, exist_ok=True)
                print(f"Directory '{args[0]}' created.")
            except Exception as e:
                print(f"Error creating directory: {e}")
        else:
            print("Error: Cannot create directory outside working directory.")

    def remove_directory(self, current_dir, args):
        if len(args) != 1:
            print("Usage: rmdir <name>")
            return
        dir_path = get_absolute_path(current_dir, args[0])
        if validate_path(dir_path, self.working_dir):
            try:
                shutil.rmtree(dir_path)
                print(f"Directory '{args[0]}' removed.")
            except FileNotFoundError:
                print("Error: Directory does not exist.")
            except Exception as e:
                print(f"Error removing directory: {e}")
        else:
            print("Error: Cannot remove directory outside working directory.")

    def create_file(self, current_dir, args):
        if len(args) != 1:
            print("Usage: touch <name>")
            return
        file_path = get_absolute_path(current_dir, args[0])
        if validate_path(file_path, self.working_dir):
            try:
                with open(file_path, 'a'):
                    os.utime(file_path, None)
                print(f"File '{args[0]}' created.")
            except Exception as e:
                print(f"Error creating file: {e}")
        else:
            print("Error: Cannot create file outside working directory.")

    def read_file(self, current_dir, args):
        if len(args) != 1:
            print("Usage: cat <name>")
            return
        file_path = get_absolute_path(current_dir, args[0])
        if validate_path(file_path, self.working_dir):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    print(content)
            except FileNotFoundError:
                print("Error: File does not exist.")
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print("Error: Cannot read file outside working directory.")

    def write_file(self, current_dir, args):
        if len(args) < 2:
            print("Usage: write <name> <text>")
            return
        file_path = get_absolute_path(current_dir, args[0])
        text = ' '.join(args[1:])
        if validate_path(file_path, self.working_dir):
            try:
                with open(file_path, 'w') as f:
                    f.write(text)
                print(f"Text written to '{args[0]}'.")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("Error: Cannot write to file outside working directory.")

    def remove_file(self, current_dir, args):
        if len(args) != 1:
            print("Usage: rm <name>")
            return
        file_path = get_absolute_path(current_dir, args[0])
        if validate_path(file_path, self.working_dir):
            try:
                os.remove(file_path)
                print(f"File '{args[0]}' removed.")
            except FileNotFoundError:
                print("Error: File does not exist.")
            except Exception as e:
                print(f"Error removing file: {e}")
        else:
            print("Error: Cannot remove file outside working directory.")

    def copy_file(self, current_dir, args):
        if len(args) != 2:
            print("Usage: cp <source> <destination>")
            return
        src_path = get_absolute_path(current_dir, args[0])
        dst_path = get_absolute_path(current_dir, args[1])
        if validate_path(src_path, self.working_dir) and validate_path(dst_path, self.working_dir):
            try:
                shutil.copy2(src_path, dst_path)
                print(f"File copied from '{args[0]}' to '{args[1]}'.")
            except FileNotFoundError:
                print("Error: Source file does not exist.")
            except Exception as e:
                print(f"Error copying file: {e}")
        else:
            print("Error: Cannot copy files outside working directory.")

    def move_file(self, current_dir, args):
        if len(args) != 2:
            print("Usage: mv <source> <destination>")
            return
        src_path = get_absolute_path(current_dir, args[0])
        dst_path = get_absolute_path(current_dir, args[1])
        if validate_path(src_path, self.working_dir) and validate_path(dst_path, self.working_dir):
            try:
                shutil.move(src_path, dst_path)
                print(f"File moved from '{args[0]}' to '{args[1]}'.")
            except FileNotFoundError:
                print("Error: Source file does not exist.")
            except Exception as e:
                print(f"Error moving file: {e}")
        else:
            print("Error: Cannot move files outside working directory.")

    def rename_file(self, current_dir, args):
        if len(args) != 2:
            print("Usage: rename <old_name> <new_name>")
            return
        old_path = get_absolute_path(current_dir, args[0])
        new_path = get_absolute_path(current_dir, args[1])
        if validate_path(old_path, self.working_dir) and validate_path(new_path, self.working_dir):
            try:
                os.rename(old_path, new_path)
                print(f"File renamed from '{args[0]}' to '{args[1]}'.")
            except FileNotFoundError:
                print("Error: Source file does not exist.")
            except Exception as e:
                print(f"Error renaming file: {e}")
        else:
            print("Error: Cannot rename files outside working directory.")