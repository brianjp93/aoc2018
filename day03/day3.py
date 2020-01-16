"""day3.py
"""

dat = '''
#1 @ 749,666: 27x15
#2 @ 118,560: 22x18
#3 @ 194,731: 16x29
#4 @ 295,407: 21x29
#5 @ 717,30: 29x24
#6 @ 969,722: 11x25
#7 @ 117,596: 20x22
#8 @ 557,190: 19x17
#9 @ 445,84: 22x24
#10 @ 527,900: 28x12
#11 @ 48,71: 20x17
#12 @ 644,603: 29x16
#13 @ 786,478: 19x10
#14 @ 40,483: 14x15
#15 @ 683,475: 22x13
#16 @ 173,683: 10x10
#17 @ 862,778: 12x29
#18 @ 169,513: 20x13
#19 @ 151,719: 28x13
#20 @ 49,342: 15x29
#21 @ 678,900: 13x29
#22 @ 97,522: 6x16
#23 @ 888,500: 11x21
#24 @ 781,576: 12x22
#25 @ 122,367: 28x18
#26 @ 625,149: 22x27
#27 @ 668,803: 15x11
#28 @ 822,317: 26x15
#29 @ 685,945: 19x11
#30 @ 786,296: 13x18
#31 @ 848,839: 15x16
#32 @ 663,448: 28x24
#33 @ 941,785: 13x24
#34 @ 579,902: 26x11
#35 @ 343,206: 19x11
#36 @ 301,174: 27x12
#37 @ 539,52: 16x20
#38 @ 740,676: 17x26
#39 @ 771,191: 11x18
#40 @ 80,930: 22x29
#41 @ 402,979: 16x18
#42 @ 978,896: 14x27
#43 @ 299,185: 20x24
#44 @ 885,32: 20x25
#45 @ 28,376: 13x26
#46 @ 103,323: 22x22
#47 @ 495,160: 18x14
#48 @ 318,567: 13x20
#49 @ 206,353: 11x13
#50 @ 763,100: 21x13
#51 @ 852,973: 18x12
#52 @ 50,249: 20x26
#53 @ 329,579: 11x11
#54 @ 546,884: 12x16
#55 @ 425,681: 18x18
#56 @ 152,610: 17x16
#57 @ 802,735: 29x21
#58 @ 113,567: 22x18
#59 @ 361,386: 27x25
#60 @ 921,9: 25x19
#61 @ 68,903: 23x21
#62 @ 368,599: 16x25
#63 @ 553,182: 11x16
#64 @ 391,822: 26x28
#65 @ 589,207: 12x20
#66 @ 188,348: 23x22
#67 @ 499,43: 16x21
#68 @ 849,175: 14x10
#69 @ 650,527: 20x10
#70 @ 108,72: 11x25
#71 @ 685,124: 12x29
#72 @ 364,370: 25x10
#73 @ 578,357: 18x24
#74 @ 514,961: 25x28
#75 @ 376,981: 22x11
#76 @ 96,496: 16x17
#77 @ 682,6: 14x13
#78 @ 191,804: 17x19
#79 @ 202,556: 28x23
#80 @ 390,525: 11x20
#81 @ 836,610: 22x20
#82 @ 566,79: 22x28
#83 @ 441,68: 16x12
#84 @ 270,609: 12x10
#85 @ 520,392: 20x16
#86 @ 104,416: 23x26
#87 @ 104,763: 22x16
#88 @ 669,877: 11x24
#89 @ 277,658: 27x12
#90 @ 909,134: 25x14
#91 @ 414,925: 29x28
#92 @ 304,618: 15x23
#93 @ 838,975: 23x14
#94 @ 761,377: 19x26
#95 @ 923,178: 11x10
#96 @ 901,945: 22x20
#97 @ 179,325: 18x24
#98 @ 877,792: 27x17
#99 @ 870,233: 24x24
#100 @ 945,390: 13x14
#101 @ 697,868: 10x19
#102 @ 823,154: 19x27
#103 @ 444,900: 16x27
#104 @ 538,45: 25x14
#105 @ 90,423: 15x10
#106 @ 425,822: 26x19
#107 @ 968,167: 20x21
#108 @ 721,420: 25x12
#109 @ 516,30: 27x29
#110 @ 316,565: 11x13
#111 @ 379,278: 26x16
#112 @ 940,770: 13x24
#113 @ 429,913: 16x18
#114 @ 278,174: 25x20
#115 @ 659,232: 22x16
#116 @ 482,36: 20x10
#117 @ 162,410: 19x11
#118 @ 160,949: 21x27
#119 @ 48,268: 15x17
#120 @ 50,512: 12x27
#121 @ 215,330: 26x12
#122 @ 504,400: 28x28
#123 @ 129,529: 21x18
#124 @ 160,370: 26x19
#125 @ 955,275: 21x29
#126 @ 576,320: 13x28
#127 @ 492,955: 24x29
#128 @ 111,918: 24x17
#129 @ 654,910: 13x10
#130 @ 390,607: 21x23
#131 @ 498,581: 16x21
#132 @ 1,126: 20x24
#133 @ 108,809: 4x3
#134 @ 600,572: 13x29
#135 @ 67,717: 21x27
#136 @ 387,392: 21x15
#137 @ 510,44: 10x15
#138 @ 940,137: 10x26
#139 @ 375,506: 18x10
#140 @ 825,669: 18x10
#141 @ 528,338: 24x13
#142 @ 657,492: 20x28
#143 @ 659,677: 3x6
#144 @ 885,878: 16x24
#145 @ 310,214: 26x27
#146 @ 947,823: 13x17
#147 @ 10,222: 18x26
#148 @ 56,575: 24x16
#149 @ 646,914: 16x20
#150 @ 313,512: 18x16
#151 @ 321,622: 24x17
#152 @ 937,195: 21x14
#153 @ 386,23: 18x26
#154 @ 922,148: 18x29
#155 @ 126,45: 20x27
#156 @ 590,14: 13x11
#157 @ 538,739: 22x18
#158 @ 497,171: 24x21
#159 @ 824,484: 12x21
#160 @ 329,843: 23x28
#161 @ 163,179: 22x18
#162 @ 160,98: 18x22
#163 @ 664,1: 24x17
#164 @ 414,502: 21x12
#165 @ 15,792: 11x20
#166 @ 454,169: 12x27
#167 @ 260,924: 24x14
#168 @ 565,223: 13x15
#169 @ 247,165: 20x13
#170 @ 72,41: 23x26
#171 @ 640,265: 28x24
#172 @ 150,867: 28x18
#173 @ 478,577: 21x29
#174 @ 654,695: 13x25
#175 @ 426,674: 23x17
#176 @ 664,290: 19x5
#177 @ 427,509: 10x14
#178 @ 349,382: 21x21
#179 @ 416,582: 17x25
#180 @ 340,270: 22x10
#181 @ 835,750: 15x12
#182 @ 944,548: 11x22
#183 @ 590,509: 17x11
#184 @ 378,224: 13x15
#185 @ 682,283: 28x19
#186 @ 607,82: 26x15
#187 @ 604,468: 28x15
#188 @ 719,127: 29x28
#189 @ 319,15: 22x26
#190 @ 119,285: 13x14
#191 @ 235,512: 26x24
#192 @ 191,473: 11x20
#193 @ 0,840: 10x27
#194 @ 617,528: 21x16
#195 @ 206,474: 24x11
#196 @ 285,197: 20x19
#197 @ 347,352: 15x22
#198 @ 412,735: 26x20
#199 @ 372,931: 23x15
#200 @ 461,497: 13x28
#201 @ 689,943: 28x12
#202 @ 621,93: 26x25
#203 @ 897,795: 12x13
#204 @ 652,648: 11x21
#205 @ 259,367: 11x26
#206 @ 43,187: 26x22
#207 @ 170,194: 27x29
#208 @ 539,760: 22x22
#209 @ 404,291: 20x29
#210 @ 782,419: 25x27
#211 @ 613,61: 3x10
#212 @ 821,325: 16x21
#213 @ 65,689: 12x11
#214 @ 303,270: 24x24
#215 @ 836,463: 17x17
#216 @ 1,643: 23x15
#217 @ 953,540: 13x28
#218 @ 140,530: 28x27
#219 @ 625,447: 12x13
#220 @ 492,638: 26x21
#221 @ 156,711: 10x12
#222 @ 35,699: 17x27
#223 @ 301,187: 14x24
#224 @ 805,618: 23x11
#225 @ 550,881: 11x21
#226 @ 209,536: 24x20
#227 @ 181,331: 14x26
#228 @ 849,922: 15x19
#229 @ 100,832: 12x18
#230 @ 224,410: 6x6
#231 @ 437,952: 17x25
#232 @ 299,494: 16x22
#233 @ 37,9: 14x19
#234 @ 177,563: 22x18
#235 @ 152,230: 17x11
#236 @ 18,250: 16x28
#237 @ 759,373: 28x24
#238 @ 202,724: 24x18
#239 @ 291,769: 10x12
#240 @ 816,908: 27x21
#241 @ 228,198: 11x18
#242 @ 164,233: 27x11
#243 @ 957,624: 27x24
#244 @ 840,726: 29x24
#245 @ 4,797: 24x12
#246 @ 172,879: 15x17
#247 @ 972,905: 14x27
#248 @ 674,845: 10x15
#249 @ 846,573: 21x21
#250 @ 806,277: 20x29
#251 @ 812,900: 22x12
#252 @ 147,361: 24x20
#253 @ 865,723: 18x18
#254 @ 416,125: 21x22
#255 @ 899,831: 13x18
#256 @ 570,189: 20x21
#257 @ 302,498: 15x28
#258 @ 360,65: 15x14
#259 @ 178,394: 18x25
#260 @ 543,744: 13x24
#261 @ 746,590: 23x12
#262 @ 803,586: 26x26
#263 @ 381,559: 26x14
#264 @ 513,391: 14x19
#265 @ 647,20: 17x21
#266 @ 611,53: 11x26
#267 @ 60,387: 22x21
#268 @ 118,142: 19x11
#269 @ 550,816: 25x19
#270 @ 249,538: 24x29
#271 @ 423,966: 20x13
#272 @ 921,676: 20x12
#273 @ 238,145: 14x12
#274 @ 278,650: 24x24
#275 @ 629,561: 23x15
#276 @ 98,784: 11x12
#277 @ 281,169: 18x29
#278 @ 929,427: 29x19
#279 @ 164,384: 20x12
#280 @ 145,46: 28x26
#281 @ 717,115: 20x11
#282 @ 929,798: 25x11
#283 @ 275,457: 21x12
#284 @ 898,437: 16x17
#285 @ 466,643: 20x16
#286 @ 744,930: 22x11
#287 @ 857,719: 26x20
#288 @ 860,527: 17x21
#289 @ 212,530: 18x27
#290 @ 328,630: 25x10
#291 @ 476,7: 23x29
#292 @ 787,796: 22x12
#293 @ 18,243: 26x10
#294 @ 389,25: 21x15
#295 @ 687,942: 25x10
#296 @ 380,626: 13x11
#297 @ 357,559: 15x29
#298 @ 1,849: 25x14
#299 @ 457,819: 13x21
#300 @ 719,52: 20x25
#301 @ 895,473: 10x22
#302 @ 301,196: 11x15
#303 @ 432,392: 25x22
#304 @ 591,11: 25x25
#305 @ 101,628: 29x14
#306 @ 322,860: 10x10
#307 @ 300,754: 5x5
#308 @ 437,297: 29x21
#309 @ 451,518: 24x16
#310 @ 649,518: 22x15
#311 @ 558,368: 27x20
#312 @ 432,928: 17x25
#313 @ 784,483: 22x23
#314 @ 316,351: 23x21
#315 @ 10,374: 20x20
#316 @ 321,278: 22x10
#317 @ 524,808: 21x17
#318 @ 389,977: 15x10
#319 @ 102,804: 20x19
#320 @ 17,868: 19x15
#321 @ 303,198: 16x11
#322 @ 872,72: 20x10
#323 @ 331,126: 21x27
#324 @ 137,462: 19x23
#325 @ 170,318: 21x29
#326 @ 268,836: 19x10
#327 @ 390,961: 13x23
#328 @ 161,296: 10x29
#329 @ 204,722: 18x20
#330 @ 249,689: 11x11
#331 @ 912,153: 20x29
#332 @ 66,730: 10x15
#333 @ 87,63: 29x14
#334 @ 745,390: 19x20
#335 @ 105,304: 14x12
#336 @ 833,313: 29x12
#337 @ 451,852: 27x17
#338 @ 0,640: 25x14
#339 @ 204,256: 21x13
#340 @ 663,493: 15x18
#341 @ 35,222: 22x26
#342 @ 326,17: 21x14
#343 @ 670,801: 18x11
#344 @ 902,248: 12x21
#345 @ 730,584: 19x13
#346 @ 387,214: 20x25
#347 @ 298,933: 25x12
#348 @ 242,815: 19x21
#349 @ 62,556: 27x28
#350 @ 652,594: 20x10
#351 @ 250,564: 25x28
#352 @ 206,348: 24x14
#353 @ 232,167: 21x11
#354 @ 478,282: 26x13
#355 @ 268,556: 18x13
#356 @ 656,673: 11x21
#357 @ 631,753: 23x29
#358 @ 311,276: 12x27
#359 @ 899,131: 23x11
#360 @ 940,134: 26x28
#361 @ 345,407: 20x16
#362 @ 816,301: 19x12
#363 @ 844,773: 17x23
#364 @ 850,494: 15x28
#365 @ 967,366: 17x19
#366 @ 549,894: 11x10
#367 @ 318,398: 28x21
#368 @ 9,394: 24x15
#369 @ 725,304: 11x27
#370 @ 829,266: 13x12
#371 @ 880,136: 25x21
#372 @ 166,871: 19x10
#373 @ 210,229: 14x18
#374 @ 351,364: 17x13
#375 @ 182,37: 23x21
#376 @ 675,798: 12x14
#377 @ 809,180: 16x19
#378 @ 488,465: 15x10
#379 @ 452,314: 29x24
#380 @ 501,528: 20x23
#381 @ 299,752: 13x15
#382 @ 783,579: 22x22
#383 @ 579,641: 12x23
#384 @ 904,948: 17x16
#385 @ 812,580: 10x27
#386 @ 117,929: 11x14
#387 @ 129,127: 28x20
#388 @ 714,740: 25x22
#389 @ 732,307: 26x11
#390 @ 885,415: 15x18
#391 @ 45,406: 28x13
#392 @ 356,360: 29x26
#393 @ 630,285: 20x28
#394 @ 854,831: 14x19
#395 @ 451,819: 26x24
#396 @ 424,435: 22x24
#397 @ 243,682: 20x13
#398 @ 284,466: 22x16
#399 @ 605,25: 25x11
#400 @ 959,643: 24x12
#401 @ 140,504: 23x17
#402 @ 6,234: 16x25
#403 @ 872,805: 14x13
#404 @ 466,632: 14x19
#405 @ 944,484: 17x16
#406 @ 619,507: 10x27
#407 @ 8,551: 28x26
#408 @ 435,931: 8x10
#409 @ 901,123: 21x25
#410 @ 55,375: 10x19
#411 @ 424,921: 10x11
#412 @ 822,618: 28x17
#413 @ 823,948: 15x25
#414 @ 580,893: 6x18
#415 @ 597,892: 14x26
#416 @ 615,582: 27x24
#417 @ 52,916: 20x11
#418 @ 679,329: 22x14
#419 @ 32,136: 20x12
#420 @ 921,367: 27x21
#421 @ 292,100: 23x11
#422 @ 508,353: 13x13
#423 @ 376,31: 24x11
#424 @ 718,390: 26x24
#425 @ 429,526: 26x26
#426 @ 406,540: 17x19
#427 @ 144,36: 22x25
#428 @ 218,974: 18x24
#429 @ 742,592: 12x22
#430 @ 934,39: 15x10
#431 @ 638,445: 21x14
#432 @ 944,193: 24x23
#433 @ 825,961: 17x22
#434 @ 235,427: 23x14
#435 @ 661,461: 29x26
#436 @ 715,33: 29x11
#437 @ 728,939: 21x10
#438 @ 312,498: 27x28
#439 @ 224,517: 24x21
#440 @ 670,307: 22x16
#441 @ 194,703: 15x14
#442 @ 117,957: 17x20
#443 @ 884,102: 20x12
#444 @ 438,183: 18x17
#445 @ 178,907: 28x23
#446 @ 235,694: 14x28
#447 @ 61,245: 25x12
#448 @ 289,54: 15x23
#449 @ 373,310: 17x13
#450 @ 425,313: 28x15
#451 @ 298,750: 11x14
#452 @ 916,779: 27x28
#453 @ 373,824: 17x24
#454 @ 503,926: 16x16
#455 @ 549,166: 18x28
#456 @ 723,366: 14x20
#457 @ 904,798: 18x10
#458 @ 177,165: 13x24
#459 @ 353,128: 12x29
#460 @ 289,714: 14x21
#461 @ 471,276: 17x23
#462 @ 812,660: 14x26
#463 @ 239,890: 10x21
#464 @ 89,374: 24x12
#465 @ 128,566: 11x19
#466 @ 454,272: 12x11
#467 @ 736,285: 29x28
#468 @ 27,621: 20x21
#469 @ 194,257: 26x17
#470 @ 305,347: 25x16
#471 @ 602,684: 21x15
#472 @ 182,38: 28x29
#473 @ 540,792: 22x28
#474 @ 313,867: 23x10
#475 @ 163,692: 16x23
#476 @ 348,949: 25x10
#477 @ 890,473: 18x21
#478 @ 35,904: 24x15
#479 @ 861,310: 19x11
#480 @ 24,242: 17x29
#481 @ 314,433: 28x14
#482 @ 498,914: 10x29
#483 @ 556,58: 15x22
#484 @ 960,92: 11x29
#485 @ 375,7: 27x16
#486 @ 871,553: 20x28
#487 @ 289,167: 11x24
#488 @ 312,699: 10x29
#489 @ 584,487: 16x23
#490 @ 299,574: 21x19
#491 @ 354,616: 17x25
#492 @ 675,516: 11x5
#493 @ 847,671: 11x18
#494 @ 960,161: 28x29
#495 @ 910,246: 19x14
#496 @ 448,818: 13x20
#497 @ 288,167: 16x25
#498 @ 845,436: 18x18
#499 @ 197,351: 13x18
#500 @ 882,410: 13x16
#501 @ 372,301: 25x28
#502 @ 423,927: 21x10
#503 @ 423,447: 17x24
#504 @ 797,895: 20x20
#505 @ 769,136: 22x10
#506 @ 811,269: 20x26
#507 @ 837,983: 19x12
#508 @ 571,121: 12x23
#509 @ 904,472: 13x11
#510 @ 610,565: 20x10
#511 @ 335,464: 23x14
#512 @ 550,206: 22x16
#513 @ 452,845: 23x20
#514 @ 410,945: 18x16
#515 @ 943,804: 19x28
#516 @ 14,472: 26x21
#517 @ 12,983: 16x13
#518 @ 110,757: 28x19
#519 @ 373,292: 24x22
#520 @ 886,833: 26x25
#521 @ 980,663: 13x19
#522 @ 847,842: 29x14
#523 @ 803,520: 11x26
#524 @ 510,276: 15x15
#525 @ 542,50: 28x26
#526 @ 830,313: 10x28
#527 @ 941,514: 13x20
#528 @ 269,385: 11x20
#529 @ 841,752: 28x26
#530 @ 650,602: 23x21
#531 @ 536,201: 24x13
#532 @ 591,62: 18x20
#533 @ 975,955: 20x23
#534 @ 675,8: 18x17
#535 @ 165,431: 27x16
#536 @ 621,191: 18x17
#537 @ 876,259: 24x23
#538 @ 194,571: 24x15
#539 @ 821,913: 24x29
#540 @ 538,203: 11x8
#541 @ 479,960: 21x17
#542 @ 488,598: 15x13
#543 @ 234,408: 21x15
#544 @ 114,229: 24x12
#545 @ 903,17: 13x12
#546 @ 360,877: 11x16
#547 @ 327,146: 11x27
#548 @ 904,439: 11x25
#549 @ 38,180: 16x27
#550 @ 495,591: 26x12
#551 @ 376,26: 29x14
#552 @ 111,325: 12x16
#553 @ 303,638: 27x17
#554 @ 755,890: 17x11
#555 @ 883,909: 11x16
#556 @ 897,264: 10x17
#557 @ 766,888: 22x15
#558 @ 217,394: 19x28
#559 @ 55,747: 11x25
#560 @ 753,381: 19x24
#561 @ 584,647: 23x19
#562 @ 922,745: 21x29
#563 @ 902,319: 24x11
#564 @ 369,320: 13x19
#565 @ 373,371: 12x16
#566 @ 547,442: 16x28
#567 @ 579,496: 27x23
#568 @ 494,917: 17x17
#569 @ 323,377: 20x16
#570 @ 887,666: 24x25
#571 @ 394,268: 23x26
#572 @ 255,113: 17x28
#573 @ 838,788: 19x14
#574 @ 933,145: 14x16
#575 @ 159,468: 26x19
#576 @ 434,179: 12x19
#577 @ 44,472: 27x17
#578 @ 774,563: 24x27
#579 @ 35,693: 28x14
#580 @ 411,667: 21x10
#581 @ 524,732: 23x12
#582 @ 451,173: 25x12
#583 @ 946,642: 17x20
#584 @ 8,345: 25x29
#585 @ 901,143: 29x12
#586 @ 202,840: 14x10
#587 @ 631,970: 21x17
#588 @ 885,685: 14x12
#589 @ 410,522: 24x27
#590 @ 58,517: 25x28
#591 @ 85,1: 22x20
#592 @ 465,913: 29x22
#593 @ 807,498: 11x29
#594 @ 194,208: 14x18
#595 @ 666,835: 16x22
#596 @ 971,649: 13x18
#597 @ 428,231: 22x22
#598 @ 575,667: 18x27
#599 @ 192,265: 18x15
#600 @ 297,387: 22x24
#601 @ 500,185: 14x17
#602 @ 440,937: 20x25
#603 @ 636,565: 10x4
#604 @ 356,290: 20x11
#605 @ 246,887: 19x12
#606 @ 835,307: 18x21
#607 @ 624,431: 17x26
#608 @ 325,620: 25x14
#609 @ 266,631: 27x10
#610 @ 195,601: 13x24
#611 @ 762,406: 6x17
#612 @ 431,949: 18x14
#613 @ 267,555: 24x19
#614 @ 856,787: 28x13
#615 @ 175,191: 20x12
#616 @ 598,7: 21x26
#617 @ 183,435: 12x17
#618 @ 419,542: 17x20
#619 @ 343,124: 15x15
#620 @ 345,402: 17x26
#621 @ 70,64: 12x13
#622 @ 911,723: 3x4
#623 @ 593,56: 13x12
#624 @ 474,928: 18x26
#625 @ 195,612: 14x27
#626 @ 200,249: 22x17
#627 @ 515,717: 13x29
#628 @ 324,342: 12x18
#629 @ 252,509: 24x19
#630 @ 796,789: 11x12
#631 @ 270,579: 15x14
#632 @ 913,817: 16x17
#633 @ 235,326: 27x21
#634 @ 199,656: 17x20
#635 @ 11,538: 16x18
#636 @ 40,630: 15x21
#637 @ 918,819: 6x12
#638 @ 319,952: 18x13
#639 @ 552,558: 24x29
#640 @ 129,817: 28x22
#641 @ 443,428: 11x13
#642 @ 86,281: 14x10
#643 @ 944,86: 14x25
#644 @ 309,583: 21x25
#645 @ 423,433: 27x12
#646 @ 10,196: 10x17
#647 @ 385,878: 10x24
#648 @ 578,890: 14x26
#649 @ 817,478: 13x11
#650 @ 936,254: 23x14
#651 @ 964,466: 24x17
#652 @ 191,477: 26x12
#653 @ 92,730: 23x20
#654 @ 318,840: 22x17
#655 @ 975,277: 25x18
#656 @ 680,62: 14x28
#657 @ 752,146: 27x27
#658 @ 529,411: 20x19
#659 @ 205,785: 12x14
#660 @ 551,562: 28x15
#661 @ 302,190: 29x13
#662 @ 237,421: 27x11
#663 @ 117,845: 22x11
#664 @ 911,851: 12x22
#665 @ 571,142: 15x12
#666 @ 708,389: 22x18
#667 @ 711,310: 20x23
#668 @ 795,289: 13x27
#669 @ 236,712: 16x27
#670 @ 566,343: 10x15
#671 @ 469,818: 27x27
#672 @ 84,914: 21x16
#673 @ 47,621: 10x19
#674 @ 891,103: 10x29
#675 @ 638,296: 15x18
#676 @ 354,415: 29x27
#677 @ 269,519: 14x15
#678 @ 735,337: 24x19
#679 @ 365,980: 17x16
#680 @ 545,35: 20x11
#681 @ 968,640: 22x23
#682 @ 202,660: 7x12
#683 @ 502,189: 22x20
#684 @ 196,797: 20x16
#685 @ 741,103: 27x12
#686 @ 353,671: 11x23
#687 @ 962,626: 27x26
#688 @ 406,831: 20x28
#689 @ 927,860: 26x15
#690 @ 550,880: 26x11
#691 @ 104,503: 18x27
#692 @ 393,882: 16x29
#693 @ 565,607: 10x20
#694 @ 859,823: 19x26
#695 @ 298,126: 10x21
#696 @ 897,331: 20x26
#697 @ 969,955: 21x21
#698 @ 855,730: 16x11
#699 @ 366,598: 18x10
#700 @ 190,794: 23x10
#701 @ 81,903: 17x19
#702 @ 13,383: 10x24
#703 @ 674,941: 20x18
#704 @ 621,966: 23x19
#705 @ 609,463: 26x11
#706 @ 787,441: 26x27
#707 @ 238,397: 29x15
#708 @ 790,815: 10x26
#709 @ 615,906: 22x10
#710 @ 77,647: 11x28
#711 @ 370,548: 29x15
#712 @ 669,514: 21x10
#713 @ 360,957: 28x18
#714 @ 615,493: 16x29
#715 @ 880,901: 26x17
#716 @ 161,446: 12x25
#717 @ 88,2: 18x11
#718 @ 221,237: 15x29
#719 @ 258,222: 25x16
#720 @ 131,263: 22x10
#721 @ 382,591: 21x24
#722 @ 651,145: 20x12
#723 @ 470,494: 12x25
#724 @ 843,164: 17x25
#725 @ 278,982: 23x13
#726 @ 237,711: 19x20
#727 @ 358,621: 28x22
#728 @ 548,500: 19x16
#729 @ 6,129: 29x17
#730 @ 312,300: 26x21
#731 @ 838,252: 19x27
#732 @ 470,155: 16x28
#733 @ 832,942: 14x12
#734 @ 673,283: 26x29
#735 @ 296,162: 17x22
#736 @ 568,640: 26x23
#737 @ 833,453: 13x15
#738 @ 724,399: 13x24
#739 @ 942,102: 12x18
#740 @ 233,137: 19x20
#741 @ 581,459: 17x19
#742 @ 64,398: 21x11
#743 @ 978,635: 13x21
#744 @ 352,90: 20x21
#745 @ 77,534: 24x28
#746 @ 704,310: 27x20
#747 @ 729,298: 15x25
#748 @ 93,275: 27x12
#749 @ 748,69: 11x15
#750 @ 362,36: 16x29
#751 @ 30,955: 13x19
#752 @ 574,294: 22x23
#753 @ 202,305: 11x13
#754 @ 318,504: 13x12
#755 @ 760,556: 21x27
#756 @ 930,474: 28x11
#757 @ 445,743: 19x18
#758 @ 406,674: 27x27
#759 @ 380,594: 22x20
#760 @ 273,162: 29x24
#761 @ 305,845: 26x12
#762 @ 177,233: 23x10
#763 @ 458,197: 26x18
#764 @ 25,434: 21x28
#765 @ 322,792: 17x22
#766 @ 209,734: 10x25
#767 @ 623,904: 18x14
#768 @ 795,9: 14x27
#769 @ 316,625: 21x21
#770 @ 733,72: 29x25
#771 @ 113,809: 19x15
#772 @ 548,504: 18x18
#773 @ 884,460: 12x18
#774 @ 583,275: 20x25
#775 @ 714,134: 13x13
#776 @ 375,135: 11x18
#777 @ 33,275: 16x17
#778 @ 468,204: 16x13
#779 @ 244,554: 21x15
#780 @ 850,446: 12x16
#781 @ 908,346: 21x25
#782 @ 158,324: 16x14
#783 @ 689,478: 17x12
#784 @ 484,724: 14x16
#785 @ 604,599: 24x13
#786 @ 657,717: 19x11
#787 @ 475,724: 13x10
#788 @ 169,75: 29x25
#789 @ 439,597: 13x13
#790 @ 826,466: 22x24
#791 @ 306,939: 11x22
#792 @ 858,502: 16x28
#793 @ 114,609: 26x29
#794 @ 667,800: 29x21
#795 @ 842,33: 19x18
#796 @ 20,859: 10x17
#797 @ 304,957: 22x23
#798 @ 755,358: 28x23
#799 @ 20,951: 16x24
#800 @ 100,10: 15x28
#801 @ 779,139: 20x12
#802 @ 786,25: 18x24
#803 @ 40,581: 20x10
#804 @ 804,599: 23x15
#805 @ 676,980: 11x11
#806 @ 736,434: 22x21
#807 @ 435,714: 14x25
#808 @ 124,30: 22x26
#809 @ 620,428: 11x21
#810 @ 364,216: 26x23
#811 @ 457,12: 28x22
#812 @ 46,121: 18x29
#813 @ 530,810: 21x14
#814 @ 404,800: 10x27
#815 @ 84,323: 19x25
#816 @ 693,129: 21x11
#817 @ 532,21: 11x20
#818 @ 256,133: 20x28
#819 @ 476,10: 23x16
#820 @ 953,255: 27x13
#821 @ 766,505: 14x10
#822 @ 127,541: 16x20
#823 @ 900,854: 16x23
#824 @ 80,918: 15x26
#825 @ 169,347: 25x26
#826 @ 941,810: 12x20
#827 @ 543,776: 27x21
#828 @ 82,845: 28x28
#829 @ 824,939: 24x20
#830 @ 168,272: 16x17
#831 @ 554,821: 16x17
#832 @ 304,78: 17x20
#833 @ 575,460: 13x21
#834 @ 682,539: 11x24
#835 @ 583,73: 16x14
#836 @ 271,780: 22x27
#837 @ 628,518: 10x20
#838 @ 166,262: 26x17
#839 @ 801,784: 24x16
#840 @ 716,370: 25x25
#841 @ 880,866: 13x22
#842 @ 871,9: 24x24
#843 @ 817,474: 26x13
#844 @ 254,220: 10x16
#845 @ 939,200: 11x22
#846 @ 141,224: 14x14
#847 @ 588,507: 24x23
#848 @ 649,313: 24x28
#849 @ 85,474: 11x28
#850 @ 258,612: 15x21
#851 @ 69,463: 26x21
#852 @ 697,62: 28x23
#853 @ 718,214: 27x24
#854 @ 665,837: 17x22
#855 @ 494,583: 25x19
#856 @ 317,194: 22x27
#857 @ 650,701: 18x17
#858 @ 472,960: 20x26
#859 @ 560,652: 27x14
#860 @ 348,366: 11x16
#861 @ 909,719: 11x15
#862 @ 586,701: 19x20
#863 @ 549,237: 18x15
#864 @ 618,149: 27x17
#865 @ 349,263: 12x12
#866 @ 352,74: 16x18
#867 @ 91,219: 26x19
#868 @ 463,256: 19x23
#869 @ 697,436: 25x29
#870 @ 299,727: 10x11
#871 @ 628,286: 29x28
#872 @ 93,370: 24x20
#873 @ 116,753: 16x15
#874 @ 67,261: 15x10
#875 @ 755,166: 19x12
#876 @ 114,449: 27x14
#877 @ 296,178: 27x26
#878 @ 257,126: 12x9
#879 @ 597,77: 14x18
#880 @ 579,652: 17x27
#881 @ 355,533: 27x29
#882 @ 445,56: 25x22
#883 @ 431,350: 25x25
#884 @ 244,147: 20x23
#885 @ 161,348: 22x26
#886 @ 342,526: 5x3
#887 @ 949,964: 24x19
#888 @ 803,238: 18x18
#889 @ 647,422: 17x28
#890 @ 651,16: 14x17
#891 @ 495,351: 17x15
#892 @ 160,851: 27x23
#893 @ 108,224: 25x28
#894 @ 312,85: 27x24
#895 @ 128,833: 12x18
#896 @ 659,308: 25x15
#897 @ 586,321: 10x28
#898 @ 242,124: 25x19
#899 @ 297,134: 19x17
#900 @ 487,119: 25x26
#901 @ 838,535: 29x21
#902 @ 289,66: 10x28
#903 @ 903,278: 26x13
#904 @ 59,247: 22x19
#905 @ 175,690: 11x12
#906 @ 521,116: 29x27
#907 @ 379,92: 17x10
#908 @ 92,520: 16x26
#909 @ 513,30: 18x12
#910 @ 922,760: 14x15
#911 @ 181,832: 22x20
#912 @ 944,943: 25x25
#913 @ 317,807: 12x22
#914 @ 942,483: 17x10
#915 @ 711,359: 22x29
#916 @ 516,543: 13x29
#917 @ 546,609: 24x23
#918 @ 409,574: 24x12
#919 @ 685,940: 21x21
#920 @ 648,656: 10x29
#921 @ 794,729: 27x23
#922 @ 737,578: 26x18
#923 @ 716,309: 21x24
#924 @ 160,844: 17x21
#925 @ 176,968: 12x16
#926 @ 552,876: 12x25
#927 @ 9,802: 18x26
#928 @ 527,746: 21x16
#929 @ 61,456: 17x17
#930 @ 939,14: 12x29
#931 @ 363,401: 19x19
#932 @ 530,426: 23x21
#933 @ 33,411: 29x21
#934 @ 542,68: 29x16
#935 @ 734,577: 12x15
#936 @ 299,64: 24x19
#937 @ 899,356: 17x10
#938 @ 181,342: 21x17
#939 @ 370,594: 20x16
#940 @ 52,721: 16x23
#941 @ 321,385: 26x15
#942 @ 848,159: 12x27
#943 @ 814,291: 23x24
#944 @ 18,803: 25x25
#945 @ 834,458: 14x17
#946 @ 440,543: 22x18
#947 @ 417,377: 20x28
#948 @ 181,263: 19x20
#949 @ 307,69: 17x29
#950 @ 890,412: 13x29
#951 @ 947,856: 17x19
#952 @ 367,841: 16x17
#953 @ 221,945: 24x14
#954 @ 217,449: 26x19
#955 @ 27,695: 15x26
#956 @ 366,866: 16x17
#957 @ 506,273: 12x20
#958 @ 874,65: 27x13
#959 @ 402,442: 24x20
#960 @ 344,381: 18x15
#961 @ 345,427: 11x22
#962 @ 10,975: 19x22
#963 @ 354,464: 16x27
#964 @ 6,335: 10x16
#965 @ 60,730: 21x17
#966 @ 376,90: 26x17
#967 @ 528,109: 18x26
#968 @ 482,924: 29x12
#969 @ 494,376: 20x22
#970 @ 464,823: 13x26
#971 @ 83,628: 28x27
#972 @ 854,577: 13x19
#973 @ 261,614: 13x21
#974 @ 952,93: 15x15
#975 @ 250,308: 10x19
#976 @ 19,209: 22x14
#977 @ 274,184: 14x16
#978 @ 330,856: 26x24
#979 @ 257,930: 19x14
#980 @ 844,508: 26x12
#981 @ 250,806: 15x20
#982 @ 752,483: 22x26
#983 @ 334,385: 25x13
#984 @ 650,464: 19x20
#985 @ 927,815: 17x27
#986 @ 913,735: 21x11
#987 @ 269,549: 25x12
#988 @ 116,544: 18x26
#989 @ 84,953: 26x21
#990 @ 752,182: 29x19
#991 @ 796,769: 21x18
#992 @ 800,799: 11x20
#993 @ 79,711: 21x23
#994 @ 683,293: 28x19
#995 @ 526,427: 16x28
#996 @ 671,242: 16x14
#997 @ 293,393: 11x25
#998 @ 165,697: 9x6
#999 @ 854,966: 29x11
#1000 @ 63,738: 26x14
#1001 @ 213,956: 20x29
#1002 @ 580,649: 25x10
#1003 @ 536,335: 15x11
#1004 @ 544,187: 27x18
#1005 @ 850,608: 15x22
#1006 @ 384,931: 19x19
#1007 @ 29,649: 26x19
#1008 @ 366,624: 26x10
#1009 @ 671,825: 23x16
#1010 @ 873,250: 28x16
#1011 @ 780,822: 20x28
#1012 @ 944,396: 12x28
#1013 @ 937,20: 13x23
#1014 @ 685,73: 3x7
#1015 @ 662,287: 25x12
#1016 @ 946,406: 14x28
#1017 @ 186,895: 19x13
#1018 @ 84,36: 19x12
#1019 @ 650,150: 26x12
#1020 @ 98,212: 13x19
#1021 @ 413,441: 14x29
#1022 @ 256,977: 15x10
#1023 @ 975,651: 5x11
#1024 @ 338,52: 29x16
#1025 @ 876,271: 21x15
#1026 @ 88,71: 16x14
#1027 @ 434,603: 10x27
#1028 @ 974,470: 21x25
#1029 @ 84,768: 25x21
#1030 @ 886,324: 21x12
#1031 @ 248,710: 28x20
#1032 @ 437,209: 10x27
#1033 @ 272,835: 18x17
#1034 @ 47,589: 21x17
#1035 @ 71,459: 26x22
#1036 @ 229,360: 23x29
#1037 @ 523,395: 26x18
#1038 @ 451,956: 27x19
#1039 @ 360,93: 13x10
#1040 @ 420,947: 22x24
#1041 @ 439,478: 27x21
#1042 @ 510,544: 13x20
#1043 @ 304,520: 15x26
#1044 @ 181,254: 27x11
#1045 @ 87,313: 26x19
#1046 @ 712,386: 11x18
#1047 @ 142,144: 14x22
#1048 @ 654,467: 20x10
#1049 @ 50,73: 23x27
#1050 @ 510,759: 21x29
#1051 @ 776,581: 11x15
#1052 @ 951,378: 24x22
#1053 @ 18,436: 14x26
#1054 @ 518,59: 26x14
#1055 @ 955,88: 16x17
#1056 @ 35,628: 27x22
#1057 @ 491,965: 29x29
#1058 @ 169,983: 19x12
#1059 @ 23,475: 24x15
#1060 @ 886,112: 28x14
#1061 @ 402,315: 25x20
#1062 @ 213,203: 22x17
#1063 @ 129,521: 16x17
#1064 @ 336,523: 18x17
#1065 @ 102,775: 28x12
#1066 @ 282,660: 15x26
#1067 @ 902,345: 10x17
#1068 @ 233,969: 29x20
#1069 @ 666,317: 3x13
#1070 @ 341,205: 16x24
#1071 @ 337,964: 27x12
#1072 @ 607,675: 14x20
#1073 @ 690,445: 12x29
#1074 @ 926,532: 26x20
#1075 @ 937,466: 29x11
#1076 @ 570,714: 25x14
#1077 @ 678,520: 19x27
#1078 @ 307,351: 27x10
#1079 @ 526,34: 29x29
#1080 @ 74,684: 18x16
#1081 @ 450,752: 23x15
#1082 @ 755,795: 22x27
#1083 @ 260,138: 21x29
#1084 @ 321,315: 19x29
#1085 @ 188,214: 17x22
#1086 @ 784,712: 21x18
#1087 @ 458,550: 14x28
#1088 @ 796,582: 27x13
#1089 @ 321,230: 21x29
#1090 @ 898,470: 22x20
#1091 @ 138,370: 11x12
#1092 @ 345,361: 10x10
#1093 @ 177,882: 19x16
#1094 @ 946,702: 26x26
#1095 @ 619,490: 24x19
#1096 @ 133,506: 20x20
#1097 @ 266,869: 25x21
#1098 @ 387,970: 19x21
#1099 @ 311,323: 17x24
#1100 @ 310,488: 28x22
#1101 @ 770,651: 13x16
#1102 @ 965,301: 28x11
#1103 @ 466,826: 19x15
#1104 @ 88,632: 17x10
#1105 @ 902,137: 25x19
#1106 @ 752,329: 18x26
#1107 @ 182,164: 23x17
#1108 @ 289,679: 14x28
#1109 @ 176,502: 18x18
#1110 @ 214,971: 12x27
#1111 @ 389,207: 28x28
#1112 @ 331,19: 4x8
#1113 @ 312,635: 25x29
#1114 @ 509,141: 14x21
#1115 @ 392,798: 13x24
#1116 @ 876,419: 27x12
#1117 @ 636,613: 28x14
#1118 @ 681,326: 11x25
#1119 @ 787,707: 20x27
#1120 @ 31,11: 25x21
#1121 @ 270,551: 20x21
#1122 @ 353,134: 17x27
#1123 @ 752,773: 17x25
#1124 @ 648,692: 12x28
#1125 @ 495,632: 27x27
#1126 @ 860,171: 14x20
#1127 @ 253,507: 20x22
#1128 @ 316,494: 16x10
#1129 @ 524,569: 29x29
#1130 @ 238,309: 20x13
#1131 @ 783,542: 15x29
#1132 @ 553,681: 23x11
#1133 @ 884,495: 10x25
#1134 @ 910,18: 17x12
#1135 @ 436,127: 14x10
#1136 @ 61,738: 12x24
#1137 @ 966,288: 12x27
#1138 @ 722,117: 7x3
#1139 @ 95,933: 28x29
#1140 @ 336,683: 25x24
#1141 @ 681,946: 25x17
#1142 @ 359,61: 22x20
#1143 @ 37,637: 22x18
#1144 @ 768,578: 20x13
#1145 @ 855,666: 15x26
#1146 @ 255,689: 10x27
#1147 @ 599,478: 20x24
#1148 @ 195,715: 18x23
#1149 @ 478,641: 21x14
#1150 @ 882,180: 27x20
#1151 @ 851,302: 28x21
#1152 @ 363,300: 27x26
#1153 @ 309,631: 4x3
#1154 @ 199,224: 12x17
#1155 @ 228,153: 19x13
#1156 @ 487,22: 14x27
#1157 @ 682,302: 17x15
#1158 @ 187,487: 16x21
#1159 @ 210,315: 19x26
#1160 @ 376,789: 18x29
#1161 @ 67,567: 13x17
#1162 @ 221,515: 14x29
#1163 @ 397,514: 12x26
#1164 @ 384,371: 18x23
#1165 @ 882,953: 27x29
#1166 @ 287,88: 28x12
#1167 @ 884,89: 21x21
#1168 @ 99,820: 17x13
#1169 @ 492,656: 21x14
#1170 @ 147,831: 29x21
#1171 @ 128,256: 10x13
#1172 @ 841,476: 24x16
#1173 @ 328,17: 11x14
#1174 @ 109,287: 20x12
#1175 @ 113,311: 12x27
#1176 @ 856,917: 18x13
#1177 @ 466,556: 24x10
#1178 @ 486,585: 19x16
#1179 @ 711,226: 10x13
#1180 @ 108,254: 26x24
#1181 @ 725,313: 10x24
#1182 @ 365,127: 23x25
#1183 @ 488,371: 22x14
#1184 @ 381,502: 16x21
#1185 @ 322,567: 17x24
#1186 @ 210,564: 12x29
#1187 @ 525,797: 21x24
#1188 @ 58,431: 29x25
#1189 @ 661,24: 20x15
#1190 @ 797,234: 17x18
#1191 @ 851,38: 13x21
#1192 @ 962,75: 11x27
#1193 @ 568,200: 16x23
#1194 @ 863,319: 12x18
#1195 @ 25,704: 27x24
#1196 @ 835,510: 29x14
#1197 @ 427,904: 23x25
#1198 @ 327,956: 18x27
#1199 @ 168,609: 16x23
#1200 @ 591,31: 16x26
#1201 @ 428,374: 13x16
#1202 @ 183,332: 6x7
#1203 @ 139,266: 12x12
#1204 @ 616,33: 19x28
#1205 @ 479,470: 18x10
#1206 @ 483,910: 19x25
#1207 @ 38,760: 28x21
#1208 @ 307,727: 10x27
#1209 @ 607,19: 28x29
#1210 @ 760,404: 12x25
#1211 @ 541,23: 10x18
#1212 @ 457,555: 14x23
#1213 @ 307,693: 12x12
#1214 @ 176,965: 11x15
#1215 @ 880,555: 3x12
#1216 @ 365,261: 21x25
#1217 @ 900,338: 24x18
#1218 @ 796,796: 15x12
#1219 @ 94,64: 12x11
#1220 @ 398,1: 28x10
#1221 @ 511,944: 11x29
#1222 @ 432,174: 17x29
#1223 @ 619,427: 19x16
#1224 @ 978,670: 19x12
#1225 @ 330,384: 26x20
#1226 @ 233,701: 16x14
#1227 @ 264,870: 21x12
#1228 @ 457,889: 23x29
#1229 @ 614,202: 25x29
#1230 @ 744,689: 26x27
#1231 @ 484,912: 16x11
#1232 @ 912,679: 21x26
#1233 @ 509,20: 24x14
#1234 @ 679,847: 21x29
#1235 @ 897,950: 14x17
#1236 @ 449,85: 25x28
#1237 @ 907,821: 25x17
#1238 @ 685,967: 19x20
#1239 @ 104,16: 22x28
#1240 @ 363,95: 5x5
#1241 @ 629,755: 23x18
#1242 @ 570,345: 15x28
#1243 @ 270,193: 23x11
#1244 @ 43,348: 12x21
#1245 @ 903,482: 22x29
#1246 @ 915,179: 27x24
#1247 @ 76,26: 16x14
#1248 @ 874,197: 16x23
#1249 @ 869,728: 26x14
#1250 @ 158,377: 10x11
#1251 @ 379,138: 26x17
#1252 @ 298,977: 21x12
#1253 @ 914,737: 27x26
#1254 @ 153,123: 21x27
#1255 @ 842,731: 20x24
#1256 @ 885,852: 24x26
#1257 @ 707,747: 23x18
#1258 @ 729,387: 19x23
#1259 @ 238,452: 24x20
'''.strip().splitlines()

# print(dat)
claims = {}
for line in dat:
    claimset = set()
    n, rest = line.split('@')
    coords, dims = rest.split(':')
    x, y = tuple(map(int, coords.split(',')))
    xlen, ylen = tuple(map(int, dims.split('x')))
    # print((x, y), (xlen, ylen))

    for nx in range(x, x+xlen):
        for ny in range(y, y+ylen):
            claims[(nx, ny)] = claims.get((nx, ny), 0) + 1

n = len([x for x in claims.values() if x >= 2])
print(n)


for line in dat:
    claimset = set()
    n, rest = line.split('@')
    coords, dims = rest.split(':')
    x, y = tuple(map(int, coords.split(',')))
    xlen, ylen = tuple(map(int, dims.split('x')))

    is_valid = True
    for nx in range(x, x+xlen):
        for ny in range(y, y+ylen):
            if claims[(nx, ny)] > 1:
                is_valid = False
        if not is_valid:
            break

    if is_valid:
        print(f'{n} is valid.')
