from cProfile import label
import tkinter as tk


class Operation(tk.Button):
    """ Object encapsulates ALL operation related actions """

    def __init__(self,
                 master,
                 width,
                 height,
                 image=None,
                 geometry='400x600+200+200',
                 title=None,
                 icon=None,
                 label_obj=None):
        self._master = master
        self._geometry = geometry
        self._title = title
        self._icon = icon
        self._label_obj = label_obj
        super().__init__(master=master,
                         width=width,
                         height=height,
                         image=image,
                         command=self.init_button)
        
        
    def init_button(self):
        """ main callable which initiates all button related actions """
        win = tk.Toplevel(self._master)
        win.geometry(self._geometry)
        win.title(self._title)
        win.resizable(0,0)
        if self._icon is not None:
            win.iconbitmap(self._icon)
        self._add_labels(win=win, label_obj=self._label_obj)
        
        
        # звать здесь
        
         
        # TODO: How would you implement nested buttons if it was necessary?

        win.grab_set()
        win.focus_set()
        win.wait_window()

        # TODO: Implement Entry, labels, calculation etc...

    def _add_labels(self, win, label_obj):
        label = tk.Label(win, width=300, height=300, image=label_obj, anchor=tk.CENTER)
        label.grid(row=0, column=0, columnspan=3, padx=47, pady=10)
                
    def _add_entries(self):
        self.block_user_entr = (self.win.register(lambda val: val.isdigit()),'%S')
        
        

    def _calculate(self):
        raise NotImplementedError


    
class CalculatorApp(tk.Tk):
    """ Sets up the main window and prepares object for session initialization """

    def __init__(self, geometry, title, settings, icon):

        # Non-pythonic way to initialize tk.Tk object without recursive loop error

        tk.Tk.__init__(self)
        self.geometry(geometry)
        self.resizable(0, 0)
        self.title(title)
        if icon is not None:
            self.iconbitmap(icon)
        self._cfg = settings
        
        self._store_button_images()    
        print('22')
    @staticmethod
    def create_img(img_path, subsample=False):
        if subsample:
            return tk.PhotoImage(file=img_path).subsample(2, 2)
        return tk.PhotoImage(file=img_path)
    
    
    def _store_button_images(self):
        for img_path in self._cfg:
            data = self._cfg[img_path]
            data.update({'img_obj': self.create_img(img_path, subsample=True)})
            label_path = data.pop('label_img')
            data.update({'label_obj': self.create_img(label_path)})

    def create_op(self, img_obj, g_row, g_column, geometry, title, icon, label_obj):

        # TODO: Handle constants outside of implementation

        op = Operation(self, 150, 150, img_obj, geometry, title, icon, label_obj)
        
        op.grid(row=g_row, column=g_column, rowspan=2, padx=30, pady=20)

    def run(self):
        for button_settings in self._cfg.values():
            self.create_op(**button_settings)

        self.mainloop()
