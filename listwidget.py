# -*- coding: utf-8 -*-

"""
List Widget
Create a scrollable list with selectable rows. Data must be a List of Lists

@version: 17.03.17
@author: Edgardo Javier Stacul
@email: staculjavier@gmail.com
"""

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, ListProperty

Builder.load_string("""
<List>:
    ScrollView:
        id: sv
        GridLayout:
            id:         gl
            cols:       root.cols
            size_hint:  (None,None)
            height:     self.minimum_height
            width:      self.minimum_width
            spacing:    '2dp'
            
<ListCell>:
    font_size:'12dp'
    padding: ('2dp','2dp')
    size_hint: (None,None)
    size: self.texture_size
    color: 0,0,0,1
    bcolor: 1,1,1,1
    canvas.before:
        Color:
            rgba: self.bcolor
        Rectangle:
            pos: self.pos
            size: self.size

<ListHeader>:
    font_size: '12dp'
    padding: ('2dp','2dp')
    size_hint: (None,None)
    size: self.texture_size
    color: 1,1,1,1
    bcolor: 0.5, 0.5, 0.5, 1
    canvas.before:
        Color:
            rgba: self.bcolor
        Rectangle:
            pos: self.pos
            size: self.size
""")
    
class List(RelativeLayout):
    data = ListProperty([])
    cols = NumericProperty()
    rowSelected = NumericProperty()
    
    def __init__(self, *args, **kwargs):
        super(List, self).__init__(**kwargs)
        
    def on_data(self, *arg):
        self.list_scrollable()
        
    def list_scrollable(self):
        self.t = self.ids['gl'] #get table widget from kv
        #Reset widget
        self.t.clear_widgets()
        #Build header and table content
        if isinstance(self.data, list):
            try:
                self.Rows=[]
                self.t.cols=len(self.data[0])+1
                self.t.add_widget(ListHeader(text="<>"))
                for item in self.data[0]:
                    self.t.add_widget(ListHeader(text=item))
                for i in range(len(self.data)-1):
                    row=[]
                    row.append(ToggleButton(id=str(i+1),on_press=self.select_row,group='table',size_hint=(None,1),width='20dp'))
                    #cb.bind(active=self.selrow)
                    for j in range(len(self.data[i])):
                        row.append(ListCell(text=str(self.data[i+1][j]).encode("utf-8").decode("utf-8")))
                    for cell in row:
                        self.t.add_widget(cell)
                    self.Rows.append(row)            
            except:
                self.t.cols=1
                self.t.add_widget(ListHeader(text='Error al construir tabla'))
        else:
            self.t.cols=1
            self.t.add_widget(ListHeader(text='Error: datos incorrectos'))
            
    def refresh(self):
        self.list_scrollable()
        
    def select_row(self,button):
        for cell in self.Rows[self.rowSelected-1]:
            cell.color = [0,0,0,1]
            cell.bcolor = [1,1,1,1]
        self.rowSelected = int(button.id)
        for cell in self.Rows[self.rowSelected-1]:
            cell.color = [1,1,1,1]
            cell.bcolor = [0,0,0.8,1]
        
        
class ListHeader(Button):
    bcolor = ListProperty([1,1,1,1])


class ListCell(Label):
    bcolor = ListProperty([1,1,1,1])
