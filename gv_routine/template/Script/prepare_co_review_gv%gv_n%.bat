:: ��������review GV��checkout�ļ��Ľű�
:: ͨ������perl�ű�tcg_gv_view.pl��ʵ��
::   tcg_prepare_review_co.pl������������
::     ǰ��������Ϊview name��base label�����ȹ̶�, 
::     ������������Ϊ��Ҫview���ļ��б���ļ���, �ڲ�ͬ�׶����ǲ���ͬ, �����Ҫ�����иýű�ǰ����, ������Ϊcheckout�ļ��б�

:: !!�ڵ��øýű�ǰ����ȷ����Ӧ��checkout�ļ��б������µ�!
:: !!����������ȵ���find_gvXXXXXXXX_co.bat��������checkout�ļ��б�

ccperl ..\Utility\tcg_prepare_review_co.pl %tcg_view_name% %BASE_APP_LABEL% gv%gv_n%_co.txt review_co_gv%gv_n%.bat
