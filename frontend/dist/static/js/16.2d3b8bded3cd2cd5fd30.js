webpackJsonp([16],{"6Tb+":function(t,e){},bogQ:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("P9l9"),i={data:function(){return{tableData:[],total:0,page:1,listLoading:!1}},methods:{handleCurrentChange:function(t){this.page=t,this.getProjectDynamic()},getProjectDynamic:function(){this.listLoading=!0;var t=this,e={project_id:Number(this.$route.params.project_id),page:t.page},a={"Content-Type":"application/json",Authorization:"Token "+JSON.parse(sessionStorage.getItem("token"))};Object(n.s)(a,e).then(function(e){var a=e.msg,n=e.code,i=e.data;t.listLoading=!1,"999999"===n?(t.total=i.total,t.tableData=i.data):t.$message.error({message:a,center:!0})})}},mounted:function(){this.getProjectDynamic()}},o={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-row",{staticClass:"dynamic-manage"},[a("el-col",{attrs:{span:24}},[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.listLoading,expression:"listLoading"}],staticStyle:{width:"100%"},attrs:{data:t.tableData,stripe:""}},[a("el-table-column",{attrs:{prop:"time",label:"操作时间","min-width":"13%"}}),t._v(" "),a("el-table-column",{attrs:{prop:"type",label:"类型","min-width":"10%"}}),t._v(" "),a("el-table-column",{attrs:{prop:"operationObject",label:"操作对象","min-width":"15%"}}),t._v(" "),a("el-table-column",{attrs:{prop:"operationUser",label:"操作人","min-width":"15%"}}),t._v(" "),a("el-table-column",{attrs:{prop:"description",label:"描述","min-width":"47%"}})],1),t._v(" "),a("el-pagination",{staticStyle:{float:"right"},attrs:{layout:"prev, pager, next","page-size":20,"page-count":t.total},on:{"current-change":t.handleCurrentChange}})],1)],1)},staticRenderFns:[]};var r=a("VU/8")(i,o,!1,function(t){a("6Tb+")},"data-v-af1638d6",null);e.default=r.exports}});
//# sourceMappingURL=16.2d3b8bded3cd2cd5fd30.js.map