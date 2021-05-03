module.exports = {
  devServer: {
    proxy: {
      '/post': {
        target: 'http://localhost:8000'
      }
    }
  },

  pluginOptions: {
    i18n: {
      locale: 'es',
      fallbackLocale: 'en',
      localeDir: 'plugins',
      enableInSFC: true
    }
  }
}
