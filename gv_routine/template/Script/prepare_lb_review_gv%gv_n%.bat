:: ��������review GV��label�ļ��Ľű�
:: ͨ������perl�ű�tcg_gv_view.pl��ʵ��
::   tcg_prepare_review_lb.pl������������
::     ǰ��������Ϊview name��base label�����ȹ̶�, 
::     ������������Ϊ��Ҫview���ļ��б���ļ���, �ڲ�ͬ�׶����ǲ���ͬ, �����Ҫ�����иýű�ǰ����, ������Ϊlabel�ļ��б�

:: !!�ڵ��øýű�ǰ����ȷ����Ӧ��label�ļ��б������µ�!
:: !!����������ȵ���find_gvXXXXXXXX_lb.bat��������label�ļ��б�

ccperl ..\Utility\tcg_prepare_review_lb.pl %tcg_view_name% %BASE_APP_LABEL% gv%gv_n%_lb.txt review_lb_gv%gv_n%.bat