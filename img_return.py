from nider.core import Font
from nider.core import Outline
from nider.models import Content
from nider.models import Linkback
from nider.models import Paragraph
from nider.models import Image
import json

f = open("quotes.json", "r")
File_json = json.load(f, encoding='ISO 8859-1')
roboto_font_folder = '/home/ziad/Desktop/Console_Posts/Posts/'
text_outline = Outline(2, '#121212')

def img_to_txt(txt,author,result):
    para = Paragraph(text=txt,
                 font=Font(roboto_font_folder + 'Roboto-Black.ttf',30),
                 text_width=30,
                 align='center',
                 color='#ededed',
                 outline=text_outline
                 )
    linkback = Linkback(text=author,
                    font=Font(roboto_font_folder + 'Roboto-Black.ttf',30),
                    color='#ededed',
                    outline=text_outline
                 )
    content = Content(paragraph=para, linkback=linkback)
    img = Image(content,
            fullpath=result,
            width=3000,
            height=2005
            )
    img.draw_on_image('bg.png')
def quote_Text(counter):
    global File_json
    quoteText = File_json[counter]['quoteText']
    return quoteText
def quote_Author(counter):
    global File_json
    quoteAuthor = "-" + File_json[counter]['quoteAuthor'] 
    return quoteAuthor
for counter in range(550):
    result = str(counter) + ".png"
    img_to_txt(quote_Text(counter),quote_Author(counter),result)
