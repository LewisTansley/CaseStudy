<template>
  <el-row>
      <el-card :body-style="{ padding: '0px' }">
        <img src="" class="image">
        <div style="padding: 14px;">
          <span>TITLE</span>
          <div class="bottom clearfix">
            <p class="greyText">AUTHOR</p>
            <p class="greyText">DESCRIPTION</p>
            <el-button type="text" class="primary">read more</el-button>
            <el-row>
              <el-col :span="12"><el-button type="primary">Edit</el-button></el-col>
              <el-col :span="12"><el-button type="danger">Delete</el-button></el-col>
            </el-row>
          </div>
        </div>
      </el-card>
  </el-row>
</template>

<style>
  .greyText {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
  .el-row{
    max-width: 80%;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
  }
</style>