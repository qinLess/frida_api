function getSign(str) {
    var res = ''
    Java.perform(function () {
        var context = Java.use('android.app.ActivityThread').currentApplication().getApplicationContext()
        var charset = Java.use('java.nio.charset.Charset').forName("UTF-8")
        var CPU = Java.use('com.yxcorp.gifshow.util.CPU')
        // var str = 'abi=arm32androidApiLevel=27app=0apptype=22appver=3.3.60.874bodyMd5=1208fb608e042412785ecec8397c63e4browseType=3c=ANDROID_JSB_JB_SJYY_CPA_JLOSKJBclient_key=2ac2a76dcold_launch_time_ms=1618583653623country_code=CNdarkMode=falseddpi=560deviceBit=0did=ANDROID_2ff4054a573ac183did_gt=1618560375964did_tag=0egid=DFP74A4E3728821626DD18643E90AB5B8EDB1AC9573737C6D66CE078CF16CE97encoding=zstdftt=hotfix_ver=isp=iuid=kcv=1318keyconfig_state=1kpf=ANDROID_PHONEkpn=NEBULAlanguage=zh-cnlat=30.295827ll=CRdGelG7Sz5AERmsONVaEV5Alon=120.271169max_memory=256mod=Google(Pixel XL)nbh=168net=WIFInewOc=ANDROID_JSB_JB_SJYY_CPA_JLOSKJBoc=ANDROID_JSB_JB_SJYY_CPA_JLOSKJBos=androidpower_mode=0priorityType=1rdid=ANDROID_fe9d1be4e2c63710sbh=84sh=2560socName=Qualcomm MSM8996PRO-ABsw=1440sys=ANDROID_8.1.0totalMemory=3762ud=0ver=UNKNOWN'

        var str1 = Java.use('java.lang.String').$new(str).getBytes(charset)
        res = CPU.getClock(context, str1, 29)
    })
    return res
}


function getNSSign3(str) {
    var res = ''
    Java.perform(function () {
        // var str = '/rest/nebula/search/newaa7e76b779ef758d17823a9b51b1acf6'
        var KSecurity = Java.use('com.kuaishou.android.security.KSecurity')
        res = KSecurity.atlasSign(str)
    })
    return res
}


rpc.exports = {
    getsign: getSign,
    getnssign3: getNSSign3
}

