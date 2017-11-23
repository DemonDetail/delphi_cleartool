1.  create view and branch type using: 
      tstart --task=gv%gv_n% --base=%BASE_APP_LABEL%
    
2.  make label type:   
      cleartool mklbtype -nc -global TASK_ZHAOY2_GV%gv_n%@\dds_admin

3.  modify default Config_Spec created by tstart.

    "element * .../task_zhaoy2_gv%gv_n%/LATEST"
mkbranch  task_zhaoy2_gv%gv_n%
element * TASK_ZHAOY2_GV%gv_n%
    "......" 
end mkbranch task_zhaoy2_gv%gv_n%
    
4.  create config_view.cfg file and copy it to necessary vobs.
branche=task_zhaoy2_gv%gv_n% ; label=TASK_ZHAOY2_GV%gv_n%

5.  mk label type and branche type for BLOIS project.
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\blois_code_p_l
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\blois_code_p_l
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\blois_soft_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\blois_soft_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\blois_hmc_code
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\blois_hmc_code
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\gill_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\gill_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\hwi_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\hwi_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\gwm_secure_vob
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\gwm_secure_vob
    cleartool mklbtype -global -nc TASK_ZHAOY2_GV%gv_n%@\gill_dcm624_code
    cleartool mkbrtype -global -nc task_zhaoy2_gv%gv_n%@\gill_dcm624_code

    
        