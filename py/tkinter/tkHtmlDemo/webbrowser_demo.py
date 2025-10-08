import tempfile
import webbrowser

tmp=tempfile.NamedTemporaryFile(delete=False)
path=tmp.name+'.html'

f=open(path, 'w')
f.write("<html><body><h1>Test</h1></body></html>")
f.close()
webbrowser.open('file://' + path)