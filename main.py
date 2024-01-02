from xml.dom.minidom import parse
import xml.dom.minidom
name = input()
DOMTree = xml.dom.minidom.parse(name)
collection = DOMTree.documentElement
texts = collection.getElementsByTagName("text")
for text in texts:
    if text.childNodes[0].data=="UNREGISTERED":
        text.childNodes[0].data = ""
with open(name, 'w', encoding='utf-8') as f:
    DOMTree.writexml(f, addindent='\t', newl='\n',encoding='utf-8')
