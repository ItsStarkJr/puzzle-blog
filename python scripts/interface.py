from tkinter import *
from generator import Generator
import json

import customtkinter
from customtkinter import filedialog
from utils import write_to_json_file, open_json_file


class AddScript:
    def __init__(self) -> None:
        self.widget_background_colour = "#101010"
        # self.get_user_settings()
        self.app_setup()
        self.new_script_data = {}
        self.has_example = False

    # User settings

    # def get_user_settings(self):
    #     try:
    #         with open("user_settings.json", "r") as file:
    #             file_content = json.load(file)
    #             self.author = file_content["author"]
    #             self.profile_link = file_content["profile_link"]
    #     except:
    #         print("Something went wrong.")

    # App setup

    def app_setup(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.root = customtkinter.CTk()
        self.root.geometry("1280x1180+300+100")
        self.root.title("Add Script")
        self.root.bind("<Escape>", self.close_app)

        self.frame_1 = customtkinter.CTkFrame(master=self.root)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.setup_main_puzzle_frame()

    # def include_example(self):
    #     if self.include_example_box.get() == 1:
    #         self.setup_example_puzzle_frame()
    #         self.example_image_id_entry.grid(row=8, column=1, padx=10, pady=10)
    #         self.example_links_label.grid(
    #             row=9, column=0, columnspan=3, padx=10, pady=(10, 0)
    #         )
    #         self.example_links_box.grid(
    #             row=10, column=0, columnspan=3, padx=10, pady=(0, 10)
    #         )
    #     else:
    #         self.example_image_id_entry.destroy()
    #         self.example_links_label.destroy()
    #         self.example_links_box.destroy()

    def setup_main_puzzle_frame(self):
        # Title frame

        self.main_puzzle_frame = customtkinter.CTkFrame(self.frame_1)
        self.main_puzzle_frame.pack(pady=10)

        # check_var = customtkinter.StringVar(value="on")

        self.rules_label = customtkinter.CTkLabel(
            master=self.main_puzzle_frame,
            text="Rules:",
            text_color="grey",
        )

        self.rules_box = customtkinter.CTkTextbox(
            master=self.main_puzzle_frame,
            width=1020,
            height=150,
            fg_color=self.widget_background_colour,
            corner_radius=0,
        )

        self.rules_label.grid(row=4, column=0, columnspan=3, padx=10, pady=(10, 0))
        self.rules_box.grid(row=5, column=0, columnspan=3, padx=10)

        self.buttons_frame = customtkinter.CTkFrame(self.frame_1)
        self.buttons_frame.pack(pady=10)

        # Buttons

        self.submit_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            command=self.submit,
            text="Submit",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
        )

        self.update_html_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            command=self.update_html,
            text="Update HTML",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
        )

        self.submit_button.grid(row=0, column=0, padx=10, pady=10)
        self.update_html_button.grid(row=0, column=1, padx=10, pady=10)
        self.root.filename = filedialog.askopenfilename(
            initialdir="/",
            title="select file",
            filetypes=(("png files", "*.png"), ("all files", "*.*")),
        )

    def get_description(self):
        self.new_script_data["description"] = self.rules_box.get(0.0, "end").strip()
        print(self.new_script_data)

    def append_new_data(self):
        self.scripts_data.append(self.new_script_data)

    def get_data(self):

        self.get_description()
        # self.append_new_data()

    def submit(self):
        self.scripts_data = open_json_file("scripts_data.json")
        self.get_data()
        write_to_json_file(self.scripts_data, "scripts_data.json")

    def update_html(self):
        webpage_generator = Generator()
        webpage_generator.run()

    def close_app(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


awesome_script_adder = AddScript()
awesome_script_adder.run()
