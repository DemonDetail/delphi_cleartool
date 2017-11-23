@set   view_dir=X:\%tcg_view_name%\gill_vob\6_coding
@set qac_report=gv%gv_n%_quick_qac_result.txt
@set   qac_grab=gv%gv_n%_qq_grab.txt

ccperl ..\Utility\tcg_qq_grab.pl  %view_dir%\%qac_report% %view_dir%\%qac_grab%

copy %view_dir%\%qac_report%   %~dp0\_temp\%qac_report%
copy %view_dir%\%qac_grab%     %~dp0\_temp\%qac_grab%
copy %view_dir%\%qac_grab%     %~dp0\%qac_grab%

%cmd_BeyondCompare% %BASE_CHECK_RESULT_PATH%\quick_qac_grab_%BASE_APP_LABEL%.txt %view_dir%\%qac_grab% 



