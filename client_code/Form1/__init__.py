from ._anvil_designer import Form1Template
from anvil import *
from anvil.js import get_dom_node



class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.text_box_1.type = "search"
        self.init_components(**properties)
        print("helloabdc")
        get_dom_node(self.text_box_1).type='search'
        # Any code you write here will run before the form opens.
