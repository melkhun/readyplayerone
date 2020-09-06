<template>
  <div class="card">
    <div class="card-body">
      <h2 class="card-title">Breakdown of Instrument Types</h2>

      <!-- {{countEtf}}
      {{countBond}}
      {{countFuture}}
      {{countOption}}
      {{countEquity}} -->
    </div>
<v-btn @click="asd">asd</v-btn>
    <div class="card-img-bottom">
      <chartjs-doughnut
        :bind="true"
        :datasets="datasets"
        :labels="labels"
        :option="option"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: ['countEtf', 'countBond', 'countFuture', 'countOption', 'countEquity'],
  data() {
    return {
      datasets: [
        {
          data: [0,0,0,0,0], //Think we need compute
          backgroundColor: ["#8544FA", "#493CDE", "#9FA8D", "#3C84DE", "#44C5FA"],
          hoverBackgroundColor: ["#B47DFA", "#7567E0", "#C5CA", "#77ADE0", "#A2EAFA"]
        }
      ],
      labels: ["ETFs", "Bonds", "Futures", "Options", "Equities"], //input instrument type as labels
      option: {}
    };
  },

};
</script>


<style scoped>

</style>