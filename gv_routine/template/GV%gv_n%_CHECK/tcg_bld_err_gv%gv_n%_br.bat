
:: 1. 获取checkout的.c文件对应的err文件的路径, 生成路径列表文件.
ccperl ..\Utility\tcg_get_err_file_path.pl ..\Script\gv%gv_n%_br.txt .\_temp\gv%gv_n%_err_path.txt

:: 2. 将错误文件合并到一个文件.
ccperl ..\Utility\merge_file_context.pl gv%gv_n%_build_err.txt .\_temp\gv%gv_n%_err_path.txt

%cmd_NotePadpp% gv%gv_n%_build_err.txt