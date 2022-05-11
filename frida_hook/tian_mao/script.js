function getMapData(mapSet) {
    var result = {};
    var key_set = mapSet.keySet();
    var it = key_set.iterator();
    while (it.hasNext()) {
        var key_str = it.next().toString();
        result[key_str] = mapSet.get(key_str).toString();
    }

    return result
}


function getXSign(params) {
    var result = '';
    Java.perform(function () {
        Java.enumerateClassLoaders({
            onMatch: function (loader) {
                try {
                    if (loader.findClass('com.taobao.wireless.security.adapter.JNICLibrary')) {
                        console.log('loader: ', loader);
                        Java.classFactory.loader = loader;
                    }
                } catch (error) {
                }
            },
            onComplete: function () {
            }
        });

        var JNICLibrary = Java.use('com.taobao.wireless.security.adapter.JNICLibrary');
        var hashMap = Java.use('java.util.HashMap');

        var a1 = Java.use('java.lang.Integer').$new(0);
        var p1 = Java.array('Ljava.lang.Object;', [a1]);
        var res1 = JNICLibrary.doCommandNative(22301, p1);
        console.log('res1: ', res1);

        var a2 = Java.use('java.lang.Integer').$new(0);
        var a3 = Java.use('java.lang.Boolean').$new(true);
        var p2 = Java.array('Ljava.lang.Object;', [a2, a3]);
        var res2 = JNICLibrary.doCommandNative(22302, p2);
        console.log('res2: ', res2);

        var a = '' +
            'YNCoyETQXFUDAD6xvGW8c/tk&&&' +
            '23181017&' +
            '7e5fa4a04006ccd2dd430485bf947743&' +
            '1624375174&' +
            'mtop.alibaba.mum.citem.get&' +
            '1.0&&' +
            '231200@tmall_android_10.7.0&' +
            'Av7FBE_0MsxQF2sMj7Ir0W182Q_p3_mlWCKy-pK45lTs&&&' +
            'openappkey=DEFAULT_AUTH&27&&&&&&&';

        var ps = [
            Java.use('java.lang.String').$new('23181017'),
            Java.use('java.lang.String').$new('YNCoyETQXFUDAD6xvGW8c/tk&&&23181017&7e5fa4a04006ccd2dd430485bf947743&1624375174&mtop.alibaba.mum.citem.get&1.0&&231200@tmall_android_10.7.0&Av7FBE_0MsxQF2sMj7Ir0W182Q_p3_mlWCKy-pK45lTs&&&openappkey=DEFAULT_AUTH&27&&&&&&&'),
            Java.use('java.lang.Boolean').$new(false),
            Java.use('java.lang.Integer').$new(0),
            Java.use('java.lang.String').$new('mtop.alibaba.mum.citem.get'),
            Java.use('java.lang.String').$new('pageId=&pageName='),
            null,
            null,
            null,
            Java.use('java.lang.String').$new('r_18'),
        ];
        var p3 = Java.array('Ljava.lang.Object;', ps);
        result = JNICLibrary.doCommandNative(70102, p3);
        result = getMapData(Java.cast(result, hashMap));
    });

    return result;
}


rpc.exports = {
    getxsign: getXSign
};
