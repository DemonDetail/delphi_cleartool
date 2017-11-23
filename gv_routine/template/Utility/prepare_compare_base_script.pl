# ���ɱȽ�һЩ���ļ��Ľű� #
# ����:
# 1. view������
# 2. base��LABEL
#       ����׼��LABEL��.
# 3. ��Ҫ��review���ļ����ļ��б�
# 4. ����ļ���
# ���:
#       ���ڱȽ��ļ���bat�ļ�.


use strict;
use warnings;

my $view_name    = $ARGV[0];
my $base_lb      = $ARGV[1];
my $file_list    = $ARGV[2];
my $output       = $ARGV[3];

my $file_num = 0;
my %Files = ();

open(f_file_list,"<",$file_list) || die"cannot open the file: $file_list!\n";
open(f_output,">",$output) || die"cannot open the file: $output!\n";
while (<f_file_list>)
{
#   \gill_vob\6_coding\config_wch_etc27.py@@\main\sg7505_ctc\BR_1EWCH_A_CTC\task_zhouj_gv140370\1
#   ƥ���һ��'\'��'/', ����Ӧ��ͬ��·��: 'Z:\' 'Y:\' 'X:\task_chenj_gvXXXXXX\'
#   X:\...\...\...
#   .\...\...
#   \....
#   V:\....
    my $line = $_;
    my $path_full = "";
    my $path      = "";
    my $file_name = "";
    my $remain_str= "";
    my $ver  = "";
    if(   $line =~ /\s*([A-Za-z]:\\(([a-zA-Z0-9_]+\\)+)([a-zA-Z0-9_\.]+))(.*)/
       || $line =~        /\s*(\.\\(([a-zA-Z0-9_]+\\)+)([a-zA-Z0-9_\.]+))(.*)/
       || $line =~          /\s*(\\(([a-zA-Z0-9_]+\\)+)([a-zA-Z0-9_\.]+))(.*)/ )
    {
        $path_full = $1;
        $path      = $2;
        $file_name = $4;
        $remain_str= $5;
        
        if( $remain_str =~ /(\@\@.*)/)
        {
            $ver = $1;  #ver start with @@
        }
        elsif( $remain_str =~ /\s*/)
        {
            $ver = "";
        }
        
        #����ͬ��ʽ��·��ͳһ�滻Ϊ"X:\view_name\"���͵�·��.
        $path_full =~ s/^[\\\/]/X:\\$view_name\\/;           #   \gill_vob\...   -> X:\task_chenj_gvXXXXXX\gill_vob
        $path_full =~ s/^\.[\\\/]/X:\\$view_name\\/;         #  .\gill_vob\...   -> X:\task_chenj_gvXXXXXX\gill_vob
        $path_full =~ s/^[A-WYZ]:[\\\/]/X:\\$view_name\\/;   # Y:\gill_vob\...   -> X:\task_chenj_gvXXXXXX\gill_vob
        
        $file_num = $file_num + 1;
        print "$path_full  $ver\n";
        print f_output "cleartool diff -g $path_full\@\@\\$base_lb  $path_full$ver & pause\n";
        $Files{$path} = $ver;
    }
}
print "total: $file_num\n";

close f_file_list;
close f_output;