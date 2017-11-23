1.  create view and branch type using: 
      tstart --task=gv225086 --base=
    
2.  make label type:   
      cleartool mklbtype -nc -global TASK_ZHAOY2_GV225086@\dds_admin

3.  modify default Config_Spec created by tstart.

    "element * .../task_zhaoy2_gv225086/LATEST"
mkbranch  task_zhaoy2_gv225086
element * TASK_ZHAOY2_GV225086
    "......" 
end mkbranch task_zhaoy2_gv225086
    
4.  create config_view.cfg file and copy it to necessary vobs.
branche=task_zhaoy2_gv225086 ; label=TASK_ZHAOY2_GV225086

5.  mk label type and branche type for BLOIS project.
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\blois_code_p_l
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\blois_code_p_l
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\blois_soft_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\blois_soft_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\blois_hmc_code
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\blois_hmc_code
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\gill_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\gill_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\hwi_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\hwi_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\gwm_secure_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\gwm_secure_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV225086@\gill_dcm624_code
    cleartool mkbrtype -global -nc task_zhaoy2_gv225086@\gill_dcm624_code

    
        