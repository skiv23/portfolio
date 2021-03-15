module.exports = {
  filenameHashing: false,
  pages: {
    index: {
      entry: 'src/main.js',
      title: 'Portfolio'
    }
  },
  pluginOptions: {
    s3Deploy: {
      registry: undefined,
      awsProfile: 'default',
      overrideEndpoint: false,
      region: 'eu-central-1',
      bucket: 's-bondar-dev',
      createBucket: false,
      staticHosting: false,
      assetPath: 'dist',
      assetMatch: '**/*.{js,css}',
      deployPath: '/static/',
      acl: 'private',
      pwa: false,
      enableCloudfront: false,
      pluginVersion: '4.0.0-rc3',
      uploadConcurrency: 5
    }
  }
}
