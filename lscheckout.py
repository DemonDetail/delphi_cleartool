#!/usr/bin/python3
import re
import os
import sys
import tkinter.messagebox

labelname = 'TASK_ZHAOY2_'
bat_path = "C:\\D\\Tools\\lscheckout"
proj_path = "C:\\D\\Project\\tool_proj"
driverletter = 'X:\\'
NETViewPath = '\\\\CNSHGCTC-AP07\\views\ASIA\\bjq5dl\\'


def lscheckout(view = None):
    curpath = proj_path+'\\'+view
    # os.remove(curpath+"\\checkout.log")
    os.system(bat_path+"\\bat\\lscheckout.bat "+ "X:\\"+view+" >"+curpath+"\\checkout.log")
    f = open(curpath+"\\checkout.log", 'r')
    fw = open(curpath+"\\lscheckout.txt", 'w')
    line = f.readline()
    while line != "":
        r = re.search(r'checkout version \"(.*?)\"',line)
        if r is None:
            pass
        else:
            #print(r.group(0))
            rversion = re.search(r'from \\(.*?)\\[0-9]{1,3} ',line)
            if rversion is None:
                version = ' not found'
            else:
                version = rversion.group(0)[5:-1]
            fw.write(r.group(0)[18:-1] + '@@'+ version +'\n')
        line = f.readline()
    f.close()
    fw.close()   
def find_br( branch = None, view = None):
    # curpath = os.getcwd()
    # os.remove(curpath+"\\checkout.log")
    outpath = proj_path+'\\'+view
    print(outpath)
    if branch and view  :
        os.system(bat_path+"\\bat\\find_br.bat " + branch + " " + view + " "+ outpath)
    else: 
        print("error:  no branch or no view ")
def find_lb(label = None , view = None):
    # curpath = os.getcwd()
    # os.remove(curpath+"\\checkout.log")
    outpath = proj_path+'\\'+view    
    if label and view  :
        os.system(bat_path+"\\bat\\find_br.bat " + label + " " + view + " "+ outpath)
    else: 
        print("error:  no branch or no view ")
def des_attr(file = None):
    result = None
    ser = re.search(r'X:\\ ',file)
    if ser:
        cmd = r"cleartool describe -aattr CtcSpecLabel -short "
        if file:
            cmd = cmd + file
            r = os.popen(cmd)
            result = r.read()
            r.close()
        else:
            result = None
    return result
# def lsvtree(file = None ):
def getFile_1x( line = None):
    fileattr = [r'ProjectFile',r'SourceFile',r'AsmFile',r'HeaderFile',r'T55File']
    for head in fileattr:
        r = re.search(head + r'\(\'([^\']*)\'',line)
        if r is None:
            pass
        else:
            length = len(head)+2
            # outfile.write(r.group(0)[length:-1].replace('/','\\')+"\n")
            break
    return('\\gill_vob\\6_coding\\' + r.group(0)[length:-1].replace('/','\\'))
def getFileList_1x(file = None, outpath = None):
    with open(outpath,'w+') as outfile: 
        fileattr = [r'ProjectFile',r'SourceFile',r'AsmFile',r'HeaderFile',r'T55File']
        print(file)
        if file != None:
            with open(file) as f:
                line = f.readline()
                while line != "":
                    for head in fileattr:
                        r = re.search(head + r'\(\'([^\']*)\'',line)
                        if r is None:
                            pass
                        else:
                            length = len(head)+2
                            outfile.write('\\gill_vob\\6_coding\\'+r.group(0)[length:-1].replace('/','\\')+"\n")
                            break
                    line = f.readline()
def getFile_1m( line = None):
    return('\\blois_hmc_code\\Software\\Environnement\\codewright\\'+line)
