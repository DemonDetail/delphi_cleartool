@set output=blois_co_s_s.bat
@echo. >%output%

ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_scheduler\src\s_s_scheduler.c           %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_scheduler\src\s_s_scheduler.h           %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\target_bin\t55error.txt               %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\target_bin\%BASE_APP_LABEL%.api       %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\target_bin\%BASE_APP_LABEL%.t55       %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_fault_manager\src\F_M_Fault.c           %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\S_S\s_s_fault_manager\src\F_M_Fault.h           %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_soft_vob\Software\S_S\s_s_fault_manager\src\F_M_Rbm_Structure.c   %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_soft_vob\Software\S_S\s_s_fault_manager\src\F_M_Rbm_Structure.h   %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\Appli\dti\src\dti.c                             %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\Appli\dti\src\dti.h                             %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\Arbitration.t55                   %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\calib_original.h                  %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\calib.h                           %gv_branche% >> %output%
ccperl ..\Utility\checkout_file_to_branche.pl Z:\blois_hmc_code\Software\_Software\src\pack_id.c                         %gv_branche% >> %output%

@pause
