i=12
while(i<=26):
    download_btn = "//*[@id='content']/tbody/tr["+str(i)+"]/td[2]/span/a[2]"
    i = i+1
    print(download_btn)
        # else: