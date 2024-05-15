import os
import zipfile
import time

if str(os.getcwd()).endswith("system32"):
    # This has to be in every script to prevent FileNotFoundError
    # Because for some reason, it runs it at C:\Windows\System32
    # Yeah, it is stupid, but I can't put these lines in custom_functions
    # Because that still brings up an error

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

output_dir = '.'
repo_path = os.getcwd()
output_path = os.path.join(output_dir, f"pack.mcpack")
start_time = time.time()
with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(repo_path):
        if '.git' in dirs:
            dirs.remove('.git')
        if '.gitattributes' in files:
            files.remove('.gitattributes')
        if 'zipper.py' in files:
            files.remove('zipper.py')
        if "pack.mcpack" in files:
            files.remove(f"pack.mcpack")
        if os.path.abspath(__file__) in files:
            files.remove(os.path.abspath(__file__))
        for file in files:
            file_path = os.path.join(root, file)
            file_path_length = len(file_path)
            try:
                print(f"\rArchiving: {str(file_path)[len(str(os.getcwd())):]}{' ' * (os.get_terminal_size().columns - len(str(file_path)[len(str(os.getcwd())):]) - 12)}", end='', flush=True)
            except OSError:
                print(f"\rArchiving: {file_path}", end='', flush=True)
            zipf.write(file_path, os.path.relpath(file_path, repo_path))
elapsed_time = time.time() - start_time
print(f"\rRepository zipped successfully at {output_path}{' ' * os.get_terminal_size().columns}",flush=True)
input(f"Elapsed Time: {elapsed_time:.2f} seconds")
