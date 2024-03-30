import os
import shutil
import json

def copy_and_rename_version():
    versions_dir = os.path.expandvars(r"%appdata%\.minecraft\versions")
    home_dir = os.path.expandvars(r"%appdata%\.minecraft\home")
    versions = os.listdir(versions_dir)

    print("Версії:")
    for i, version in enumerate(versions):
        print(f"{i+1}. {version}")

    version_number = int(input("Введіть номер версії, яку ви хочете скопіювати: ")) - 1
    new_version_name = input("Введіть нову назву версії: ")

    old_version_path = os.path.join(versions_dir, versions[version_number])
    new_version_path = os.path.join(versions_dir, new_version_name)

    shutil.copytree(old_version_path, new_version_path)

    for filename in [".jar", ".jar.bak", ".json"]:
        old_file_path = os.path.join(new_version_path, versions[version_number] + filename)
        new_file_path = os.path.join(new_version_path, new_version_name + filename)
        os.rename(old_file_path, new_file_path)

        if filename == ".json":
            with open(new_file_path, "r+") as json_file:
                data = json.load(json_file)
                data["id"] = new_version_name
                data["jar"] = new_version_name
                data["family"] = new_version_name
                json_file.seek(0)
                json.dump(data, json_file)
                json_file.truncate()

    new_home_path = os.path.join(home_dir, new_version_name)
    os.makedirs(new_home_path, exist_ok=True)
    os.makedirs(os.path.join(new_home_path, "mods"), exist_ok=True)

copy_and_rename_version()
