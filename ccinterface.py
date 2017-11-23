#!/usr/bin/python3
import re
import os
import sys
import shutil
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import threading

import lscheckout


labelname = 'TASK_ZHAOY2_'
proj_path = "C:\\D\\Project\\tool_proj"
bat_path = "C:\\D\\Tools\\lscheckout"
NETViewPath = '\\\\CNSHGCTC-AP07\\views\ASIA\\bjq5dl\\'

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):

        self.button1 = tk.Button(self, text="creat folder", width = 14, fg="red",command=self.create_folder)
        self.button2 = tk.Button(self, text="find branch", width = 14, fg="red",command=self.findbr_button)
        self.button3 = tk.Button(self, text="find label", width = 14, fg="red",command=self.findlb_button)
        self.button4 = tk.Button(self, text="find checkout", width = 14, fg="red",command=self.findco_button)
        self.button5 = tk.Button(self, text="get file from conf ", width = 14, fg="red",command=self.getfilelist_button)

        self.button6 = tk.Button(self, text="sf file", width = 14, fg="red",command=self.setfile_sf)
        self.button7 = tk.Button(self, text="pjt file list", width = 14, fg="red",command=self.setfile_list)
        self.button8 = tk.Button(self, text="sf Gen target", width = 14, fg="red",command=self.sf_gen_target)
        self.button9 = tk.Button(self, text="all files in view", width = 14, fg="red",command=self.getfiles_from_folder)
        self.button_cpconfig = tk.Button(self, text="copy config to view", width = 14, fg="red",command=self.copy_config2view)
        self.button_createview = tk.Button(self, text="create view", width = 14, fg="red",command=self.mkview)
        self.button_getspec = tk.Button(self, text="get spec/UT", width = 14, fg="red",command=self.get_spec_relative)
        # self.button8 = tk.Button(self, text="find checkout", width = 14, fg="red",command=self.findco_button)
        # self.button8 = tk.Button(self, text="get file list", width = 14, fg="red",command=self.getfilelist_button)
        self.specUn = tk.IntVar()
        self.check_spec = tk.Checkbutton(self, text ='spec        ', variable =self.specUn ,width = 10)

        self.utCb =tk.IntVar()
        self.check_ut = tk.Checkbutton(self, text ='UT result', variable =self.utCb ,width = 10)

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)        

        self.text_view = tk.Text(self,height = "1",width = 30)  
        self.text_base = tk.Text(self,height = "1",width = 30)  

        self.entry_view = tk.Entry(self,width = 40)  
        self.entry_base = tk.Entry(self,width = 40)  
        self.entry_label = tk.Entry(self,width = 40)  
        self.entry_branch = tk.Entry(self,width = 40)  
        self.entry_sf = tk.Entry(self,width = 40)  
        self.entry_filelist = tk.Entry(self,width = 40)  
        self.entry_gv = tk.Entry(self,width = 40)  

        self.label1 = tk.Label(self, text = '')
        self.label2 = tk.Label(self, text = 'view')
        self.label3 = tk.Label(self, text = 'base')
        self.label4 = tk.Label(self, text = 'label')
        self.label5 = tk.Label(self, text = 'branch')
        self.label6 = tk.Label(self, text = 'gv')

        menubar = tk.Menu(self) 
        filemenu = tk.Menu(menubar, tearoff=0)  
        filemenu.add_command(label="Open", command=self.findlb_button)  
        filemenu.add_command(label="Save", command=self.findlb_button)  
        filemenu.add_separator()  
        filemenu.add_command(label="Exit", command=root.destroy)  

        menubar.add_cascade(label="File", menu=filemenu) 
        menubar.add_cascade(label="Exit", command=root.destroy) 

        self.master['menu'] = menubar
        
        
        self.button1.grid(row = 2, column = 1, padx = 10, pady = 5)
        self.button2.grid(row = 8, column = 1, padx = 10, pady = 5)
        self.button3.grid(row = 7, column = 1, padx = 10, pady = 5)
        self.button4.grid(row = 9, column = 1, padx = 10, pady = 5)
        self.button5.grid(row = 13, column = 1, padx = 10, pady = 5)
        self.button6.grid(row = 2, column = 4, padx = 10, pady = 5)
        self.button7.grid(row = 3, column = 4, padx = 10, pady = 5)
        self.button8.grid(row = 10, column = 4, padx = 10, pady = 5)
        self.button9.grid(row = 14, column = 1, padx = 10, pady = 5)
        self.button_cpconfig.grid(row = 4, column = 1, padx = 10, pady = 5)
        self.button_createview.grid(row = 3, column = 1, padx = 10, pady = 5) 
        self.button_getspec.grid(row = 14, column = 4, padx = 10, pady = 5) 


        self.check_spec.grid(row = 14, column = 5, padx = 10, pady = 5) 
        self.check_ut.grid(row = 15, column = 5, padx = 10, pady = 5) 
        # self.text_view.grid(row = 2, column = 2, padx = 10)
        # self.text_base.grid(row = 4, column = 2, padx = 10)
        self.entry_view.grid(row = 2, column = 3, padx = 10, pady = 10)
        self.entry_base.grid(row = 3, column = 3, padx = 10, pady = 10)    
        self.entry_label.grid(row = 7, column = 3, padx = 10, pady = 10)
        self.entry_branch.grid(row = 8, column = 3, padx = 10, pady = 10) 
        self.entry_gv.grid(row = 6, column = 3, padx = 10, pady = 10)  

        self.entry_sf.grid(row = 2, column = 5, padx = 10, pady = 10)
        self.entry_filelist.grid(row = 3, column = 5, padx = 10, pady = 10) 

        # self.quit.grid(row = 20, column = 10, padx = 10 ,pady = 10)
        self.label2.grid(row = 2, column = 2, padx = 10)
        self.label3.grid(row = 3, column = 2, padx = 10)
        self.label4.grid(row = 7, column = 2, padx = 10)
        self.label5.grid(row = 8, column = 2, padx = 10)
        self.label6.grid(row = 6, column = 2, padx = 10)
    def create_folder(self):
        view = self.entry_view.get().replace('\n','')
        base = self.entry_base.get().replace('\n','')
        label = self.entry_label.get().replace('\n','')
        branch = self.entry_branch.get().replace('\n','')
        targetfolder = proj_path + '\\' + view +'\\'
        gv = re.findall('gv\d{6}', view)
        if os.path.exists(targetfolder):
            # delfolder = tk.messagebox.askyesno('info', "folder has existed, delete it?")
            # if delfolder == True:
            #     shutil.rmtree(targetfolder)
            #     pass
            # else:
            #     pass
            os.system('start '+ targetfolder)
            tk.messagebox.showinfo('info', 'VIEW  folder has existed')
            return
        if view == '':
            tk.messagebox.showinfo('info', 'VIEW  can not be empty')
            return 
        if len(gv) == 0:
            try:
                os.mkdir(targetfolder)
                os.system('start '+ targetfolder)
                with open(proj_path + '\\' + view +'\\'+ view+'_checkin.txt','w') as f:
                    f.write('Base: '+ base + '\n')
                    f.write('View: '+ view + '\n')
            except Exception as e:
                tk.messagebox.showinfo('error', e)
        else:
            if view == '':
                tk.messagebox.showinfo('info', 'base  can not be empty')
                return
            try:
                os.mkdir(targetfolder)
                os.system('start '+ targetfolder)
                with open(proj_path + '\\' + view +'\\'+gv[0] + '_checkin.txt', 'w') as f:
                    f.write('Base: '+ base + '\n')
                    f.write('View: '+ view + '\n')
                    f.write('label='+labelname.upper()+gv[0].upper()+' ; branche='+labelname.lower()+gv[0].lower())
                cmd = os.getcwd()+'\\gv_routine\\tcg_gv_prepare_from_template.bat '+ view +' '+base+' '+ targetfolder
                print(cmd)
                os.system(cmd)
            except Exception as e:
                tk.messagebox.showinfo('error', e) 
        '''
         get the file list automatically,
        '''
        # if os.path.exists('X:\\'+view+'\\gill_vob\\6_coding\\config.py'):
        #     tk.messagebox.showinfo('info', 'File :  X:\\'+view+'\\gill_vob\\6_coding\\config.py')
        #     shutil.copy('X:\\'+view+'\\gill_vob\\6_coding\\config.py', targetfolder+'config.py')
        #     pypjt = targetfolder+'config.py'
        #     if len(gv) == 1:
        #         outpath = proj_path+'\\'+view+'\\'+gv[0]+'_filelist.txt'
        #     else: 
        #         outpath = proj_path+'\\'+view+'\\'+view+'_filelist.txt'
        #     lscheckout.multigetFileList(file = pypjt, outpath = outpath )
        # elif os.path.exists('X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt'):
        #     tk.messagebox.showinfo('info', 'File :  X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt')
        #     shutil.copy('X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt',targetfolder+'project.pjt')
        #     pypjt = targetfolder+'project.pjt'
        #     if len(gv) == 1:
        #         outpath = proj_path+'\\'+view+'\\'+gv[0]+'_filelist.txt'
        #     else: 
        #         outpath = proj_path+'\\'+view+'\\'+view+'_filelist.txt'
        #     lscheckout.multigetFileList(file = pypjt, outpath = outpath )
        # else:
        #     tk.messagebox.showinfo('info', 'do not find files list')
        #     return 
    def copy_config2view(self):
        view = self.entry_view.get().replace('\n','')
        base = self.entry_base.get().replace('\n','')
        label = self.entry_label.get().replace('\n','')
        branch = self.entry_branch.get().replace('\n','')
        targetfolder = proj_path + '\\' + view +'\\'
        gv = re.findall('gv\d{6}', view)
        if len(gv)>=1:
            # copy the config_view.cfg to catalogue
            configview = targetfolder+gv[0].upper()+'\\Script\\config_view.cfg'
            viewpath = ['\\gill_vob\\6_coding\\src\\',
                        '\\gill_vob\\6_coding\\blois_code_p_l\\',
                        '\\gill_vob\\6_coding\\blois_soft_vob\\',
                        '\\gill_vob\\6_coding\\gill_dcm624_code\\',
                        '\\blois_hmd_code\\',
                        '\\blois_code_p_l\\',
                        '\\blois_soft_vob\\',
                        '\\gwm_secure_vob\\',
                        '\\hwi_vob\\',
                        '\\gill_dcm624_code\\']
            if os.path.exists(configview):
                tk.messagebox.showinfo('info', 'File: '+configview) 
                try:
                    for i in viewpath:
                        targetpath = 'X:\\'+view+i
                        if os.path.exists(targetpath):
                            shutil.copy(configview, targetpath+'config_view.cfg')
                except Exception as e:
                    tk.messagebox.showinfo('error', e) 
        else:
            tk.messagebox.showinfo('info', 'can not get gv number') 
    def getview(self):
        # view = self.text_view.get('1.0', tk.END)
        view = self.entry_view.get()
        base = self.entry_base.get()
        label = self.entry_label.get()
        branch = self.entry_branch.get()
        # tk.messagebox.showinfo('info', view + '\n' + base)
        info = tk.messagebox.askyesno('info', 'VIEW: '+ view + '\n' + base)
        if info == True:
            print(view)
            print(base)
        else:
            pass
    def findbr_button(self):
        view = self.entry_view.get()
        base = self.entry_base.get()
        label = self.entry_label.get()
        branch = self.entry_branch.get()
        info = tk.messagebox.askyesno('info','VIEW: '+ view + '\n' + 'Branch: '+ branch)
        if info == True:
            print(view)
            print(base)
            lscheckout.find_br(branch = branch, view = view)
        else:
            pass
        pass
    def findlb_button(self):
        view = self.entry_view.get()
        base = self.entry_base.get()
        label = self.entry_label.get()
        branch = self.entry_branch.get()
        info = tk.messagebox.askyesno('info', 'VIEW: '+ view + '\n' +'Label: ' + label)
        if info == True:
            print(view)
            print(base)
        else:
            pass
    def findco_button(self):
        view = self.entry_view.get()
        base = self.entry_base.get()
        label = self.entry_label.get()
        branch = self.entry_branch.get()
        info = tk.messagebox.askyesno('info', 'VIEW: '+ view )
        if info == True:
            print(view)
            print(base)
        else:
            pass
    def getfilelist_button(self):
        view = self.entry_view.get()
        # base = self.entry_base.get()
        # label = self.entry_label.get()
        # branch = self.entry_branch.get()
        gvno = self.entry_gv.get()
        gv = re.findall('gv\d{6}', view)
        targetfolder = proj_path + '\\' + view +'\\'
        if view == '':
            tk.messagebox.showinfo('info', 'please fill in view')
            return
        info = tk.messagebox.askyesno('info', 'Get Project File Automaticlly? ')
        if info == True:
            if os.path.exists('X:\\'+view+'\\gill_vob\\6_coding\\config.py'):
                tk.messagebox.showinfo('info', 'File :  X:\\'+view+'\\gill_vob\\6_coding\\config.py')
                # shutil.copy('X:\\'+view+'\\gill_vob\\6_coding\\config.py', targetfolder+'config.py')
                srcfile = 'X:\\'+view+'\\gill_vob\\6_coding\\config.py'
                tgtfile = targetfolder+'config.py'
                print(srcfile)
                print(tgtfile)
                os.system('copy /y '+srcfile+' '+tgtfile)
                pypjt = targetfolder+'config.py'
                if len(gv) == 1:
                    outpath = proj_path+'\\'+view+'\\'+gv[0]+'_filelist.txt'
                else: 
                    outpath = proj_path+'\\'+view+'\\'+view+'_filelist.txt'
                lscheckout.multigetFileList(file = pypjt, outpath = outpath )
            elif os.path.exists('X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt'):
                tk.messagebox.showinfo('info', 'File :  X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt')
                # shutil.copy('X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt',targetfolder+'project.pjt')
                srcfile = 'X:\\'+view+'\\blois_hmc_code\\Software\\Environnement\\codewright\\project.pjt'
                tgtfile = targetfolder+'config.py'
                os.system('copy /y '+srcfile+' '+tgtfile)
                pypjt = targetfolder+'project.pjt'
                if len(gv) == 1:
                    outpath = proj_path+'\\'+view+'\\'+gv[0]+'_filelist.txt'
                else: 
                    outpath = proj_path+'\\'+view+'\\'+view+'_filelist.txt'
                lscheckout.multigetFileList(file = pypjt, outpath = outpath )
            else:
                pass
        else:
            # tk.messagebox.showinfo('info', 'do not find files list automatically')
            flist = filedialog.askopenfilename(title = 'raw file list', initialdir = proj_path+'\\'+view)
            gv = re.findall('gv\d{6}', view)
            if len(gv) == 1:
                outpath = proj_path+'\\'+view+'\\'+gv[0]+'_filelist.txt'
            else:
                if gvno == '':
                    tk.messagebox.showinfo('info', 'please fill in gv number')
                    return 
                else:
                    outpath = proj_path+'\\'+view+'\\'+gvno+'_filelist.txt'
            if flist != '':
                if  os.path.exists(outpath):
                    info = tk.messagebox.askyesno('info','regenerate file list ?')
                    if info == True:
                        if os.path.exist(outpath+'_old'):
                            os.remove(outpath+'_old')
                        os.rename(outpath, outpath+'_old')
                    else:
                        return
                lscheckout.multigetFileList(file = flist, outpath = outpath )   #outpath is a real file
                self.entry_filelist.delete(0, tk.END)
                self.entry_filelist.insert(0, outpath)
            else:
                return
    def setfile_sf(self):
        view = self.entry_view.get().replace('\n','')
        f = filedialog.askopenfilename(title= 'open sf file', initialdir = proj_path+'\\'+view)
        self.entry_sf.delete(0, tk.END)
        self.entry_sf.insert(0, f)
    def setfile_list(self):
        view = self.entry_view.get().replace('\n','')
        f = filedialog.askopenfilename(title= 'file list', initialdir = proj_path+'\\'+view)
        self.entry_filelist.delete(0, tk.END)
        self.entry_filelist.insert(0, f)
    def sf_gen_target(self):
        view = self.entry_view.get().replace('\n','')
        sffile = self.entry_sf.get().replace('\n','')
        pjtfile = self.entry_filelist.get().replace('\n','')
        gvno = self.entry_gv.get()
        if view =='':
            tk.messagebox.showinfo('error', 'please fill in view')
            return
        vtreefolder = proj_path + '\\' + view +'\\'+'vtree'
        if os.path.exists(vtreefolder):
            os.system('start '+ vtreefolder)
        else:
            os.mkdir(vtreefolder)
            os.system('start '+ vtreefolder)
        #  sf generate out file, check the gv number, name the file with gv number
        gv = re.findall('gv\d{6}', view)
        if len(gv) == 1:                   
            outFile = proj_path+'\\'+view+'\\'+gv[0]+'_sfout.txt'
        else:
            if gvno == '':
                tk.messagebox.showinfo('info', 'please fill in gv number')
                return 
            else:
                outFile = proj_path+'\\'+view+'\\'+gvno+'_sfout.txt'
        # finally generate the sf out file
        if view =='' or sffile=='' or pjtfile=='':
            tk.messagebox.showinfo('info', 'please fill in view,sffile,pjtfilelist')
            return
        else:
            specdictlist = lscheckout.alyfile_sf(file = sffile)
            if len(specdictlist) == 0:
                tk.messagebox.showinfo('info', 'no spec in sf file')
                return
            else:
                lscheckout.findtarget(listfile = pjtfile, dictlist = specdictlist, view = view, outfile = outFile)
                pass
        pass
