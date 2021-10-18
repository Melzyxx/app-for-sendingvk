from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from saya import Vk

#settings
VK_TOKEN = "вк токен"
VK_ID = 1

vk = Vk(token = VK_TOKEN)
del VK_TOKEN

def get_users(group_id:int = 1) -> list:
	response = vk.groups.getMembers(
		group_id = group_id,
		filter = "time_asc"
	)
	return response["response"]["items"]

class SenderApp(App):
	
	def __init__(self):
		super().__init__()
		self.input = TextInput(text = "text", padding = (40, 40))
	
	def click(self, instance):
		text = self.input.text
		self.input.text = ""
		users_list = get_users(VK_ID)
		for user_id in users_list:
			try:
				vk.messages.send(
					user_id = user_id,
					message = text,
					random_id = 0
				)
			except:
				pass #No permission
	
	def build(self):
		root = BoxLayout(orientation = "vertical")
		
		root.add_widget(self.input)
		
		button = Button(text = "SEND ALL", on_press = self.click)
		root.add_widget(button)
		
		return root
		
if __name__ == "__main__":
	SenderApp().run()