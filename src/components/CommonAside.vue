<template>
  <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
           :collapse="isCollapse"
           background-color="#545c64"
           text-color="#fff"
           active-text-color="#ffd04b"
  >
<h3>{{ isCollapse ? 'Ylab' : 'Ylab音乐评价平台'}}</h3>
    <el-menu-item @click="clickMenu(item)" v-for="item in noChildren" :key= "item.name" :index="item.name">
      <i :class="'el-icon-${item.icon}'"></i>
      <span slot="title">{{ item.label }}</span>
    </el-menu-item>
    <el-submenu v-for="item in hasChildren" :key= "item.name" :index="item.name" >
      <template slot="title">
        <i :class="'el-icon-${item.icon}'"></i>
        <span slot="title">{{ item.label }}</span>
      </template>
      <el-menu-item-group v-for="subItem in item.children" :key="subItem.path">
        <el-menu-item @click="clickMenu(subItem)" :index="subItem.path">{{ subItem.label }}</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
  </el-menu>
</template>


<style lang="less" scoped>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 160px;
    min-height: 400px;
  }
  .el-menu {
    height: 100vh;
    h3 {
      color: #fff;
      text-align: center;
      line-height: 48px;
      font-size: 16px;
      font-weight: 400;
    }
  }
</style>

<script>
  export default {
    data() {
      return {
        menuData: [
          {
            path: '/',
            name: 'home',
            label: '首页',
            icon: 's-home',
            url: 'Home/Home',
          },
          {
            path: '/user',
            name: 'user',
            label: '开始评价',
            icon: 'user',
            url: 'UserManage/Usermanage',
          },
          //   {
          //   path: '/scorelist',
          //   name: 'scorelist',
          //   label: '评价列表',
          //   icon: 'user',
          //   url: 'ScoreManage/Scoremanage',
          // },
          {
            path: '/page1',
                name: 'page1',
                label: '技巧标注',
                icon: 'setting',
                url: 'Other/PageOne',
          }
          // {
          //   label: '其他',
          //   icon: 'location',
          //   children: [
          //     {
          //       path: '/page1',
          //       name: 'page1',
          //       label: '页面1',
          //       icon: 'setting',
          //       url: 'Other/PageOne',
          //     },
          //     // {
          //     //   path: '/page2',
          //     //   name: 'page2',
          //     //   label: '页面2',
          //     //   icon: 'setting',
          //     //   url: 'Other/PageTwo',
          //     // }
          //   ]
          // }
        ]
      };
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      clickMenu(item) {
        if(this.$route.path !== item.path && !(this.$route.path === '/home' && (item.path === '/'))){
          this.$router.push(item.path)
        }

      }
    },
    computed: {
      noChildren() {
        return this.menuData.filter(item => !item.children)
      },
      hasChildren() {
        return this.menuData.filter(item => item.children)
      },
      isCollapse() {
        return this.$store.state.tab.isCollapse
      }
    }
  }
</script>
<style lang="less" scoped>
.el-menu {
  border: none;
}
</style>