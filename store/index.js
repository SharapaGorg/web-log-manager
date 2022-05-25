export const state = () => ({
  levelsFilter : ['WARNING', 'ERROR', 'DEBUG', 'INFO'],
  filterText : '',
  filterTime : ['1970/2/1', '3000/12/30'],
  filterTimeInSeconds: [],
  filtered : true,
  currentTable : 'logs',
  api : 'http://127.0.0.1:5000/',
  logStates: {
    time : true,
    level : true,
    content : true
  }
})

export const mutations = {
  turnLogState(state, field) {
    state.logStates[field] = !state.logStates[field]
  },
  reFilter(state) {
    state.filtered = !state.filtered
  },
  changeFillFilter(state, value) {
    state.levelsFilter = value
  },
  changeFilterText(state, value) {
    state.filterText = value
  },
  changeFilterTime(state, [index, value]) {
    state.filterTime[index] = value
  },
  replaceFilterTimeInSeconds(state, value) {
    state.filterTimeInSeconds = value
  },
  setCurrentTable(state, value) {
    state.currentTable = value
  }
}
