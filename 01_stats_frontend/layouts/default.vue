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



  body {
    font-family: 'Open Sans', sans-serif !important;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif !important;
  }


</style>

