from mycroft import MycroftSkill, intent_file_handler


class Salom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('salom.intent')
    def handle_salom(self, message):
        self.speak_dialog('salom')


def create_skill():
    return Salom()

