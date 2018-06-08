<template>
<div  class="page-container">
    <!-- <md-app md-waterfall md-mode="flexible">
      <md-app-toolbar class="md-large md-primary">
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
          <span class="md-display-1">My Title</span>
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
         <router-view/>  
         
      </md-app-content>
      
    </md-app>
  
      <md-bottom-bar  md-type="shift" @md-changed="checkNewPosts">
          <md-bottom-bar-item md-label="Home" md-icon="home"></md-bottom-bar-item>
          <md-bottom-bar-item md-label="Pages" md-icon="pages"></md-bottom-bar-item>
          <md-bottom-bar-item md-label="Favorites" md-icon="favorite"></md-bottom-bar-item>
      </md-bottom-bar> -->
    
    <router-view/> 
    <!-- <md-dialog-alert
      :md-active="Alert.show" v-on:update:mdActive="$store.commit('setAlert',{show:false})"
      :md-content="Alert.msg"
      :md-confirm-text="Alert.btnText" />

      <web-toast /> -->
  </div> 
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "App",
  data() {
    return {
      menuVisible: false
    };
  },
  methods:{
    // aa(){
    //   alert('aa')
    // }
  },
  computed: {
    ...mapState(["Header", "BottomBar", "Alert", "isLoading"])
  },
  mounted(){
    console.log(this.$store)

    // this.$alert({show:true,msg:"aaaaa",btnText:"aaaaaadd"})
  }
};
</script>


