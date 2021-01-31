#import libraries
#from bokeh.io import output_file, show
from bokeh.io import curdoc #for bokeh server
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

#prepare the bokeh output - when going for static html file
#output_file("simple_bokeh.html")
#but it won't interact unless you use a bokeh server



#create widgets
text_input=TextInput(value="Paul")
button=Button(label="Generate Text")
output=Paragraph() #no params needed as updates dynamically

def update():
    output.text="Hello, " + text_input.value

button.on_click(update)

#render widgets
lay_out=layout([[button,text_input],[output]])

#only for static html
#show(lay_out)

#bokeh server
curdoc().add_root(lay_out)