def getFileList_1m( file = None, outpath = None):
    print(file)
    print(outpath)
    with open(outpath,'w+') as outfile: 
        if file != None:
            with open(file) as f:
                line = f.readline().replace('\n','')
                while line != "":
                    line = line.replace('\n','')
                    s = line.split('\\')
                    # print(s)
                    if s[0] == '..':
                        if len(s)>=4 and s[3] =='..':
                            out = line.replace('..\..\..\..','')
                        elif len(s)>=3 and s[2] == '..':
                            out =line.replace('..\..\..', '\\blois_hmc_code')
                        elif len(s)>=2 and s[1] == '..':
                            out =line.replace('..\..', '\\blois_hmc_code\\Software')
                        outfile.write(out + '\n')              
                    line = f.readline()
def multigetFileList(file = None, outpath = None):
    ext = file.split('\\')[-1].split('.')[-1]
    print(file)
    print(outpath)
    if ext == 'py':
        return getFileList_1x(file = file, outpath = outpath)
    elif ext == 'pjt':
        return getFileList_1m(file = file, outpath = outpath)
    else:
        return 
def getvtree(file = None, path = None ):
    if file and path:
        outfile = path + '\\' + file.split('\\')[-1]+ '.vtree'
        cmd = 'cleartool lsvtree -a ' + file + ' > ' + outfile
        print(cmd)
        os.system(cmd)
    # print(outfile)
    return(outfile)
def alyfile_sf(file = None):
    with open(file) as f:
        all_text = f.read()
        all_text = all_text.replace('\n','').replace(' ','').replace('\t','')
        # print(all_text)
        obj = re.findall(r'\{(.*?[^\{}])\}', all_text)
        li = []
        di = {}                            #convert obj to dict in list
        for i in obj:
            # print(i)
            predi = i.split(';')
            di = {}
            for j in predi:
                atom = j.split('=')
                di[atom[0]] = atom[1]
            li.append(di)
        for i in li:
            print(i)
        return(li)
def findtarget(listfile= None, dictlist = None, view = None, outfile = None):
    gv = re.findall('gv\d{6}', view)
    if len(gv)>=1:
        mklabelStr = 'cleartool mklabel -rep '+labelname+gv[0].upper()+'  '
        checkoutStr = 'cleartool checkout -c \"comment\" '
        mkCtclabel = 'cleartool mkattr       CtcSpecLabel   '
    with open(outfile, 'w+') as outfile:
        with open(listfile,'r') as lf:
            for di in dictlist:
                files = []
                lf.seek(0)
                outfile.write('/*\n'+di['SPEC']+'\n')
                outfile.write(di['LABEL']+'\n*/\n')
                line = lf.readline().replace('\n','')
                while line != '':
                    result = re.findall(di['FILES'],line)
                    if result:
                        files.append(line)
                    else:
                        pass
                    line = lf.readline().replace('\n','')
                if files == []:
                    outfile.write('!!There is NO corresponding file in project file list \n')
                for viapath in files:
                    absfilepath = driverletter +view  + viapath
                    vtreefolder = proj_path + '\\' + view +'\\'+'vtree'
                    vtreefile = getvtree(file = absfilepath, path =vtreefolder)
                    print(vtreefile)
                    with open(vtreefile, 'r') as vf:
                        line = vf.readline()
                        foundFile = False
                        while line != '':
                            line = line.replace('\n','')
                            writeline = ''
                            out = ''
                            if di['LABEL']!='None' and re.findall(di['LABEL'],line) :     #re.findall(di['LABEL'],line): 
                                # outfile.write(line+'\n')
                                writeline = line+'\n'
                                foundFile = True
                            elif re.findall(di['SPEC'].lower()+'\\\\[0-9]+',line):
                                # outfile.write(line+'\n')
                                writeline = line+'\n'
                                foundFile = True
                            else:
                                pass
                            if writeline!='' and ('ATTR' in di.keys()) and len(gv)>=1:
                                if di['ATTR'] == 'R':
                                    temp = re.findall('(\S.*)@@',writeline)
                                    try:
                                        out = mklabelStr+ temp[0]+'@@\\main\\0'
                                    except Exception as e:
                                        print(writeline)
                                        print(e)
                                elif di['ATTR'] == 'U' or di['ATTR'] == 'A':
                                    try:
                                        out = mklabelStr+ writeline
                                    except Exception as e:
                                        print(writeline)
                                        print(e)
                            outfile.write(out)
                            line = vf.readline()
                        if foundFile==False:
                            outfile.write('!!Do not find LABEL or SPEC No.\n')
                            outfile.write(checkoutStr + absfilepath+'\n')
                            outfile.write(mkCtclabel +'\"\\\"'+di['SPEC'].upper()+'\"\\\"  '+absfilepath+'\n')
                outfile.write('\n\n')     #  need gap between 2 SPECs
