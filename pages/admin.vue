<template>
  <div ref="root">
    <div class="login-panel">
      <span class="field-header">TOKEN</span><br/>
      <the-mask :mask="['AAAA-####']"
                class="token-field"
                placeholder="SMTH-1234"
                v-model="fieldContent"
      />
    </div>

    <div v-show="tokenIsWrong"
         class="token-warning"
          @click="tokenIsWrong = false">TOKEN IS WRONG !</div>

    <div class="accept-button" @click="accept">
      Next
    </div>
  </div>
</template>

<script>

import { TheMask } from 'vue-the-mask'

export default {
  name: "admin",
  components: {
    TheMask
  },
  data() {
    return {
      fieldContent : '',
      tokenIsWrong: false,
      correctToken : 'NAME1234'
    }
  },
  mounted() {
      const storageField = localStorage.getItem('accept')
      if (storageField && storageField === 'accepted') {
        this.fieldContent = this.correctToken
      }
  },
  methods: {
    accept() {
      if (this.fieldContent === this.correctToken) {
        localStorage.setItem('accept', 'accepted')
        this.$router.push('adminPanel')
      }
      else {
          this.tokenIsWrong = true
      }
    }
  },
  watch: {
    fieldContent (value) {
      this.tokenIsWrong = false
    }
  }
}
</script>

<style scoped>

.token-warning {
  @apply text-[#c7bcbc] w-fit cursor-pointer block mx-auto my-1 border-[#c7bcbc];
  @apply rounded-sm border-2 px-2 font-bold
}

.login-panel {
  font-family: 'Ubuntu Mono', monospace;
  @apply pt-2 pb-4 px-4 mx-auto w-fit border-[#c7bcbc];
  @apply border-2 rounded-md mt-[50px]
}

.field-header {
  @apply text-[#c7bcbc] font-bold text-center inline-block w-full
}

.token-field {
  @apply px-2 py-1 rounded-md outline-none
}

.accept-button {
  font-family: 'Ubuntu Mono', monospace;
  @apply w-[150px] px-2 py-1 mx-auto text-center bg-[#c7bcbc] rounded-md mt-1;
  @apply cursor-pointer
}

</style>
