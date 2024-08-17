from utils import create_post_file, create_file_name, get_post_data
from bs4 import BeautifulSoup

from post_components import *
from datetime import datetime, date


class Generator:
    def __init__(self, post) -> None:
        self.post = post

        self.set_post_data("json_files/test.json")

    def set_post_data(self, file_name):
        self.post_data = get_post_data(self.post)
        self.title = self.post
        self.difficulty = self.post_data["difficulty"]
        self.variant = self.post_data["variant"]
        self.genre = self.post_data["genre"]
        self.intro = self.post_data["intro"]
        self.rules = self.post_data["rules"]
        self.tags = self.post_data["tags"]
        self.links = self.post_data["links"]
        self.image_file = "../../assets/images/1.png"
        self.date = date.today().strftime("%b %d, %Y")

    def create_post_classes(self):
        classes = ""
        classes += f" difficulty-{self.difficulty}"
        classes += f" variant-{self.variant}"
        classes += self.list_to_classes(self.genre, "genre")
        classes += self.list_to_classes(self.tags, "tags")
        return classes

        # self.split_descriptions(self.rules)

    def list_to_classes(self, data, classname):
        x = ""
        for i in data:
            x += f" {classname}-{i}"
        return x

    def split_descriptions(self, data, description):
        x = ""
        y = data.split("\r\n")
        for i in y:
            x += f'<p class="{description}-description">{i.strip()}</p>'
        return x
    
    def create_links_string(self):
        if self.links:
            links_string = ""
            for i in self.links.items():
                links_string+=f"""<a href={i[1]} target="_blank">Solve on {i[0]}</a>"""
            return links_string
        
        else:
            return ""


    

    

    def clean_up_html(self):
        soup = BeautifulSoup(self.script_string, "html.parser")
        self.script_string = soup.prettify()

    def create_page(self) -> None:
        self.post_page = f"{COMP_A}{self.title}{COMP_B}{self.image_file}{COMP_C}{self.create_post_classes()}{COMP_D}{self.title}{COMP_E}{self.date}{self.split_descriptions(self.intro, "intro")}{COMP_G}{self.split_descriptions(self.rules, "rules")}{COMP_H}{self.difficulty}{COMP_I}{self.create_links_string()}{COMP_J}{self.image_file}{COMP_K}"

    def run(self) -> None:
        self.create_page()
        create_post_file(self.post_page, self.title)


generator = Generator("1 - Dateable Puzzle Lol (Kouchoku)")
generator.run()
