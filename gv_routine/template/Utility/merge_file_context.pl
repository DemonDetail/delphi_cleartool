my $target_file = $ARGV[0];     # 汇总的log文件的文件名
my $list_file   = $ARGV[1];     # 待合并的log文件的文件名的列表


open my $out, '>', $target_file or die "Could not open '$target_file' for writing $!";
print $out "$target_file:\n";
close $out;
open my $out, '>>', $target_file or die "Could not open '$target_file' for writing $!";

open(f_list, '<',  $list_file) || die "Could not open '$list' for reading $!";

while(<f_list>)
{
    if(/(.*)\n/)
    {
        my $child_file = $1;
        
        open my $in, '<', $child_file or die "Could not open '$child_file' for reading $!";
        local $/ = undef;
        my $context = <$in>;
        close $in;
        
        print $out "\n";
        print $out "************************************************************************************************************\n";
        print $out "$child_file:\n";
        print $out "************************************************************************************************************\n";
        print $out "$context\n";
    }
}

close $out;


# open(f_file_list,"<",$file_list)
# open(my $fh, '>>', 'report.txt')
