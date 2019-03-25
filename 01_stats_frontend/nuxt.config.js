module.exports = {
  /*
   ** Headers of the page
   */
  head: {
    title: 'Stats',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: 'Nuxt.js project'},
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'},
    ],
  },
  modules: [
    '@nuxtjs/moment',
  ],
  plugins: [
    '~/plugins/buefy',
    '~/plugins/axios',
    {src: '~/plugins/vue-apexchart.js', ssr: false},
  ],

  css: [
    '~/assets/scss/main.scss',
  ],
  /*
   ** Customize the progress bar color
   */
  loading: {color: '#3B8070'},
  /*
   ** Build configuration
   */


  build: {

    vendor: ['vue-apexchart'],
    /*
     ** Run ESLint on save
     */
    extend(config, {isDev, isClient}) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/,
        });
      }
    },
  },
};

