const path = require("path");
const ManifestPlugin = require("webpack-manifest-plugin");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const webpack = require("webpack");
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  entry: "./static/index.js",
  output: {
    filename: "index.js",
    path: path.resolve(__dirname, "templates")
  },
  target: 'web',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader"
        }
      },{
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
         test: /\.scss$/,
         use: [{
           loader: 'style-loader'
         }, {
           loader: 'css-loader'
         }, {
           loader: 'sass-loader'
         }]
       },
        {
          test: require.resolve("jquery"),
          use: [
            {
              loader: "expose-loader",
              options: "$"
            }
          ]
        }
    ]
  },
  plugins: [
    new ManifestPlugin(),
    new CleanWebpackPlugin(["dist"]),
    // new webpack.ProvidePlugin({
    //   $: "jquery",
    //   jQuery: "jquery",
    //   "window.jQuery": "jquery"
    // }),
    new VueLoaderPlugin()
  ]
};
