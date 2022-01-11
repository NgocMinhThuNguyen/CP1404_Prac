from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Miles Converter App"""
    def build(self):
        """Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self):
        """Convert m to km"""
        user_input = self.get_validated_miles()
        result = user_input * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """handle up/down button press"""
        user_input = self.get_validated_miles()
        self.root.ids.input_miles.text = str(user_input + change)
        self.convert()

    def get_validated_miles(self):
        """get valid input from user"""
        try:
            user_input = float(self.root.ids.input_miles.text)
            return user_input
        except ValueError:
            return 0


MilesConverterApp().run()