
import tkinter as tk
from calculator.calculate import Calculate

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
                 operation_settings=None,
                 calculation_method=None ):
        self._master = master
        self._geometry = geometry
        self._title = title
        self._icon = icon
        self.operation_settings = operation_settings
        self._calculation_method = calculation_method
        
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
        self._add_img_labels(master=win, label_img=self.operation_settings.get("label_img"))
        self._add_text_labels_entry(master=win)
        calc_command = self._calculation_method(win, **self.dict_of_entrys)
        
        calc_button = tk.Button(master=win, text='Сalculate mass', command=calc_command, 
                                 bd=4, relief=tk.RAISED)
        calc_button.grid(row=7, column=0, columnspan=3, padx=20, sticky=tk.W+tk.E)       
        
        win.grab_set()
        win.focus_set()
        win.wait_window()

    def _add_img_labels(self, master, label_img):
        label = tk.Label(master, width=300, height=300, image=label_img)
        label.grid(row=0, column=0, columnspan=3, padx=47, pady=10)
          
    def _add_text_labels_entry(self, master):
        block_user_entr = (master.register(lambda val: val.isdigit()),'%S')
        self.dict_of_entrys = {}
        for index, (text_path, param) in enumerate(zip(self.operation_settings.get('text'), self.operation_settings.get('parameters')), 1):     
            lebel_text1 = tk.Label(master, text = text_path)
            lebel_text1.grid(row=index, column=0, ipadx=15, pady=10, sticky=tk.W)     
            
            entry = tk.Entry(master,
                                validate = 'key', relief=tk.SUNKEN, validatecommand=block_user_entr, bd = 3)
            entry.grid(row=index, column=1,ipadx=10, pady=10, sticky=tk.W)
            self.dict_of_entrys[param] = entry
            
            lebel_text2 = tk.Label(master, text = 'мм')
            lebel_text2.grid(row=index, column=2, ipadx=10, pady=10, sticky=tk.W)
    
class CalculatorApp(tk.Tk):
    """ Sets up the main window and prepares object for session initialization """
    def __init__(self, geometry, title, icon, operation_settings):
        tk.Tk.__init__(self)
        self.geometry(geometry)
        self.resizable(0, 0)
        self.title(title)
        if icon is not None:
            self.iconbitmap(icon)
        self._op_set = operation_settings
        self._store_images()  
        self.calculation_methods = Calculate.register_methods()  
        
    @staticmethod
    def create_img(img_path, subsample=False):
        if subsample:
            return tk.PhotoImage(file=img_path).subsample(2, 2)
        return tk.PhotoImage(file=img_path)
    
    def _store_images(self):
        for operation in self._op_set:
            operation_cfg = self._op_set[operation]
            operation_cfg.update({'button_img': self.create_img(operation_cfg.get("button_path"), subsample=True),
                               'label_img': self.create_img(operation_cfg.get("label_path")) })
            
    def create_op(self, title, button_img, g_row, g_column, icon, **kwargs):
        calcl_method = self.calculation_methods.get(kwargs['calculate'])
        op = Operation(self, 150, 150, button_img, title=title, icon=icon, operation_settings=kwargs, calculation_method = calcl_method)
        op.grid(row=g_row, column=g_column, rowspan=2, padx=30, pady=20)

    def run(self):
        for op_set_key, op_set_value in self._op_set.items():
            self.create_op(op_set_key, **op_set_value)
        self.mainloop()
