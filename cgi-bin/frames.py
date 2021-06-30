import cgi

print('Content-type: text/html')
print()
print("""<frameset cols="25%,75%" frameborder="yes" border="5" bordercolor="#008800">
    <frame src="form.py" marginwidth="20" marginheight="20">
    <frame src="mg_assist.py" name="main_window" marginwidth="0" scrolling="no" noresize>
    </frameset>""")

