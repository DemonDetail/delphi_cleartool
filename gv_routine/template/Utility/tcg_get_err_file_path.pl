# ����.c�ļ��б�, ��tcg�������������ģʽƥ����滻, ���.err�ļ����б�
# ����
#   1. Դ�ļ��б�·��
#   2. �����ļ��б�·��
# ���
#   1. �����ļ��б�


my $scr_path_list = $ARGV[0];
my $err_path_list = $ARGV[1];

open(f_scr_path_list,"<",$scr_path_list) || die"cannot open the file: $!\n";
open(f_err_path_list,">",$err_path_list) || die"cannot open the file: $!\n";
while (<f_scr_path_list>)
{
    my $src_path = $_;
    my $err_path = "";
    
    #\src\dd_difo_injector.c
    if(     $src_path =~ /(.*\\)(src\\([a-zA-Z0-9_]+)\.c)$/
        ||  $src_path =~ /(.*\\)(src\\([a-zA-Z0-9_]+)\.c)\@\@/)
    {        
        my $base_path = "$1";
        my $src_name = "$3";
        
        $err_path = $base_path."out\\".$src_name."\.err";
        print f_err_path_list "$err_path\n";
    }    
}