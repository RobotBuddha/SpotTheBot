import easygui as eg
import tell_if_bot

value = eg.enterbox("Enter user:")
var = tell_if_bot.testAccount(value)
if(len(var)>2):
    eg.msgbox(var)
else:
    eg.msgbox("CLASSIFICATION: " + var[0] + "\nCONFIDENCE: " + str(var[1]))
