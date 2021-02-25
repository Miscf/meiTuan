rpc.exports = {
    getmtgsig: function (str) {
        Java.perform(function () {
            let nb = Java.use("com.meituan.android.common.mtguard.NBridge");
            let main = nb.main;
            let Integer = Java.use("java.lang.Integer");
            let JavaString = Java.use("java.lang.String");

            let forteststring = JavaString.$new(str);

            let test_arg = [
                "e68c4c18-35ec-4972-84e4-32a0836455a8",  // 应该是下载app的时候注册的
                forteststring.getBytes(),
                Integer.$new(2)
            ]

            let result = main.call(nb, 203, test_arg);
            send(result.toString());
        })
    }
}
