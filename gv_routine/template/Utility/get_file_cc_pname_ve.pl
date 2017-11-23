# 获取文件在ClearCase中的真实路径, 文件名, 和版本
# 考虑到了ClearCase中的链接. 如果输入路径实际是一个链接, 则先获取其真实路径, 再获取其版本.

# 输入
my $pname   = $ARGV[0];

# 常量配置
my $cc_desc_cmd      = 'cleartool describe ';
my $result = 0; # 0: wrong, 1: pname_ve, 2: link -> real_pname_ve

#Step 1. 获取文件名.
my $fname = '';
my $fpath = '';
if( $pname =~ /(.*?)(\w+\.\w+)\s*$/)
{
    $fpath = $1;
    $fname = $2;
    #print "fpath: $fpath\n";
    #print "fname: $fname\n";
}

#Step 2. 获取文件真实路径和版本
#   如果已经是真实路径, 则直接获取版本. 
#   如果是链接, 则先获取实际文件的路径(real_pname), 然后再获取其版本.
my $cmd_find_version = $cc_desc_cmd.$pname;
my $output = qx($cmd_find_version);
my $exitcode = $? >> 8;
#print $output;
#print "\n";

my $version = '';
my $real_pname = $pname;
if( $output =~ /^version.*?$fname\@\@(.*?)\"/m )
{# version "Z:\blois_hmc_code\Software\S_S\s_s_scheduler\src\s_s_scheduler.c@@\main\sb7033\1myucapp_a\task_chenj_gv149984\CHECKEDOUT"if($output)
    $real_pname = $pname;
    $version = $1;
    $result = 1;    # 1: pname_ve
}
elsif($output =~ /^symbolic link.*?$fname\" -> (.*?)$fname\s*$/m)
{# symbolic link "X:\1myucapp_a200d01_gv149984_chenj\gill_vob\6_coding\src\appli\icv\src\icv.c" -> ../../../../../../blois_soft_vob/Software/Appli/icv/src/icv.c
    $real_pname = $fpath.$1.$fname;
    #print "real_pname: $real_pname\n";
    
    my $cmd_find_version = $cc_desc_cmd.$real_pname;
    my $output = qx($cmd_find_version);
    my $exitcode = $? >> 8;
    #print $output;
    #print "\n";
    
    if( $output =~ /^version.*?$fname\@\@(.*?)\"/m )
    {# version "Z:\blois_hmc_code\Software\S_S\s_s_scheduler\src\s_s_scheduler.c@@\main\sb7033\1myucapp_a\task_chenj_gv149984\CHECKEDOUT"if($output)
        $version = $1;
        $result = 2;    # 2: link -> real_pname_ve
    }
    else
    {
        $real_pname = '';
        $version = '';
        $result = 0;    # 0: wrong
    }
}
else
{
    $real_pname = '';
    $version = '';
    $result = 0;    # 0: wrong
}

#Step 3. 删去真实路径前多余的../../../
my $real_pname_short = $real_pname;

if( $result == 2 )
{# X:\1myucapp_a200d01_gv149984_chenj\gill_vob\6_coding\src\appli\icv\src\../../../../../../blois_soft_vob/Software/Appli/icv/src/icv.c
    $real_pname_short =~ s/\//\\/g;
    #print $real_pname_short."\n";
    my @dirs = ( $real_pname_short =~ /([\w|:|\.]+\\)/g );
    my $dir_num = @dirs;
    #print @dirs;
    #print "\n";
    
    my @dirs_short = ();
    foreach $dir (@dirs)
    {
        if($dir ne '..\\')
        {
            push @dirs_short, $dir;
        }
        else
        {
            pop @dirs_short;
        }
    }
    
    $real_pname_short = '';
    foreach $dir (@dirs_short)
    {
        $real_pname_short .= $dir;
    }
     
    $real_pname_short .= $fname;
}


print $real_pname_short.'@@'.$version;
exit $result;


=cut
open(f_cmd_output, "<", $output_file) || die "cannot open output file $output_file!\n";
my $line_num = 0;
while(<f_cmd_output>)
{
    my $line = $_;
    my $version = '';
    
    if( $line =~ /^version.*?$fname\@\@(.*?)\"/)
    {
        $version = $1;
        print $version;
    }
}
close f_cmd_output;
=end

