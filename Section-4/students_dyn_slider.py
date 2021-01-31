#import libraries
from bokeh.plotting import figure
#from bokeh.io import output_file, show
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.annotations import LabelSet
from bokeh.models.widgets import Select, Slider

#create cds
source_original=ColumnDataSource(dict(average_grades=[7,8,10],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudin"]))

source=ColumnDataSource(dict(average_grades=[7,8,10],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudin"]))
#create figure
f = figure(x_range=Range1d(start=0,end=12),
           y_range=Range1d(start=0,end=12))

#add labels for glyphs --shows the labels in the top left, sigh
labels=LabelSet(x='average_grades',y='exam_grades',text='student_names',
                x_offset=5,y_offset=5,source=source,render_mode='css') #adds an offset.
f.add_layout(labels)

#glyphs
f.circle(x='average_grades',y='exam_grades',source=source,size=8)

#create filtering slider
def filter_grades(attr,old,new):
    source.data={key:[value for i, value in enumerate(source_original.data[key]) if source_original.data['exam_grades'][i]>=slider.value] for key in source_original.data}
    print(slider.value)

#need function for the Select to work
#create labeling function
def update_labels(attr,old,new):
    labels.text=select.value

#dynamic feature
options=[('average_grades','Avg Grades'),('exam_grades','Exam Grades'),('student_names','Student Names')] #tuples
select=Select(title="Attribute",options=options)
#make the Select Field live
select.on_change("value",update_labels)

slider=Slider(start=min(source_original.data['exam_grades'])-1,end=max(source_original.data['exam_grades'])+1,value=8,step=0.1,title="Exam Grade: ")
slider.on_change("value",filter_grades)
#create layout
lay_out=layout([[select],[slider]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
