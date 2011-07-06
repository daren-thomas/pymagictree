from magictree import html, head, title, body, h1, p
doc = html(
        head(
          title(u'Chapter 1: Greeting')),
        body(
          h1('Chapter 1: Greeting'),
          p('Hello, world!')))

from xml.etree import ElementTree as et    
et.dump(doc)
