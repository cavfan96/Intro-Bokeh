#import libraries
from bokeh.plotting import figure
#from bokeh.io import output_file, show
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
from bokeh.models.annotations import LabelSet
from bokeh.models.widgets import RadioButtonGroup

#create cds
source=ColumnDataSource(data=dict(average_grades=["B+","A","D-"],
                             exam_grades=["A+","C","D"],
                             student_names=["Stephan","Helder","Riazudin"]))


#create figure
f = figure(x_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
           y_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"])

#add labels for glyphs --shows the labels in the top left, sigh
labels=LabelSet(x='average_grades',y='exam_grades',text='student_names',
                x_offset=5,y_offset=5,source=source,render_mode='css') #adds an offset.
f.add_layout(labels)

#glyphs
f.circle(x='average_grades',y='exam_grades',source=source,size=8)

#need function for the Select to work
#create function
def update_labels(attr,old,new):
    labels.text=options[radio_button_group.active] #active method for radio button group widget

#dynamic feature
options=['average_grades','exam_grades','student_names'] #tuples
radio_button_group=RadioButtonGroup(labels=options)
#make the Select Field live
radio_button_group.on_change("active",update_labels) #change to active for RBG

#create layout
lay_out=layout([[radio_button_group]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
