:: 用于从TCG项目文件config.py获取源文件列表.
:: 通过调用perl脚本tcg_get_list_from_config.pl来实现.

@set /P _view_name=view name:
@set  _file_list=config_list_%_view_name%.txt
@set  _miss_list=config_list_%_view_name%_miss.txt

@echo view:      X:\%_view_name%

ccperl ..\Utility\tcg_get_list_from_config.pl X:\%_view_name%\gill_vob\6_coding\config.py %_file_list% %_miss_list%

@copy %_file_list%    X:\%_view_name%\gill_vob\6_coding\%_file_list%
@copy %_file_list%    ..\_SI\%_file_list%
@copy %_miss_list%    X:\%_view_name%\gill_vob\6_coding\%_miss_list%
@copy %_miss_list%    ..\_SI\%_miss_list%