def getfolderfiles(redir = None, view = None, fhandler = None):
    dir = 'X:\\'+view+'\\'+redir
    print(dir)
    flist = os.listdir(dir)
    for f in flist:
        if os.path.isdir(dir+'\\'+f):
            if f != 'tests':
                getfolderfiles(redir+'\\'+f, view = view, fhandler = fhandler)
        else:
            ext = f.split('.')
            if len(ext)>=2 and ext[-1] != 'o' and ext[-1]!='i' and ext[-1]!='log' and ext[-1]!='doc':
                fhandler.write(redir+'\\'+f + '\n')
                print(redir+'\\'+f )
def makeview(view = None):
    outp = bat_path+'\\bat\\lsview.txt'
    print(outp)
    if  view  :
        os.system(bat_path+"\\bat\\mkview.bat " + view + " " +outp+ ' '+NETViewPath)
    else: 
        print("error:  no view ")
    pass
def find_UTresult(flist = None, atom =None , view = None, utoutfile = None):
    specdir = proj_path + '\\' + view +'\\'+'SPEC'+'\\'+atom['SPEC']
    if os.path.exists(specdir) == False:
        try:
            os.mkdir(specdir)
        except Exception as e:
            tk.messagebox.showinfo('error', e)
    cmdout = proj_path+'\\'+view+'\\'+'SPEC'+'\\'+atom['SPEC']+'\\'+atom['FILES']+'.ahlink'
    if flist and atom and view:
        flist.seek(0)
        line = flist.readline()
        while line!='':
            line = line.replace('\n', '')
            fnames = atom['FILES'].split(',')
            result = re.findall(fnames[0]+'.c',line)
            for i in fnames:
                if -1 != i.find('.c'):
                    result = re.findall(i,line)
                    break
            if len(result)>=1:
                file = 'X:\\'+view+line
                cmd = bat_path+'\\bat\\des_l.bat '+file +'  ' +cmdout
                print(cmd)
                os.system(cmd)
                extractinfo = analysisfile_des_l(cmdout)
                utattr = ['POLY_Link','tcgTestResultPS', 'RTRT_Link', 'tcgTestResultRTRT', 'Merge']
                for attr in utattr:
                    if (attr in extractinfo.keys()):
                        utoutfile.write(attr+': ' + extractinfo[attr]+'\n')
                    else:
                        utoutfile.write('Not find  '+ attr+'\n')
            line = flist.readline()
        pass