# spec  and  ut  result
    def get_spec_relative(self):
        view = self.entry_view.get().replace('\n','')
        sffile = self.entry_sf.get().replace('\n','')
        pjtfile = self.entry_filelist.get().replace('\n','')
        print(self.specUn.get())
        print(self.utCb.get())
        utfile = proj_path+'\\'+view+'\\UT_Result.txt'
        if view == '':
            return
        specfolder = proj_path + '\\' + view +'\\'+'SPEC'
        if os.path.exists(specfolder) == False:
            try:
                os.mkdir(specfolder)
            except Exception as e:
                tk.messagebox.showinfo('error', e)
        specdictlist = lscheckout.alyfile_sf(file = sffile)
        if len(specdictlist) == 0:
            tk.messagebox.showinfo('info', 'no spec in sf file')
            return
        else:
            with open(utfile,'w') as utoutfile:
                with open(pjtfile,'r') as flist:
                    for atom in specdictlist:
                        if self.specUn.get() == 1:
                            pass
                        if self.utCb.get()==1:
                            utoutfile.write('\n'+atom['SPEC']+'\n'+atom['FILES'])
                            lscheckout.find_UTresult(flist = flist, atom = atom, view = view, utoutfile = utoutfile)
                            pass
#get all fils in view,   mainly for LATEST is open
    def getfiles_from_folder(self):
        t = threading.Thread(target = self.getfiles_sub_thread)
        t.setDaemon(True)
        t.start()
    def getfiles_sub_thread(self):
        view = self.entry_view.get()
        branch = self.entry_branch.get()
        gv = re.findall('gv\d{6}', view)
        outf = proj_path+'\\'+view+'\\'+gv[0]+'_allfiles.txt'
        dirs = ['blois_hmc_code', 'blois_code_p_l', 'blois_soft_vob\Software', 
                'gill_hwi_vob','gill_dcm624_code','gwm_secure_vob', 'gill_vob\\6_coding']
        with open(outf, 'w+') as f:
            for redir in dirs:
                if os.path.exists('X:\\'+view+'\\'+redir):
                    lscheckout.getfolderfiles(redir = redir, view = view, fhandler = f)
                else:
                    print('No diretory X:\\'+view+'\\'+redir)
        self.entry_filelist.delete(0, tk.END)
        self.entry_filelist.insert(0, outf)
    def mkview(self):
        view = self.entry_view.get().replace('\n','')
        base = self.entry_base.get().replace('\n','')
        print(base)
        if view and base:
            lscheckout.makeview(view = view)
        else:
            tk.messagebox.showinfo('info', 'VIEW  or Base cannot be blanket')
        pass
        print(bat_path+'\\bat\\lsview.txt')
        with open(bat_path+'\\bat\\lsview.txt', 'r') as f:   #this is a file of all view, by cmd cleartool lsview 
            line = f.readline()
            while line!='':
                table = re.findall('\S+', line)
                if len(table)>=2:
                    for i in range(len(table)):
                        if table[i] == base:
                            srcfile = table[i+1]+'\\config_spec'
                            tgtfile = NETViewPath+view+'.vws\\config_spec'
                            print(srcfile)
                            print(tgtfile)
                            info = tk.messagebox.askyesno('info',srcfile + '\n'+tgtfile)
                            if info == True:
                                os.system('copy /y '+srcfile+' '+tgtfile)
                                gv = re.findall('gv\d{6}', view)
                                if len(gv)>=1:
                                    os.system('copy '+srcfile+' '+proj_path+'\\'+view+'\\'+gv[0]+'config_spec')
                                else:
                                    pass
                                return
                line = f.readline()

root = tk.Tk()
root.title("ccinterface")
root.geometry("1000x500")
app = Application(master=root)
app.mainloop()
