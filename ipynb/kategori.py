def kategori(Crm):
    if(Crm == 648):
        return "arson"
    if(Crm == 230 or Crm == 231 or Crm == 235 or Crm == 236 or Crm == 250 or Crm == 251 or Crm == 435 or Crm == 436 or Crm == 622 or Crm == 623 or Crm == 624 or Crm == 625 or Crm == 626 or Crm == 627 or Crm == 647):
        return "assault"
    if(Crm == 942):
        return "bribe"
    if(Crm == 310 or Crm == 320 or Crm == 330 or Crm == 410 or Crm == 973):
        return "burglary"
    if(Crm == 649 or Crm == 651 or Crm == 652 or Crm == 653 or Crm == 654 or Crm == 660):
        return "forgery"
    if(Crm == 900 or Crm == 901 or Crm == 902 or Crm == 903):
        return "curfew"
    if(Crm == 438 or Crm == 755 or Crm == 763 or Crm == 880 or Crm == 882 or Crm == 884 or Crm == 886):
        return "disorderlyconduct"
    if(Crm == 865):
        return "drugs"
    if(Crm ==433 or Crm == 668 or Crm == 670):
        return "embezzlement"
    if(Crm == 928 or Crm == 930 or Crm == 946):
        return"BlackMail"
    if(Crm == 870 or Crm == 237):
        return "Family Offense"
    if(Crm == 662 or Crm == 664 or Crm == 950 or Crm == 951):
        return "fraud"
    if(Crm == 110 or Crm == 113):
        return "homicide"
    if(Crm == 910 or Crm == 920 or Crm == 922):
            return "kidnapping"
    if(Crm ==331 or Crm == 480 or Crm == 485 or Crm == 407 or Crm == 510 or Crm == 520):
        return "motor theft"
    if(Crm == 805 or Crm == 806):
        return "prostitution"
    if(Crm ==210 or Crm == 220):
        return "robbery"
    if(Crm == 121 or Crm == 122 or Crm == 762 or Crm == 810 or Crm == 815 or Crm == 820 or Crm == 821 or Crm == 836 or Crm == 840 or Crm == 845 or Crm == 860 or Crm == 850 or Crm == 932 or Crm == 956):
        return "sex offense"
    if(Crm == 888):
        return "trespassing"
    if(Crm == 740 or Crm == 744 or Crm == 924):
        return "vandalism"
    if(Crm ==753 or Crm == 756 or Crm == 761 or Crm == 931):
        return "weapon law"
    if(Crm == 331 or Crm == 341 or Crm == 343 or Crm == 345 or Crm == 347 or Crm == 349 or Crm == 354 or Crm == 430):
        return "grand theft"
    if(Crm == 350 or Crm == 351 or Crm == 352 or Crm == 353 or Crm == 420 or Crm == 421 or Crm == 431 or Crm >=440 and Crm <=475 ):
        return "theft"
    if(Crm == 997):
        return "traffic"
    if(Crm == 812 or Crm == 813):
        return "Children"
    return "MISC"