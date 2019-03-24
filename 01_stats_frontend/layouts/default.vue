<template>
  <div class="main">

    <!--<Header class="header"/>-->

    <!--<div class="container">-->
      <div class="content">

        <section>
          <nuxt/>
        </section>

      </div>
    <!--</div>-->

  </div>
</template>

<script>
  import Header from '../components/Header';
  import Footer from '../components/Footer';

  export default {
    components: {Footer, Header},
  };
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Open+Sans');
  @import url('https://fonts.googleapis.com/css?family=Montserrat');

  html {
    font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    word-spacing: 1px;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
  }

  body {
    font-family: 'Open Sans', sans-serif;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
  }


</style>

