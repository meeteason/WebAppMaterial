import Vue from 'vue'

import webToast from "./web-toast"

// var webToast = require("./web-toast")
console.log(webToast.render())


const ToastConstructor = Vue.extend(webToast);



ToastConstructor.prototype.open = (title) => {
    instance.title = title || '';

    document.body.appendChild(instance.$el);

    pageScroll.lock();
};

ToastConstructor.prototype.close = function () {
    const el = instance.$el;
    el.parentNode && el.parentNode.removeChild(el);

    pageScroll.unlock();
};


const instance = new ToastConstructor({
    el: document.createElement('div')
});

export default {
    open: instance.open,
    close: instance.close
};