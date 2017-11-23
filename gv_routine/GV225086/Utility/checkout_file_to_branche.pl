use Cwd;

my $pname   = $ARGV[0];
my $branche = $ARGV[1];

my $cur_dir = get_cur_perl_dir();
# print $cur_dir."\n";
my $get_ver_cmd_head = 'ccperl '.$cur_dir.'\get_file_cc_pname_ve.pl';
my $mk_br_cmd_head   = 'cleartool mkbranch -nc';
my $co_cmd_head      = 'cleartool checkout -nc';

#Step 1. ��ȡ�ļ���ClearCase�еİ汾
my $get_ver_cmd = $get_ver_cmd_head.' '.$pname;
my $return  = qx($get_ver_cmd);
my $exit    = $? >> 8;
my $pname_ve = '';
if( $exit != 0 )
{
    $pname_ve = $return;
}
#print $pname_ve;
#print "\n";

my $real_pname   = '';
my $pname_ve_br  = '';
my $pname_ve_num = '';
if( $pname_ve =~ /(.*?)\@\@(.*?)(\w+)$/)
{
    $real_pname     = $1;
    $pname_ve_br    = $2;
    $pname_ve_num   = $3;
    #print $1."\n";
    #print $2."\n";
    #print $3."\n";
}

#Step 2. �ڵ�ǰ�汾�ϴ�����֧
if( $pname_ve_num =~ /^\d+$/)
{
    my $mk_br_cmd = $mk_br_cmd_head.' '.$branche.' '.$pname_ve;
    my $co_cmd    = $co_cmd_head.' '.$real_pname.'@@'.$pname_ve_br.$branche.'\LATEST';
    print $mk_br_cmd."\n";
    # blois��CC��������Trigger, mkbranche����Զ�checkout.
    # print $co_cmd."\n"; 
}
elsif( ( $pname_ve_num eq 'CHECKEDOUT' ) && 
       ( $pname_ve_br =~ /$branche\\$/ )   )
{
    print '@echo'." !Already Checked Out: \n";
    print '@echo'."    $pname_ve\n";
}
else
{
    print '@echo'." !ERROR, Can't Check Out: \n";
    print '@echo'."    $pname_ve\n";
}

# ��ȡ��ǰperl�ű����ִ��·����·��
# ������"C:\Tool\Script"ִ��run.bat, run.bat����"C:Tool\Utility\perl.pl"
# ��ô��perl.pl�е���������Ӻ�����õ�·����..\Utility
sub get_cur_perl_dir
{
    my $path = $0;
    my $dir = '';
    if($path =~/(.*)[\/|\\]/)
    {
        $dir = $1;
    }
    return $dir;
}

