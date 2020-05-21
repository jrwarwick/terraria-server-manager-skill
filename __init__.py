from mycroft import MycroftSkill, intent_file_handler


class TerrariaServerManager(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('manager.server.terraria.intent')
    def handle_manager_server_terraria(self, message):
        self.speak_dialog('manager.server.terraria')


def create_skill():
    return TerrariaServerManager()

