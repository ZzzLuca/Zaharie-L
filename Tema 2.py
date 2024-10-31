txt = ["Judecătorii din Iași au eliminat toate înregistrările DNA din dosarul lui Dumitru Buzatu, acuzat de luare de mită. Ce urmează"]
txt1 = txt[len(txt)//2:] 
txt1.upper()
txt1.replace(" "," ")
txt2 = txt[len(txt)//2]
txt2.replace(".",",","!","?")
txt2.reverse()
txt2.capitalize()
print(txt1 + txt2)
