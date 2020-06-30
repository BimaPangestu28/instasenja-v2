<template>
  <div>
    <Subheader title="Bot Account" subtitle="List of bot account for instagram" />
    <Table
      title="Bot Account"
      subtitle="You can read all bot account instagram"
      :payloads="payloads"
      :fields="['name', 'phone', 'website']"
      :destroy="destroy"
      :canPrev.sync="canPrev"
      :canNext.sync="canNext"
      :totalPaginate.sync="totalPaginate"
      :paginateSelect.sync="paginateSelect"
    />
  </div>
</template>

<script>
import Subheader from "../components/Subheader";
import Table from "../components/Table";

import axios from "axios";

export default {
  components: {
    Subheader,
    Table
  },

  data() {
    return {
      payloads: [],
      showForm: false,
      canPrev: false,
      canNext: false,
      totalPaginate: 0,
      paginateSelect: 1
    };
  },

  watch: {
    paginateSelect(val) {
      this.paginateSelect = val;
      
      axios
        .get(
          "http://localhost:8001/api/v1/contacts?limit=25&offset=" +
            25 * (val - 1)
        )
        .then(data => {
          this.payloads = data.data.results;

          this.canPrev = data.data.previous;
          this.canNext = data.data.next;
          this.totalPaginate = Math.ceil(data.data.count / 25);
        });
    }
  },

  mounted() {
    axios.get("http://localhost:8001/api/v1/contacts?limit=25").then(data => {
      this.payloads = data.data.results;

      this.canPrev = data.data.previous;
      this.canNext = data.data.next;
      this.totalPaginate = Math.ceil(data.data.count / 25);
    });
  }
};
</script>