def analysisfile_des_l(file = None):          # used to extract information from  .ahlink file of view file
    ext_info = {}
    with open(file, 'r') as inf:
        line = inf.readline()
        while line!='':
            line = line.replace('\n','')
            split = re.findall('\S+',line)
            if len(split)>=1:
                if split[0] == 'version':
                    ext_info['VERSION'] = split[1].replace('\"','')
                elif split[0]=='Labels:':
                    pass
                elif split[0] =='CtcSpecLabel':
                    try:
                        ext_info['CtcSpecLabel'] = split[2].replace('\"','') 
                    except Exception as e:
                        print(e)
                elif  -1 != split[0].find('Merge') :
                    split = line.split('<-')
                    try:
                        if 'Merge' in ext_info.keys():
                            ext_info['Merge'] = ext_info['Merge']+line+'\n'
                        else:
                            ext_info['Merge'] = line+'\n'
                    except Exception as e:
                        print(e)
                elif  -1 != split[0].find('tcgTestResultRTRT') :
                    split = line.split('->')
                    try:
                        ext_info['tcgTestResultRTRT'] = line   #split[1].replace('\"','').replace(' ','')
                    except Exception as e:
                        print(e)
                elif  -1 != split[0].find('tcgTestResultPS') :
                    split = line.split('->')
                    try:
                        ext_info['tcgTestResultPS'] = line   #split[1].replace('\"','').replace(' ','')
                    except Exception as e:
                        print(e)                                     
                elif  -1 != split[0].find('RTRT_Link') :
                    split = line.split('->')
                    try:
                        ext_info['RTRT_Link'] =  re.findall('-> \S+',line)[0].replace('-> ','')
                    except Exception as e:
                        print(e)
                elif  -1 != split[0].find('POLY_Link') :
                    split = line.split('->')
                    try:
                        ext_info['POLY_Link'] =  re.findall('-> \S+',line)[0].replace('-> ','')
                    except Exception as e:
                        print(e)       
                elif  -1 != split[0].find('PSTR_Link') :         
                    split = line.split('->')
                    try:
                        ext_info['PSTR_Link'] =  re.findall('-> \S+',line)[0].replace('-> ','')
                    except Exception as e:
                        print(e)            
            line = inf.readline()
        print(ext_info)
    return(ext_info)
    pass

if __name__=="__main__":
    pass
    # lscheckout()
    # find_br(branch = 'task_gv217878', view = 'TASK_ZHAOY2_Compare')
    # getFileList_1x(file = "C:\\D\\Tools\\lscheckout\\config.py" , outpath = "C:\\D\\Tools\\lscheckout\\config_filelist.txt")
    # alyfile_sf('C:\\D\\Tools\\lscheckout\\spec_file_gvxxxx.sf')
    # rf = getvtree(file = 'X:\\1xyunapp_b100p11_gv224799_zhaoy2\\gill_vob\\6_coding\\src\\p_l\\p_l_pwm_output\\src\\p_l_imv_drv_diag.c',path =proj_path)
    # print(rf
    # a = alyfile_sf(file= 'C:\\D\\Tools\\lscheckout\\spec_file_gvxxxx.sf' )
    # findtarget(listfile= 'C:\\D\\Tools\\proj_test\\filelist.txt', dictlist = a , viewpath = 'X:\\1xyunapp_b100p11_gv224799_zhaoy2\\gill_vob\\6_coding')
     # getfolderfiles('X:\\1mqmcapp_a310d21_gv225086_zhaoy2\\blois_hmc_code')
# re.findall('SPEC=\s*([A-Za-z]{1}\d{7}_\d+\.\d+)', s)
    analysisfile_des_l('C:\\D\\Project\\tool_proj\\1xyunapp_b100p11_gv224799_zhaoy2\\SPEC\\A0108494_1.0\\p_l_imv_drv_diag.ahlink')

# import os, re
# # execute command, and return the output
# def execCmd(cmd):
#   r = os.popen(cmd)
#   text = r.read()
#   r.close()
#   return text
# # write "data" to file-filename
# def writeFile(filename, data):
#   f = open(filename, "w")
#   f.write(data)
#   f.close()
# # 获取计算机MAC地址和IP地址
# if __name__ == '__main__':
#   cmd = "ipconfig /all"
#   result = execCmd(cmd)
#   pat1 = "Physical Address[\. ]+: ([\w-]+)"
#   pat2 = "IP Address[\. ]+: ([\.\d]+)"
#   MAC = re.findall(pat1, result)[0]    # 找到MAC
#   IP = re.findall(pat2, result)[0]    # 找到IP
#   print("MAC=%s, IP=%s" %(MAC, IP))