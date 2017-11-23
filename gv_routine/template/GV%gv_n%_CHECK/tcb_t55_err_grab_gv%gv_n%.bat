@set   view_dir=X:\%tcg_view_name%\blois_hmc_code\Software\_Software\target_bin
@set t55_report=t55error.txt
@set   t55_grab=gv%gv_n%_t55error_grab.txt

ccperl ..\Utility\tcg_qq_grab.pl  %view_dir%\%t55_report% %view_dir%\%t55_grab%

copy %view_dir%\%t55_report%   %~dp0\_temp\%t55_report%
copy %view_dir%\%t55_grab%     %~dp0\_temp\%t55_grab%
copy %view_dir%\%t55_grab%     %~dp0\%t55_grab%

%cmd_BeyondCompare% %BASE_CHECK_RESULT_PATH%\t55error_grab_%BASE_APP_LABEL%.txt %view_dir%\%t55_grab% 



