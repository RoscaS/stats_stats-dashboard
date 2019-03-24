<template>
  <footer class="footer">
    <div class="content has-text-centered">

      <p>Copyright &copy; {{ getCopyright() }}
        <a class="jrosk" href="mailto:jrosk.managment@gmail.com"
           title="With  by Sol Rosca">
          JrosK
        </a>
      </p>

    </div>
  </footer>
</template>

<script>
  import moment from 'moment';

  export default {
    name: 'Footer',
    methods: {
      getCopyright() {
        return moment().format('Y');
      },
    },
  };
</script>

<style lang="scss" scoped>

  footer {
    height: 50px;
  }

  a {
    margin-left: 10px;

    &:hover {
      color: #7957D5;
      text-decoration: underline;
    }
  }

</style>
