const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const FileManagerPlugin = require("filemanager-webpack-plugin");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const webpack = require("webpack");

module.exports = merge(common, {
  devtool: "source-map",
  plugins: [
    new UglifyJsPlugin({ sourceMap: true, cache: true, parallel: true }),
    new HtmlWebpackPlugin({
      template: "./public/index.ejs",
      filename: "../dist/index.html"
    }),
    new FileManagerPlugin({
      onEnd: {
        mkdir: ["./public/dist/assets"],
        copy: [
          { source: "./public/assets", destination: "./public/dist/assets" }
        ]
      }
    }),
    new webpack.DefinePlugin({
      DEV: false
    })
  ]
});
