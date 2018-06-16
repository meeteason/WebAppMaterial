<template>
<md-snackbar :md-position="position" :md-duration="isInfinity ? Infinity : duration" :md-active.sync="showSnackbar" md-persistent>
      <span>Connection timeout. Showing limited messages!</span>
      <md-button class="md-primary" @click="showSnackbar = false">Retry</md-button>
    </md-snackbar>
</template>
<script>
export default {
  name:"web-toast",
  components: {},
  props: {
    isInfinity: {
      type: Boolean,
      default: false
    },
    duration: {
      type: Number,
      default: 2000
    }
  },
  data() {
    return {
      position: "center",
      showSnackbar: true
    };
  },
  mounted() {},
  watch: {},
  computed: {},
  methods: {}
};
</script>