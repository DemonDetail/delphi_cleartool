my $report_in  = $ARGV[0];
my $report_out = $ARGV[1];
my $cond = "/^E20[2|3]:/";

open(CW_IN,"<",$report_in) || die"cannot open the file: $report_in\n";
open(CW_OUT,">",$report_out) || die"cannot open the file: $report_out\n";

while(<CW_IN>)
{
    if(/^E20[2|3]:/)
    {
        print CW_OUT $_;
    }
}

close(CW_IN);
close(CW_OUT);