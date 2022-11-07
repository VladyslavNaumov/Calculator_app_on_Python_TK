import tkinter as tk
from math import pi

сon_coef = 0.000001 #переводной коэф.
weigt_of_still = 7850 # Вес стали в кг/м3

class Calculate:
    сon_coef = 0.000001 #переводной коэф.
    weigt_of_still = 7850 # Вес стали в кг/м3
    
    @classmethod   
    def register_methods(cls):
        methods = {'calc_dvt_shv': cls.calc_dvt_shv, 
                   'calc_ugol': cls.calc_ugol,
                   'calc_pr': cls.calc_pr, 
                   'calc_kv': cls.calc_kv,
                   'calc_kr': cls.calc_kr
                   }
        return methods 
        
    
    """Calculation formula of I-beam and Channel"""
    @staticmethod
    def calc_dvt_shv(master, w_height, s_width, w_thickness, s_thickness, length):
        
        def calc_command():
            get_l_st = int(w_height.get())
            get_l_pl = int(s_width.get())
            get_t_st = int(w_thickness.get())
            get_t_pl = int(s_thickness.get())
            get_l_elem = int(length.get())/1000

            mas_elem = round((((get_l_st*get_t_st + get_l_pl*get_t_pl*2)*сon_coef*
                            get_l_elem)*weigt_of_still), 2)
            
            lab_v_dvt = tk.Label(master, wraplength=380)
            str_to_dp = f'weight of element, lenght: {get_l_elem} m = {mas_elem} kg'
            lab_v_dvt['text'] = str_to_dp
            lab_v_dvt.grid(row=8, column=0, columnspan=3, padx=20, sticky=tk.W+tk.E)
        return calc_command
    
    
    """Calculation formula of Corner"""
    @staticmethod
    def calc_ugol(master, fst_s_size, sc_s_size, w_thickness, length):
        def calc_command():
            get_l_pl1_ugol = int(fst_s_size.get())
            get_l_pl2_ugol = int(sc_s_size.get())
            get_t_pl_ugol = int(w_thickness.get())
            get_l_el_ugol = int(length.get())/1000

            mas_sv_ugol = round((((get_l_pl1_ugol*get_t_pl_ugol + get_l_pl2_ugol*
                                get_t_pl_ugol)*сon_coef * get_l_el_ugol) * weigt_of_still),2)
            
            lab_v_ugol = tk.Label(master, wraplength=380)
            str_to_ugol = f'weight of element, lenght: {get_l_el_ugol} m = {mas_sv_ugol} kg'
            lab_v_ugol['text'] = str_to_ugol
            lab_v_ugol.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E)
        return calc_command
    
    """Calculation formula of Rectengular tube"""
    @staticmethod
    def calc_pr(master, fst_s_size, sc_s_size, w_thickness, length):
        def calc_command():
            get_a_pr = int(fst_s_size.get())
            get_b_pr = int(sc_s_size.get())
            get_t_pr = int(w_thickness.get())
            get_el_pr = int(length.get())/1000
            mas_sv_pr = round(((((get_a_pr * get_b_pr) - ((get_a_pr - get_t_pr)*(get_b_pr - get_t_pr))) * 
            сon_coef * get_el_pr) * weigt_of_still),2)
            lab_v_pr = tk.Label(master, wraplength=380)
            str_to_pr = f'weight of element, lenght: {get_el_pr} m = {mas_sv_pr} kg'
            lab_v_pr['text'] = str_to_pr
            lab_v_pr.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E )

            if  mas_sv_pr <= 0:
                lab_v_pr_otm = tk.Label(master, 
                text='Side sizes[1,2] must be more then thickness[3]',fg='red')
                lab_v_pr_otm.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E )
        return calc_command    
    
    """Calculation formula of Square tube"""
    @staticmethod
    def calc_kv(master, sqr_s_size, w_thickness, length):
        def calc_command():    
            get_d_kv = int(sqr_s_size.get())
            get_t_kv = int(w_thickness.get())
            get_l_kv = int(length.get())/1000

            mas_sv_kv = round(((((get_d_kv**2 -(get_d_kv-get_t_kv*2)**2))* 
            сon_coef * get_l_kv) * weigt_of_still),2)
            lab_v_kv = tk.Label(master, wraplength=380)
            str_to_kv = f'weight of element, lenght: {get_l_kv} m = {mas_sv_kv} kg'
            lab_v_kv['text'] = str_to_kv
            lab_v_kv.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E )

            if  mas_sv_kv <= 0:
                lab_v_kv_otm = tk.Label(master, 
                text='Side size[1] must be more then thickness [2]',fg='red')
                lab_v_kv_otm.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E)
        return calc_command    
    
    @staticmethod
    def calc_kr(master, diametr, w_thickness, length):
        def calc_command():
            get_d_kr = int(diametr.get())
            get_t_kr = int(w_thickness.get())
            get_l_kr = int(length.get())/1000

            mas_sv_kr =round(((((get_d_kr**2 -(get_d_kr-get_t_kr*2)**2)*pi/4)* 
            сon_coef * get_l_kr) * weigt_of_still),2)
            lab_v_kr = tk.Label(master, wraplength=380)
            str_to_kr = f'weight of element, lenght: {get_l_kr} m = {mas_sv_kr} kg'
            lab_v_kr['text'] = str_to_kr
            lab_v_kr.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E )

            if  mas_sv_kr <= 0:
                lab_v_kr_otm = tk.Label(master, 
                text='Diametr [1] must be more then thickness [2]', fg='red')
                lab_v_kr_otm.grid(row=8, column=0, columnspan=3,padx=20, sticky=tk.W+tk.E )
        return calc_command

    
