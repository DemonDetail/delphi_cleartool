
:: 1. ��ȡcheckout��.c�ļ���Ӧ��err�ļ���·��, ����·���б��ļ�.
ccperl ..\Utility\tcg_get_err_file_path.pl ..\Script\gv225086_br.txt .\_temp\gv225086_err_path.txt

:: 2. �������ļ��ϲ���һ���ļ�.
ccperl ..\Utility\merge_file_context.pl gv225086_build_err.txt .\_temp\gv225086_err_path.txt

"C:\Program Files (x86)\Notepad++\notepad++.exe" gv225086_build_err.txt