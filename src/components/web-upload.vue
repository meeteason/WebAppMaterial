<template>
  <div class="md-web-upload md-layout md-gutter">
    <div class="upload-show-img" v-for="item in files" v-bind:key="item.url">
      <img @load="onImgLoad(item,$event)" :src="item.url" alt="">
      <md-icon v-if="item.uploaded" @click.native="delImg(item.id)" class="fa">delete_forever</md-icon>
      <md-progress-spinner v-if="!item.uploaded" class="md-accent" md-mode="indeterminate"></md-progress-spinner>
    </div>
    <div class="btn-imgadd">
      <md-icon class="md-size-2x">add</md-icon>

      <input type="file" @change="change" ref="file" :accept="accept" :name="name" multiple />

    </div>
    <!-- <button @click="upload">上传</button> -->
    <!-- <form ref="form" enctype="multipart/form-data">
    </form> -->
  </div>
</template>
<script>
// import $ from 'jQuery'
export default {
  name: "web-upload",
  props: {
    name: {
      type: String,
      default: "smfile"
    },
    SSL: {
      type: Boolean,
      default: true
    },
    accept: {
      type: String,
      default: "image/gif, image/jpeg ,image/png"
    },
    size: {
      type: Number,
      default: 5
    },
    multiple: {
      type: Boolean,
      default: false
    },
    placeholder: {
      type: String,
      default: "请选择图片"
    },
    count: {
      type: Number,
      default: 10
    }
  },
  data() {
    return {
      action: "https://sm.ms/api/upload?inajax=1&ssl=1",
      files: []
    };
  },
  mounted() {
    // $(this.$refs.form).ajaxForm({
    //   beforeSubmit: () => {
    //     let tooBig = false
    //     // document
    //     let files = this.$refs.form.querySelector('input[type=file]').files
    //     if (files.length > 10) {
    //       this.$message.error(`the files less than 10`)
    //       return false
    //     }
    //     for (let i = 0; i < files.length; i++) {
    //       let fileSize = files[i].size / 1024 / 1024
    //       if (fileSize > this.size) {
    //         this.$message.error(`the file size less than ${this.size}M`)
    //         tooBig = true
    //         return false
    //       }
    //     }
    //     return !tooBig
    //   },
    //   beforeSend: () => {
    //     this.$emit('beforeSend', this.$refs.file)
    //   },
    //   success: data => {
    //     console.log(data)
    //     this.$emit('update:imgData', data)
    //   },
    //   error: err => {
    //     //失败
    //     // alert('表单提交异常！' + err.msg)
    //     this.$message.error(err)
    //   },
    //   complete: xhr => {
    //     //完成
    //     // status.html(xhr.responseText)
    //     console.log(xhr)
    //   }
    // })
  },
  methods: {
    change() {
      if (this.$refs.file.files.length > this.count) {
        alert("一次只能上传" + this.count + "张图片");
        return false;
      }
      for (let index = 0; index < this.$refs.file.files.length; index++) {
        const element = this.$refs.file.files[index];
        console.log(element, this.files);
        if (!this.files.find(item => item.id == element.name)) {
          let item = {
            id: element.name,
            url: window.URL.createObjectURL(element),
            obj: element,
            uploaded: false
          };
          this.files.push(item);
          this.uploadImg(item);
        }
      }
      this.$refs.file.value = "";
    },
    uploadImg(item) {
      let ajaxForm = new FormData(),
        request = new XMLHttpRequest();
      ajaxForm.append(this.name, item.obj);
      request.open("post", this.action, true);
      request.onload = () => {
        item.uploaded = true;
        this.$emit("imgList", item);
      };
      request.send(ajaxForm);
    },
    delImg(id) {
      console.log(this.files.findIndex(item => (item.id = id)));
      this.files.splice(this.files.findIndex(item => (item.id = id)), 1);
    },
    onImgLoad(item, event) {
      if (event.target.width > event.target.height) {
        event.target.className = "w100";
      } else {
        event.target.className = "y100";
      }
      console.log(event.target, event.target.className);
    }
  }
};
</script>
<style lang="less">
.md-web-upload {
  .upload-show-img {
    position: relative;
    display: inline-block;
    overflow: hidden;
    width: 30vw;
    height: 30vw;
    margin: 5px;
    background-color: #666;

    img {
      position: absolute;
    }
    img.w100 {
      width: 100%;
      top: 50%;
      transform: translate(0, -50%);
    }
    img.y100 {
      height: 100%;
      left: 50%;
      transform: translate(-50%, 0);
    }
    .md-progress-spinner {
      position: absolute;
      top: 25%;
      left: 25%;
      // transform: translate(-50%, -50%);
    }
    .md-icon-font {
      color: #ccc;
      position: absolute;
      top: 0;
      right: 0;
    }
  }
  .btn-imgadd {
    position: relative;
    display: inline-block;
    overflow: hidden;
    width: 30vw;
    height: 30vw;
    margin: 5px;
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
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


