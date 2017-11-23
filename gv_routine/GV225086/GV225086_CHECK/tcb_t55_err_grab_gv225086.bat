@set   view_dir=X:\C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\\blois_hmc_code\Software\_Software\target_bin
@set t55_report=t55error.txt
@set   t55_grab=gv225086_t55error_grab.txt

ccperl ..\Utility\tcg_qq_grab.pl  %view_dir%\%t55_report% %view_dir%\%t55_grab%

copy %view_dir%\%t55_report%   %~dp0\_temp\%t55_report%
copy %view_dir%\%t55_grab%     %~dp0\_temp\%t55_grab%
copy %view_dir%\%t55_grab%     %~dp0\%t55_grab%

"C:\Program Files (x86)\Beyond Compare 3\BCompare.exe" C:\Users\fzslqx\Documents\Projects\BASE_CHECK_RESULT\t55error_grab_.txt %view_dir%\%t55_grab% 



