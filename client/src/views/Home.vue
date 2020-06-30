<template>
  <div>
    <Subheader
      title="History Log"
      subtitle="List of history log from action bot instagram and scraping data"
    />
    <Table
      title="All history"
      subtitle="You can read history usage this application"
      :payloads="payloads"
      :fields="['description', 'created_date']"
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
      payloads: []
    };
  },

  mounted() {
    axios
      .get("http://localhost:8001/api/v1/histories?limit=25&ordering=-id")
      .then(data => {
        this.payloads = data.data.results;
      });

    this.$pusher.subscribe("notice").bind("log", data => {
      data.created_date = new Date();
      data.description = data.message;

      this.payloads.unshift(data);
    });
  }
};
</script>