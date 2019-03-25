<template>
  <div class="tags has-addons">
    <span class="tag is-dark">Q{{Q}}</span>
    <span class="tag is-primary">{{value}}</span>
  </div>
</template>

<script>
  export default {
    props: {
      Q: {type: String},
      value: {type: Number},
    },
  };
</script>

<style lang="scss" scoped>

  .tags {
    margin-left: 4px;
    /*margin-top: 10px;*/
  }

</style>
