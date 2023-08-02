<template>
  <el-row>
    <el-col :span="24" v-for="(o, index) in 1" :key="o" :offset="index > 0 ? 1 : 0">
      <el-card :body-style="{ padding: '0px' }">
        <img src="" class="image">
        <div style="padding: 14px;">
          <h1>Add new Book</h1>
          <div class="bottom clearfix">
            <p class="greyText"></p>
            <p class="greyText"></p>
            <el-button type="text" class="primary"></el-button>
            <el-row>
              <el-col :span="24"><router-link to="/DataEntry"><el-button type="primary">Add</el-button></router-link></el-col>
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