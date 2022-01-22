from model.browsemodeutil import BrowseModeUtil
import tkinter as tk
class BrowseMode:
    def __init__(self,widgets,state):
        self.widgets=widgets
        self.util = BrowseModeUtil(state)
        self.setPageData(self.util.pageData)
    def place(self):
        self.widgets[0].place(x=200.0, y=160.0)
        self.widgets[1].place(x=200.0, y=205)
        self.widgets[2].place(x=880, y=206, height=352)
        self.widgets[3].place(x=600.0, y=600)
        self.widgets[4].place(x=800.0, y=160)
        self.widgets[5].place(x=1020.0, y=178)
        self.widgets[6].place(x=1020.0, y=200)

    def addCharacter(self):
        start = int(str(self.widgets[1].tag_ranges("sel")[0]).replace("1.", ""))
        end = int(str(self.widgets[1].tag_ranges("sel")[1]).replace("1.", ""))
        pageData = self.util.generateBrowsingPageDataAfterAdd(start,end)
        self.setPageData(pageData)
        
    def setPageData(self,pageData):
        self.widgets[1].tag_remove(tk.SEL, "1.0", tk.END)
        self.widgets[1].configure(state='normal')
        self.widgets[1].delete(1.0, tk.END)
        self.widgets[1].insert('end', pageData['signList'])
        self.widgets[1].configure(state='disabled')


    def selectResults(self,state):
        hsk = self.widgets[5].get()
        state.changeHsk(hsk)
        pageData = self.util.generateBrowsingPageDataAfterAdd(0,0)
        self.setPageData(pageData)