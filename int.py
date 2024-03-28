from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

f=0

class MyApp(App):
	def build(self):
		layout = BoxLayout(orientation='vertical')
		button = Button(text='Press on me', size_hint=(0.3, 0.3), pos_hint={'x':0.35})
		button.bind(on_press=self.on_button_click)
		self.label = Label(text=f'{f}')
		layout.add_widget(self.label)
		layout.add_widget(button)
		return layout

	def on_button_click(self, instance):
		self.label.text=f'{f+1}'

if __name__ == '__main__':
	MyApp().run()
