my $target_file  = $ARGV[0];     # 汇总的log文件的文件名
my $list_file    = $ARGV[1];     # 待合并的log文件的文件名的列表
my $src_ref_path = $ARGV[2];     # 文件列表的根目录


open my $out, '>', $target_file or die "Could not open '$target_file' for writing $!";
print $out "$target_file:\n";
close $out;
open my $out, '>>', $target_file or die "Could not open '$target_file' for writing $!";

open(f_list, '<',  $list_file) || die "Could not open '$list' for reading $!";

my $i = 0;

while(<f_list>)
{
    if(/(.*)\n/)
    {
        my $child_file = $1;
        my $error_file = $1;
        
        if($child_file =~ /\.c$/)
        {
            print '>';
            if(++$i >= 25)
            {
                $i = 0;
                print "\n";
            }
            
            # \src\ -> \out\
            # .c -> .err
            $error_file =~ s/\\src\\/\\out\\/g;
            $error_file =~ s/\.c$/\.err/g;
            $error_file = $src_ref_path.$error_file;
            
            #print 'error file: '.$error_file."\n";
            
            if(open my $in, '<', $error_file)
            {
                local $/ = undef;
                my $context = <$in>;
                close $in;
                
                print $out "\n";
                print $out "************************************************************************************************************\n";
                print $out "$error_file:\n";
                print $out "************************************************************************************************************\n";
                print $out "$context\n";
            }
            else
            {
                print "\nCould not open '$error_file' for reading $!\n";
            }

        }
    }
}

print "\n";

close $out;


# open(f_file_list,"<",$file_list)
# open(my $fh, '>>', 'report.txt')
