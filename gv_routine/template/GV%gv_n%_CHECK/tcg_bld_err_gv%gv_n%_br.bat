
:: 1. ��ȡcheckout��.c�ļ���Ӧ��err�ļ���·��, ����·���б��ļ�.
ccperl ..\Utility\tcg_get_err_file_path.pl ..\Script\gv%gv_n%_br.txt .\_temp\gv%gv_n%_err_path.txt

:: 2. �������ļ��ϲ���һ���ļ�.
ccperl ..\Utility\merge_file_context.pl gv%gv_n%_build_err.txt .\_temp\gv%gv_n%_err_path.txt

%cmd_NotePadpp% gv%gv_n%_build_err.txt