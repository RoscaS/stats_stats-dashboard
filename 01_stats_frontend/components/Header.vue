<template>
  <div class="header">
    <h1 class="title"><span class="manager">Mon'</span>titre</h1>
    <p>Et son sous-titre</p>
  </div>
</template>

<script>
  export default {
    name: 'Header',
  };
</script>

<style lang="scss" scoped>

  .header {
    padding: 30px 0 50px 0;
    text-align: center;
    background: white;

    h1 {
      font-size: 50px;
    }

    .manager {
      color: #e96900;
    }
  }


</style>
