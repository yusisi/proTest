// https://www.npmjs.com/package/web-pwa

import SW,{Notify,WebCaches} from 'web-pwa';
 
window.onload = function(){
    SW.register('sw.js');
    var tableName = 'prefetch-cache-v1';
    WebCaches.table(tableName).addRow('/app.js')
    .then(res=>{
        // res: 成功
    })
    Notify.request() // 请求推送权限
    .then(permission=>{
        // 用户同意
        Notify.show('villianhr','Hello Pwa')
        .onclick(event=>{
            event.close(); // 关闭当前 Notification
            Notify.focus(); // 聚焦窗口
        })
    })
}