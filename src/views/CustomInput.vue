<template>
  <div class="input-data">
    <i v-if="icon" :class="icon"></i>
    <input :type="type" v-model="localValue" @input="updateValue" required>
    <div class="underline"></div>
    <label>{{ placeholder }}</label>
  </div>
</template>

<script>
export default {
  props: {
    value: String,
    placeholder: String,
    type: {
      type: String,
      default: 'text' // 默认类型为文本
    },
    icon: String
  },
  data() {
    return {
      localValue: this.value
    }
  },
  methods: {
    updateValue(event) {
      this.$emit('input', event.target.value)
    }
  },
  watch: {
    value(newValue) {
      this.localValue = newValue
    }
  }
}
</script>

<style scoped>
.input-data {
  position: relative;
  width: 100%;
  height: 40px;
  margin-bottom: 40px;
  display: flex; /* 新增的 flex 布局 */
  align-items: center; /* 垂直居中对齐 */
}

.input-data i {
  font-size: 19px;
  margin-right: 10px;
  opacity: 0.3; /* 透明度，0.0 - 1.0，值越小越透明 */
}

.input-data input {
  width: 100%;
  height: 100%;
  border: none;
  outline: none; /* 去除默认的焦点边框 */
  background: transparent;
  font-size: 17px;
  border-bottom: 2px solid #c0c0c0;
}

.input-data input:focus ~ label,
.input-data input:valid ~ label {
  transform: translateY(-20px);
  font-size: 15px;
  color: #2c6fdb;
}

.input-data label {
  position: absolute;
  bottom: 10px;
  left: 30px; /* 调整左边距 */
  color: #808080;
  pointer-events: none;
  transition: all 0.3s ease;
}

.input-data .underline {
  position: absolute;
  bottom: -2px;
  height: 2px;
  width: 100%;
  background-color: #2c6fdb;
  transform: scaleX(0);
  transition: all 0.3s ease;
}

.input-data input:focus ~ .underline,
.input-data input:valid ~ .underline {
  transform: scaleX(1);
}
</style>
