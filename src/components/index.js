// import webmodellist from "./web-model-list"
import webupload from "./web-upload"
const install = Vue => {
  // Vue.component(webmodellist.name, webmodellist)
  Vue.component(webupload.name, webupload)
}
export default {
  install
}
