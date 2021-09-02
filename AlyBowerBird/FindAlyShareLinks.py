import re
import urllib
from bs4 import BeautifulSoup
import urllib.request

def FindAlyShareLinks(url):
    '''
    return:dict in list,key="code","link"
    '''
    alyShareLinkPattern = re.compile(r"(?P<linkName>www.aliyundrive.com/s/[\S]{11})")
    accessCodePattern = re.compile(r".*提取码: (?P<accessCode>[0-9a-zA-Z]{4})")
    resources = []
    
    if url == "":
        return
    page = urllib.request.urlopen(url).read()
    page = page.decode("utf-8")
    soup = BeautifulSoup(page, "lxml")
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    text = soup.get_text()
    lines = [line.strip() for line in text.splitlines()]
    reDupTmp = []
    for index,eachLine in enumerate(lines):
        ret = re.search(alyShareLinkPattern,eachLine)
        retList = re.findall(alyShareLinkPattern,eachLine)
        if len(retList) != 0:
            for ret in retList:                       
                eachResDic = dict()                
                for codeLineIndex in range(index - 1,index + 1):
                    codeRet = re.findall(accessCodePattern,lines[codeLineIndex])
                    if len(codeRet) != 0:
                        eachResDic["code"] = codeRet[0]
                        break
                    else:
                        eachResDic["code"] = ""
                eachResDic["link"] = ret
                #else:
                #    eachResDic["code"] = ""
                #    eachResDic["link"] = ret.group("linkName")
            
                if eachResDic["link"] not in reDupTmp:
                    reDupTmp.append(eachResDic["link"])
                    resources.append(eachResDic)
    return resources
