module.exports = {
  devServer: {
    proxy: {
      '/post': {
        target: 'http://localhost:8000'
      }
    }
  }
}
