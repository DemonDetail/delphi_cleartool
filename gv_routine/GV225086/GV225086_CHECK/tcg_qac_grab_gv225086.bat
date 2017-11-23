@set   view_dir=X:\C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\\gill_vob\6_coding
@set qac_report=gv225086_quick_qac_result.txt
@set   qac_grab=gv225086_qq_grab.txt

ccperl ..\Utility\tcg_qq_grab.pl  %view_dir%\%qac_report% %view_dir%\%qac_grab%

copy %view_dir%\%qac_report%   %~dp0\_temp\%qac_report%
copy %view_dir%\%qac_grab%     %~dp0\_temp\%qac_grab%
copy %view_dir%\%qac_grab%     %~dp0\%qac_grab%

"C:\Program Files (x86)\Beyond Compare 3\BCompare.exe" C:\Users\fzslqx\Documents\Projects\BASE_CHECK_RESULT\quick_qac_grab_.txt %view_dir%\%qac_grab% 



