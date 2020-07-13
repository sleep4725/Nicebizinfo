import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import time

from mainCode.getSessionObj import GetSessionObj
from mainCode.getSeleniumObj import ArgSet

class Nicebizinfo():

    def __init__(self):

        self.url = "http://www.nicebizinfo.com/ep/EP0100M001GE.nice?"
        self.subUrl = "https://www.nicebizinfo.com/ep/EP0100M002GE.nice?"

    def dataGet(self):

        chromeObj = ArgSet.getSelenium()
        paramEncode = urlencode({
            "itgSrch": "c16",
            "pageno" : 294
        })

        reqUrl = self.url + paramEncode
        chromeObj.get(url=reqUrl)
        chromeObj.implicitly_wait(3)
        print (chromeObj.title)
        bgList = chromeObj.find_elements_by_css_selector("tr.bg")

        for b in bgList:
            aTag = b.find_element_by_css_selector("th.tal.bdl1 > span.fz14.fwb.ml10.fErr > a")
            subParams = str(aTag.get_attribute("onclick")).replace("NICE.dutch.showDtlView", "").strip("('").strip("')")
            encodeParams = urlencode({"kiscode": subParams})
            subUrlRequest = self.subUrl + encodeParams
            self.subUrlRequest(url= subUrlRequest)

        chromeObj.close()
        chromeObj.quit()

    def subUrlRequest(self, url):

        chromeObj = ArgSet.getSelenium()
        chromeObj.get(url=url)
        chromeObj.implicitly_wait(3)

        bsObj = BeautifulSoup(chromeObj.page_source,"html.parser")
        header = bsObj.select_one("div.header > h1")
        print(header.string)

        tbody = bsObj.select_one("div.cTable.sp4 > table > tbody").select("tr")

        result = dict()
        for t in tbody:
            bgData = [ str(i.text).replace(" ", "") for i in t.select("th.bg")]
            bgData.append("TEL_FAX")
            tdData = t.select("td")

            for i in zip(bgData, tdData):

                strData = str(i[1].text).strip()
                if strData[:3] == "TEL":
                    strData = strData.replace("\n", "").replace("\t", "")

                result[i[0]] = strData

        print(result)


        chromeObj.close()
        chromeObj.quit()