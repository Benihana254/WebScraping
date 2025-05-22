# Programme to open url from clipboard and terminal
import webbrowser,sys,pyperclip
if len(sys.argv)>1:
    #below joins the typed argument disregarding index 0 and 1 to the last
    address = ' '.join(sys.argv[1:])
#this lines after an empy argument after 'python MapIt.py'
else: address = pyperclip.paste()
webbrowser.open_new_tab(f'https://www.google.com/maps/place/{address}')
print(f'You have been directed to {address}')
