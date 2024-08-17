import json
import string
import os


def strip_casefold(data) -> str:
    """Returns data stripped and lower case."""
    return data.strip().casefold()


def check_string_is_empty(data) -> bool:
    """Checks if data consists of only whitespace characters."""
    if data.translate({ord(c): None for c in string.whitespace}) == "":
        return True


def create_post_file(data, title) -> None:
    if not os.path.exists(f"posts/{title}"):
        os.makedirs(f"posts/{title}")
    try:

        with open(f"posts/{title}/index.html", "w") as file:
            file.write(data)
            print(f"Saved {title}/index.html to posts.")
    except:
        print("File already exists.")


def write_to_json_file(data, filename) -> None:
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
            print(f"Saved to {filename}")
    except:
        print("Something went wrong.")


def create_file_name(title) -> str:
    file_name = "".join(letter for letter in title if letter.isalnum())
    return file_name


def get_post_data(post):
    try:
        with open("save_files/db.json", "r") as file:
            db_content = json.load(file)
            post_data = db_content[post]
            print(f"\nData loaded for {post}.\n")
        return post_data
    except:
        print("Something went wrong.")
