<template>
  <div>
    <Subheader title="Bot Account" subtitle="List of bot account for instagram" />
    <Table
      title="Bot Account"
      subtitle="You can read all bot account instagram"
      :payloads="payloads"
      :fields="['username', 'password']"
      :create="true"
      :showForm.sync="showForm"
      v-if="showForm == false"
      :destroy="destroy"
      :indexEdit.sync="indexEdit"
      :canPrev.sync="canPrev"
      :canNext.sync="canNext"
      :totalPaginate.sync="totalPaginate"
      :paginateSelect.sync="paginateSelect"
    />

    <Form
      title="Bot Account"
      subtitle="You can create or upate bot account instagram"
      v-else
      :showForm.sync="showForm"
      :submit="submit"
      :indexEdit.sync="indexEdit"
    >
      <div class="form-group row">
        <div class="col-lg-6">
          <label>Username:</label>
          <input
            type="text"
            class="form-control"
            placeholder="Enter username"
            v-model="data.username"
          />
          <span class="form-text text-muted">Please enter your username</span>
        </div>
        <div class="col-lg-6">
          <label>Password:</label>
          <input
            type="text"
            class="form-control"
            placeholder="Enter password"
            v-model="data.password"
          />
          <span class="form-text text-muted">Please enter your password</span>
        </div>
      </div>
    </Form>
  </div>
</template>

<script>
import Subheader from "../components/Subheader";
import Table from "../components/Table";
import Form from "../components/Form";

import axios from "axios";

export default {
  components: {
    Subheader,
    Table,
    Form
  },

  data() {
    return {
      payloads: [],
      showForm: false,
      indexEdit: -1,
      canPrev: false,
      canNext: false,
      totalPaginate: 0,
      paginateSelect: 1,

      data: {
        username: "",
        password: ""
      }
    };
  },

  watch: {
    indexEdit(val) {
      if (val > -1) {
        this.data = this.payloads[val];
        this.showForm = true;
      } else {
        this.data = {
          username: "",
          password: ""
        };
        this.showForm = false;
      }
    },

    paginateSelect(val) {
      axios
        .get(
          "http://localhost:8001/api/v1/bots?limit=25&offset=" + 25 * (val - 1)
        )
        .then(data => {
          this.payloads = data.data.results;

          this.canPrev = data.data.previous;
          this.canNext = data.data.next;
          this.totalPaginate = Math.ceil(data.data.count / 25);
        });
    }
  },

  methods: {
    submit() {
      axios.post("http://localhost:8001/api/v1/bots", this.data).then(data => {
        this.payloads.push(data.data);
        this.showForm = false;
      });
    },

    destroy(index) {
      if (
        confirm(
          "Are you sure delete bot with username " +
            this.payloads[index].username +
            " ?"
        )
      ) {
        axios
          .delete(
            "http://localhost:8001/api/v1/bots/" + this.payloads[index].id
          )
          .then(() => {
            this.payloads.splice(index, 1);

            alert("Delete bot success");
          });
      }
    }
  },

  mounted() {
    axios.get("http://localhost:8001/api/v1/bots?limit=25").then(data => {
      this.payloads = data.data.results;

      this.canPrev = data.data.previous;
      this.canNext = data.data.next;
      this.totalPaginate = Math.ceil(data.data.count / 25);
    });
  }
};
</script>