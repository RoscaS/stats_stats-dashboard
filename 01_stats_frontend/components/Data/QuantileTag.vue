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
      value: {type: String},
    },
  };
</script>

<style lang="scss" scoped>

</style>
