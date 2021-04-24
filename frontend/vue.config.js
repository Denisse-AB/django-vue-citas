module.exports = {
  // outputDir: path.resolve(__dirname, '../server/public'),
  devServer: {
    proxy: {
      '/post': {
        target: 'http://localhost:8000'
      }
    }
  }
}
