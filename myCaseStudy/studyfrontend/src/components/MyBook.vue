<template>
  <el-row>
    <el-col :span="6" v-for="(o, index) in 3" :key="o" :offset="index > 0 ? 3 : 0">
      <el-card :body-style="{ padding: '0px' }">
        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        <div style="padding: 14px;">
          <span>BOOK NAME</span>
          <div class="bottom clearfix">
            <p class="greyText">author</p>
            <p class="greyText">description</p>
            <el-button type="text" class="primary">read more</el-button>
            <el-row>
              <el-col :span="12"><el-button type="primary">Edit</el-button></el-col>
              <el-col :span="12"><el-button type="danger">Delete</el-button></el-col>
            </el-row>
          </div>
        </div>
      </el-card>
    </el-col>
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
  }
</style>