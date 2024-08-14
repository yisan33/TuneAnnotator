<template>
  <div class="custom-tooltip-wrapper" @mouseover="showTooltip" @mouseleave="hideTooltip">
    <slot></slot>
    <div v-if="visible" class="custom-tooltip-content">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: false
    }
  },
  methods: {
    showTooltip() {
      this.visible = true;
    },
    hideTooltip() {
      this.visible = false;
    }
  }
}
</script>

<style scoped>
.custom-tooltip-wrapper {
  position: relative;
  display: inline-block;
}

.custom-tooltip-content {
  position: absolute;
  background-color: #f0f4f7; /* 背景色 */
  color: #333; /* 字体颜色 */
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  white-space: nowrap;
  z-index: 1000;
  transition: opacity 0.3s ease;
  opacity: 0;
  transform: translateY(-10px);
}

.custom-tooltip-wrapper:hover .custom-tooltip-content {
  opacity: 1;
  transform: translateY(0);
}
</style>
