@set output=blois_co_s_s.bat
@echo. >%output%

ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_scheduler\src\s_s_scheduler.c           task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_scheduler\src\s_s_scheduler.h           task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\target_bin\t55error.txt               task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\target_bin\.api       task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\target_bin\.t55       task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_fault_manager\src\F_M_Fault.c           task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_fault_manager\src\F_M_Fault.h           task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_soft_vob\Software\S_S\s_s_fault_manager\src\F_M_Rbm_Structure.c   task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_soft_vob\Software\S_S\s_s_fault_manager\src\F_M_Rbm_Structure.h   task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\Appli\dti\src\dti.c                             task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\Appli\dti\src\dti.h                             task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\Arbitration.t55                   task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\calib_original.h                  task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\calib.h                           task_zhaoy2_gv225086 >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\pack_id.c                         task_zhaoy2_gv225086 >> %output%

@pause
