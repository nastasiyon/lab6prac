import configparser
import os
from file_ops import FileOperations
from utils import validate_path, get_absolute_path

class FileManager:
    def __init__(self):
        # Load configuration
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.working_dir = config['Settings']['working_directory']
        if not os.path.exists(self.working_dir):
            os.makedirs(self.working_dir)
        self.current_dir = self.working_dir
        self.file_ops = FileOperations(self.working_dir)

    def run(self):
        print("Simple File Manager. Type 'help' for commands.")
        while True:
            try:
                prompt = f"{self.current_dir}> "
                command = input(prompt).strip().split()
                if not command:
                    continue
                cmd = command[0].lower()
                args = command[1:]

                if cmd == 'help':
                    self.show_help()
                elif cmd == 'ls':
                    self.file_ops.list_directory(self.current_dir)
                elif cmd == 'cd':
                    self.change_directory(args)
                elif cmd == 'mkdir':
                    self.file_ops.create_directory(self.current_dir, args)
                elif cmd == 'rmdir':
                    self.file_ops.remove_directory(self.current_dir, args)
                elif cmd == 'touch':
                    self.file_ops.create_file(self.current_dir, args)
                elif cmd == 'cat':
                    self.file_ops.read_file(self.current_dir, args)
                elif cmd == 'write':
                    self.file_ops.write_file(self.current_dir, args)
                elif cmd == 'rm':
                    self.file_ops.remove_file(self.current_dir, args)
                elif cmd == 'cp':
                    self.file_ops.copy_file(self.current_dir, args)
                elif cmd == 'mv':
                    self.file_ops.move_file(self.current_dir, args)
                elif cmd == 'rename':
                    self.file_ops.rename_file(self.current_dir, args)
                elif cmd == 'exit':
                    print("Exiting File Manager.")
                    break
                else:
                    print(f"Unknown command: {cmd}. Type 'help' for commands.")
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")
            except Exception as e:
                print(f"Error: {e}")

    def show_help(self):
        print("""
Available Commands:
  ls                    - List files and directories
  cd <path>             - Change current directory
  mkdir <name>          - Create a new directory
  rmdir <name>          - Remove a directory
  touch <name>          - Create an empty file
  cat <name>            - Read file contents
  write <name> <text>   - Write text to a file
  rm <name>             - Remove a file
  cp <src> <dst>        - Copy a file
  mv <src> <dst>        - Move a file
  rename <old> <new>    - Rename a file
  exit                  - Exit the file manager
  help                  - Show this help
        """)

    def change_directory(self, args):
        if len(args) != 1:
            print("Usage: cd <path>")
            return
        new_path = get_absolute_path(self.current_dir, args[0])
        if validate_path(new_path, self.working_dir):
            if os.path.isdir(new_path):
                self.current_dir = new_path
            else:
                print("Error: Not a directory or does not exist.")
        else:
            print("Error: Cannot navigate outside working directory.")

if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.run()