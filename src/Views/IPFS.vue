<template>
<div class="page-ipfs">

  <md-app md-waterfall md-mode="flexible">
      <md-app-toolbar style="-webkit-app-region: drag" class="md-large md-primary">
        <div class="md-toolbar-row">
          <div class="md-toolbar-section-start">
            <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
              <md-icon>menu</md-icon>
            </md-button>
          </div>

          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button">
              <md-icon>more_vert</md-icon>
            </md-button>
          </div>
        </div>

        <div class="md-toolbar-row md-toolbar-offset">
          <span class="md-display-1">IPFS Disk</span>
        </div>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>
        <md-list>
          <md-list-item>
            <md-icon>move_to_inbox</md-icon>
            <span class="md-list-item-text">Inbox</span>
          </md-list-item>

          <md-list-item>
            <md-icon>send</md-icon>
            <span class="md-list-item-text">Sent Mail</span>
          </md-list-item>

          <md-list-item>
            <md-icon>delete</md-icon>
            <span class="md-list-item-text">Trash</span>
          </md-list-item>

          <md-list-item>
            <md-icon>error</md-icon>
            <span class="md-list-item-text">Spam</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        
          <div>
          <md-button class="md-raised md-primary" @click="uploadSelectFiles" :disabled="selectFiles.length<=0 || uploadProcess">Upload</md-button>
          </div>
        <div class="content-wrap">
          <div class="item-wrap" v-for="item in selectFiles" :key="item.id">
            <video @loadeddata="videoLoaded(item,$event)"  v-if="item.type=='video'" :src="item.objUrl"></video>
            <img v-else-if="item.type=='img'" :src="item.objUrl" alt="">
            <p v-else>{{item.name}}</p>
            <md-icon v-if="!item.uploading && !uploadProcess" @click.native="deleteItem(item.id)" class="fa icon-delete">delete_forever</md-icon>
            <md-progress-spinner  v-if="item.uploading" class="md-accent icon-loading" md-mode="indeterminate"></md-progress-spinner>
          </div>
          <div class="btn-add item-wrap" v-show="!uploadProcess">
            <md-icon class="md-size-2x">add</md-icon>
            <input type="file" @change="change" ref="file"  multiple />
          </div> 
         </div>
      </md-app-content>
      
    </md-app>
  
</div>
</template>
<script>
import ipfsAPI from "ipfs-api";
const ipfs = ipfsAPI({
  host: "ipfs.infura.io",
  port: "5001",
  protocol: "https"
});
export default {
  components: {},
  data() {
    return {
      menuVisible: false,
      selectFiles: [],
      uploadProcess:false
    };
  },
  mounted() {},
  watch: {},
  computed: {},
  methods: {
    videoLoaded(item, event) {
      // /clientWidth clientHeight
      // console.log(item,event)
      // event.target.width = 200
      // event.target.height = 200
    },
    getBuffer(file) {

      return new Promise((resolove, reject) => {
        let reader = new FileReader();
        reader.readAsArrayBuffer(file);

        reader.onerror = err => {
          reject(err);
        };

        reader.onabort = err => {
          reject(err);
        };

        reader.onloadend = () => {
          resolove(Buffer.from(reader.result));
        };
      });
    },
    async change() {
      // debugger;
      for (let i = 0; i < this.$refs.file.files.length; i++) {
        let file = this.$refs.file.files[i];
        // debugger;
        console.log(this.selectFiles.find(f => f.id == file.path));
        if (!this.selectFiles.find(f => f.id == file.path)) {
          let item = {};
          item.uploading = false;
          item.source = file;
          item.id = file.path;
          item.buffer = await this.getBuffer(file);
          item.name = item.source.name;
          item.objUrl = window.URL.createObjectURL(file);
          console.log(item.buffer);
          if (file.type.indexOf("image") != -1) {
            item.type = "img";
          } else if (file.type.indexOf("video") != -1) {
            item.type = "video";
          } else {
            item.type = "other";
          }

          this.selectFiles.push(item);
        }
      }

      this.$refs.file.value = "";
    },
    async uploadSelectFiles() {
      // ipfs.add(buffer)
      this.uploadProcess = true;
      for (let index = 0; index < this.selectFiles.length; index++) {
        const item = this.selectFiles[index];
        item.uploading = true;
        let result = await ipfs.add(item.buffer)
        item.uploading = false;
        item.hash = result.hash
        console.log(result)
      }
      this.uploadProcess = false;
      // this.selectFiles.forEach(item=>{
        
      // })
    },
    deleteItem(id){
      this.selectFiles.splice(this.selectFiles.findIndex(item => (item.id = id)), 1);
    }
  }
};
</script>

<style lang="less">
.page-ipfs {
  height: 100%;
  width: 100%;

  .md-app {
    height: 100%;
    width: 100%;
  }
  .md-toolbar {
    -webkit-app-region: drag;
  }
  .content-wrap {
    display: flex;
    flex-wrap: wrap;
  }
  .item-wrap {
    position: relative;
    display: flex;
    overflow: hidden;
    width: 200px;
    height: 200px;
    margin: 5px;
    border: 1px dashed #d9d9d9;
    justify-content: center;
    align-items: center;
    border-radius: 6px;
    .video-wrap {
      max-width: none;
    }
    .image-wrap {
      max-height: 100%;
      max-width: 100%;
    }
    .icon-delete {
      position: absolute;
      top: 0;
      right: 0;
    }
    .icon-loading {
      // top: 50%;
      // left: 50%;
      position: absolute;
      transform: translate(-50%, -50%);
    }
  }

  .btn-add {
    cursor: pointer;
    .md-icon {
      top: 50%;
      left: 50%;
      position: absolute;
      transform: translate(-50%, -50%);
    }
    input[type="file"] {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      padding: 0;
      margin: 0;
      opacity: 0;
    }
  }
}
</style>
