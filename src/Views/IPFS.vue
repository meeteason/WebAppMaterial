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
            <md-button @click="getLocalData"   class="md-icon-button">
              <md-icon>refresh</md-icon>
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
          <md-list-item @click="current='Home'">
            <md-icon>home</md-icon>
            <span class="md-list-item-text">Home</span>
          </md-list-item>
          <md-list-item @click="current='All'">
            <md-icon>folder</md-icon>
            <span class="md-list-item-text">All</span>
          </md-list-item>

          <md-list-item @click="current='Videos'">
            <md-icon>video_library</md-icon>
            <span class="md-list-item-text">Videos</span>
          </md-list-item>

          <md-list-item @click="current='Images'">
            <md-icon>collections</md-icon>
            <span class="md-list-item-text">Images</span>
          </md-list-item>

          <md-list-item @click="current='Other'">
            <md-icon>attach_file</md-icon>
            <span class="md-list-item-text">Other</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <div v-show="current=='Home'">          
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
        </div>
        <div v-show="current!='Home'">
            <div class="content-wrap">
              <div class="item-wrap" v-for="item in localData" :key="item.id">
                <video controls preload="auto" @loadeddata="videoLoaded(item,$event)"  v-if="item.type=='video'" :src="'https://ipfs.io/ipfs/'+item.id"></video>
                <img v-else-if="item.type=='img'" :src="'https://ipfs.io/ipfs/'+item.id" alt="">
                <p v-else>{{item.name}}</p>
                <!-- <md-icon v-if="!item.uploading && !uploadProcess" @click.native="deleteItem(item.id)" class="fa icon-delete">delete_forever</md-icon>
                <md-progress-spinner  v-if="item.uploading" class="md-accent icon-loading" md-mode="indeterminate"></md-progress-spinner> -->
              </div>
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
      uploadProcess: false,
      current: "Home",
      localData: []
    };
  },
  mounted() {
    this.getLocalData();
  },
  watch: {
    current() {
      if (this.menuVisible) this.menuVisible = false;
    }
  },
  computed: {},
  methods: {
    videoLoaded(item, event) {},
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
        // console.log(
        //   this.selectFiles.find(
        //     f => f.id == (file.path ? file.path : file.name)
        //   )
        // );
        if (!this.selectFiles.find(f => f.id == file.path)) {
          let item = {};
          item.uploading = false;
          item.source = file;
          item.id = file.path ? file.path : file.name;
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
      
      this.uploadProcess = true;
      while (this.selectFiles.length > 0) {
        let item = this.selectFiles[0];
        item.uploading = true;
        let result = await ipfs.add(item.buffer);
        item.uploading = false;
        item.hash = result[0].hash;
        this.saveLocal(item);
        this.selectFiles.shift();
      }
      this.uploadProcess = false;
      // for (let index = 0; index < this.selectFiles.length; index++) {
      //   const item = this.selectFiles[index];

      //   console.log(result);
      // }
    },
    deleteItem(id) {
      this.selectFiles.splice(
        this.selectFiles.findIndex(item => (item.id = id)),
        1
      );
    },
    saveLocal(item) {
      let localData = localStorage.getItem("save");
      if (!localData) localData = [];
      else localData = JSON.parse(localData);

      let findResult = localData.find(saveData => saveData.id == item.hash);
      if (!findResult) {
        localData.push({
          id: item.hash,
          type: item.type,
          time: Date.now()
        });
      }

      localStorage.setItem("save", JSON.stringify(localData));
      this.getLocalData();
    },
    getLocalData() {
      let localData = localStorage.getItem("save");
      if (!localData) localData = [];
      else localData = JSON.parse(localData);

      this.localData = localData;
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
