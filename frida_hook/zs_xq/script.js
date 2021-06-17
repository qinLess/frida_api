// 知识星球 用户私信 hook
function sendMessage(messageInfo) {
    Java.perform(function () {
        Java.scheduleOnMainThread(function () {
            var eClass = Java.use('com.unnoo.quan.l0.e.g.e')
            var V2TIMManager = Java.use('com.tencent.imsdk.v2.V2TIMManager')
            var getMessageManager = V2TIMManager.getMessageManager()

            // var userUid = 422211111548428
            // var userName = 'Bumpy Life'
            // var avatarUrl = 'https://images.zsxq.com/FpB-c8T85wOKTBY000fkMibiCTrH?e=1622476799&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:0Y5VjSMpl4ypuJTMA1WpSalhir0='
            // var userId = 'RU29129613'
            // var groupId = 48418284215218
            // var groupName = '火星'
            // var content = '哈哈哈哈'

            var randomUuid = '00064ca39188e744875890eb0aa8e6465f0'
            var accountId = Number(messageInfo['account_id'])
            var accountName = messageInfo['account_name']
            var avatarUrl = messageInfo['avatar_url']
            // var identifier = 'RU29129613'
            var identifier = messageInfo['identifier']
            var groupId = Number(messageInfo['group_id'])
            var groupName = messageInfo['group_name']
            var content = messageInfo['content']

            var message = eClass.m(randomUuid, accountId, accountName, avatarUrl, identifier, groupId, groupName, content)
            getMessageManager.sendMessage(message, identifier, null, 2, false, null, null)
            eClass.d(message)
        })
    })
}

rpc.exports = {
    sendmessage: sendMessage
}

