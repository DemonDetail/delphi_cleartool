@set   in_view_name=task_zhaoy2_gv142181
@set  in_BASE_LABEL=1EWCHAPP_A320D01
@set   in_file_list=task_gv127510_br_latest.txt
@set    in_out_name=review_task_gv127510_1EWCHAPP_A320D01.bat

ccperl ..\Utility\prepare_compare_base_script.pl %in_view_name% %in_BASE_LABEL% %in_file_list% %in_out_name%
@pause