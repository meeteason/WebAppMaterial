// import webmodellist from "./web-model-list"
import webupload from "./web-upload"
import toast from "./web-toast"
const install = Vue => {
  // Vue.component(webmodellist.name, webmodellist)
  Vue.component(webupload.name, webupload)
  Vue.component(toast.name, toast)
}
export default {
  install
}
