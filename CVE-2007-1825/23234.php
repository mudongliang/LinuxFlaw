<?php

$envelope["from"]= "joe@example.com";
$envelope["to"]  = "foo@example.com";

$part1["type"] = TYPEMULTIPART;
$part1["subtype"] = "mixed";
$part1["type.parameters"] = array("BOUNDARY" => str_repeat("A",8192));

$part2["type"] = TYPETEXT;
$part2["subtype"] = "plain";
$part2["description"] = "description3";
$part2["contents.data"] = "contents.data3\n\n\n\t";

$body[1] = $part1;
$body[2] = $part2;

imap_mail_compose($envelope, $body);

?>
